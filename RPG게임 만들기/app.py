import flask
import random
from limbus_player import 캐릭터,격투가,보안관,결투가,도적우두머리,도적일,도적이
from login import load_user, add_user
app=flask.Flask(__name__)
app.secret_key="secret"



def inital_game():
    격투가1 = 격투가()
    결투가1 = 결투가()
    보안관1 = 보안관()

    heros = [격투가1,결투가1,보안관1]

    all_monsters = [
        도적우두머리(),
        도적일(),
        도적이()
    ]

    monsters = all_monsters

    return heros,monsters

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form.get('username')
        password = flask.request.form.get('password')
        print(username,password)

        if load_user(username,password):
            print(username,password)
            return flask.redirect(flask.url_for('game'))
        else:
            return "로그인 실패,아이디 또는 비밀번호를 학인하세요"
    
    return flask.render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if flask.request.method == 'POST':
        username = flask.request.form.get('username')
        password = flask.request.form.get('password')

        if not username or not password:
            return "사용자의 이름과 비밀번호를 입력하세요."
        
        if add_user(username,password):
            return flask.render_template("register.html")
        else:
            return "사용자가 이미 존재합니다."
    return flask.render_template("register.html")

@app.route('/game', methods = ['POST','GET'])
def game():
    heros,monsters = inital_game()

    flask.session['heros'] = [{'name':hero.name,'HP':hero.HP,'max_HP':hero.HP} for hero in heros]
    flask.session['monsters'] = [{'name':monster.name,'HP':monster.HP,'max_HP':monster.HP} for monster in monsters]
    
    return flask.redirect(flask.url_for('gaming'))

@app.route('/gaming')
def gaming():
    heros=flask.session.get('heros',[])
    monsters=flask.session.get('monsters',[])

    if not heros or not monsters:
        return flask.redirect(flask.url_for('index'))

    return flask.render_template('game.html',heros = heros,monsters = monsters)


@app.route('/choose_action',methods = ['POST'])
def choose_action():
    heros_data = flask.session.get('heros',[])
    monsters_data = flask.session.get('monsters',[])

    heros = []
    for hero in heros_data:
        if hero['name'] == '격투가':
            new_hero=격투가()
        elif hero['name'] == '결투가':
            new_hero=결투가()
        elif hero['name'] == '보안관':
            new_hero=보안관()
        new_hero.HP=hero['HP']
        heros.append(new_hero)

    monsters = []
    for monster in monsters_data:
        if monster['name'] == '도적 우두머리':
            new_monster=도적우두머리()
        elif monster['name'] == '도적1':
            new_monster=도적일()
        elif monster['name'] == '도적2':
            new_monster=도적이()
        new_monster.HP=monster['HP']
        monsters.append(new_monster)
    
    selected_hero_index = int(flask.request.form['hero'])
    action_index = (flask.request.form['action'])
    target_index = int(flask.request.form['target'])
    selected_hero=heros[selected_hero_index]
    target_monster=monsters[target_index]

    attack_result=""
    if action_index == "attack":
        selected_hero.attack_target(target_monster)
        attack_result=f'{selected_hero.name}이(가) {target_monster.name}을(를) 공격했습니다.'
    elif action_index == "skill":
        if isinstance(selected_hero,격투가):
            selected_hero.스킬_2연타(target_monster)
            attack_result=f'{selected_hero.name}가 {target_monster.name}에게 2연타를 사용했습니다.'
        elif isinstance(selected_hero,결투가):
            selected_hero.돌진(target_monster)
            attack_result=f'{selected_hero.name}가 {target_monster.name}에게 돌진을 사용했습니다.'
        elif isinstance(selected_hero,보안관):
            selected_hero.격발(target_monster)
            attack_result=f'{selected_hero.name}가 {target_monster.name}에게 격발을 사용했습니다.'

    monsters = [monster for monster in monsters if monster.HP>0]


    for monster in monsters:
        if monster.HP>0:
            alive_heros=[hero for hero in heros if hero.HP>0]
            if alive_heros:
                target=random.choice(alive_heros)
                monster.attack_target(target)
                attack_result+=f'\n{monster.name}이(가) {target.name}을(를) 공격했습니다.'
            break

    heros = [hero for hero in heros if hero.HP>0]
    
    flask.session['heros']=[{'name':hero.name,'HP':hero.HP,'max_HP':hero.HP} for hero in heros]
    flask.session['monsters']=[{'name':monster.name,'HP':monster.HP,'max_HP':monster.HP} for monster in monsters]

    if not heros:
        return flask.redirect(flask.url_for("result",result='몬스터 승'))
    if not monsters:
        return flask.redirect(flask.url_for("result",result='캐릭터 승'))

    return flask.render_template('game.html',heros = flask.session['heros'],monsters=flask.session['monsters'],attack_result=attack_result)

@app.route('/result')
def result():
    result_massage=flask.request.args.get('result','결과가 없습니다.')
    return flask.render_template('result.html',result=result_massage)

if __name__ =='__main__':
    app.run(debug=True)

