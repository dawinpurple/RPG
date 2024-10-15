import random
class 캐릭터:
    def __init__(self,name,HP,ATK,DEF):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

        self.defdef = self.DEF
        self.atkatk = self.ATK
        self.stun_turn = 0
        self.take_destroye = 0
        self.take_Weakened = 0
        self.take_blodblod = 0

    def attack_target(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격하여 {self.ATK}의 피해를 입혔습니다.')
        # 타겟이 공격을 받음을 전달
        target.take_damage(self.ATK)
    
    def 기절(self):
        if self.stun_turn > 0:
                damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened


    def take_damage(self,damage):
        if damage<self.DEF:
            self.DEF = damage
        self.HP-=(damage-self.DEF)
        if self.HP<=0:
            print(f'{self.name}이(가) 치명상을 입었다.')
        else:
            #print("                  ")
            if self.DEF > 0:
                print(f'{self.name}은(는) {self.DEF}만큼의 피해를 막았다.')
                #input('enter 키를 눌러 진행하십시오.')
                #print("                  ")
            elif self.DEF < 0:
                print(f'{self.name}은(는) {-self.DEF}만큼의 피해를 더 받았다.')
                #input('enter 키를 눌러 진행하십시오.')
                #print("                  ")
            print(f'{self.name}의 현제 체력:{self.HP}')


    def take_blod(self,blod):
        if blod > 0:
            self.take_blodblod+=blod
            print(f'{self.name}이(가) 출혈 상태에 빠져 턴이 끝날 때 {self.take_blodblod}만큼 피해를 받는다.')
        else:
            #input('enter 키를 눌러 진행하십시오.')
            print(f'{self.name}이(가) 출혈로 인해 {self.take_blodblod} 만큼 피해를 받는다.')
            self.HP-=self.take_blodblod
            self.take_blodblod//=3
            #input('enter 키를 눌러 진행하십시오.')
            print(f'{self.name}의 출혈 수치가 2/3로 줄어든다.(출혈 수치-{self.take_blodblod})')

    #스턴(공격력 절반 감소)(부여할때 1 더 넣어야 작동함)
    def take_stun(self,stun):
        self.stun_turn += stun
        if self.stun_turn > 0:
            self.stun_turn = self.stun_turn - 1
        if self.stun_turn > 0:
            #print("                  ")
            if stun == 0:
                print(f'{self.name}은(는) 현제 기절 상태에 빠져 {self.stun_turn}턴동안 공격력이 절반으로 감소한다.(현재 {self.name}의 공격력{self.ATK//2})')
            else:
                print(f'{self.name}이(가) 기절 상태에 빠져 {self.stun_turn}턴동안 공격력이 절반으로 감소한다.(현재 {self.name}의 공격력{self.ATK//2})')
    #파괴(방어력감소)
    def take_dest(self,destroye):
        self.take_destroye += destroye
        if self.take_destroye > 0:
            self.DEF -= destroye
            #print("                  ")
            print(f'{self.name}의 방어가 파괴되어 이번 턴동안 방어력이 {destroye} 감소한다.(현재 {self.name}의 방어력{self.DEF})')
        elif self.take_destroye == 0:
            print(f'{self.name}의 파괴 상태이상이 해제되었다.')
            self.DEF = self.defdef
        self.take_destroye = 0
    
    #약화(공격력감소)
    def take_Weak(self,Weakened):
        self.take_Weakened += Weakened
        if Weakened > 0:
            print(f'{self.name}의 공격력이 약화되어 이번 턴동안 공격력이 {Weakened} 감소한다.(현재 {self.name}의 공격력{self.ATK-Weakened})')
        else:
            print(f'{self.name}의 약화 상태이상이 해제되었다.')
            self.take_Weakened=0

class 격투가(캐릭터):
    def __init__(self):
        super().__init__(name = "격투가",HP=100,ATK=20,DEF = 5)
        
    def 스킬_2연타(self,target):
        damage= 20
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) 왼손을 날려 {target.name}에게 {damage-10}만큼의 피해를 입혔다.')
        target.take_damage(damage-10)
        #input('enter 키를 눌러 진행하십시오.')
        #print("                  ")
        print(f'{self.name}이(가) 곧바로 오른손을 휘둘러 {target.name}에게 {damage}만큼의 피해를 입혔다.')
        target.take_damage(damage)

    def 기절시키기(self,target):
        damage=self.ATK//2
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        stun = 1
        print(f'{self.name}이(가) {target.name}의 머리를 빠르게 쳐 {damage}만큼의 피해를 입히고,기절을{stun} 부여했다.')
        target.take_damage(damage)
        target.take_stun(2)

    def 반격(self,target):
        damage = self.ATK+25
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) {target.name}을(를) 도발해 공격을 유도했다.')
        #input('enter 키를 눌러 진행하십시오.')
       # print("                  ")
        print(f'{target.name}이(가) {self.name}을(를) 향해 주먹을 날려 {target.ATK}만큼의 피해를 입혔다.')
        self.take_damage(target.ATK)
        #input('enter 키를 눌러 진행하십시오.')
        #print("                  ")
        print(f'{self.name}이(가) 순간적으로 {target.name}을(를) 걷어차 {damage}만큼의 피해를 입혔다.')
        target.take_damage(damage)

class 결투가(캐릭터):
    def __init__(self):
        super().__init__(name = "결투가",HP=80,ATK=25,DEF = 0)
    
    def 돌진(self,target):
        damage = self.ATK
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        a = random.randint(1,2)
        if self.stun_turn > 0:
            print('이 기술은 기절의 공격력 감소 영향을 받지 않는 대신 치명상을 내지 못한다.')
            a = 1
        if a == 1:
            print(f'{self.name}이(가) 무리하게 돌진하여 15 만큼의 피해를 입고 {target.name}을(를) 찔러 {damage} 만큼의 피해를 입혔다.') 
            self.take_damage(15)
            target.take_damage(damage)
        if a == 2:
            print(f'{self.name}이(가) 제빠른 돌진으로 {target.name}의 급소를 찔러 {damage*2} 만큼의 피해를 입혔다.')
            target.take_damage(damage*2)
    
    def 압박(self,target):
        damage = 13
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) 연속되는 공격으로 적을 압박한다.')
        print(f'{self.name}이(가) 정면에서 {target.name}을(를) 찔러 {damage}만큼의 피해를 입히고, 파괴를 1 부여한다')
        target.take_dest(1)
        target.take_damage(damage)
        #input('enter 키를 눌러 진행하십시오.')
        #print("                  ")
        print(f'{self.name}이(가) 뒤로 물러났다가 빠르게 발을 내딛여 {target.name}을(를) 찔러 {damage}만큼의 피해를 입히고, 파괴를 1 부여한다')
        target.take_dest(1)
        target.take_damage(damage)
        #input('enter 키를 눌러 진행하십시오.')
        #print("                  ")
        print(f'{self.name}이(가) 몸을 숙여 밑에서 {target.name}의 머리를 찔러 {damage}만큼의 피해를 입히고,파괴를 3 부여한다.')
        target.take_dest(3)
        target.take_damage(damage)

    def 찌르기(self,target):
        damage = 30
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) {target.name}을(를) 발로 차 균형을 깨뜨리고, 파괴를 10 부여했다.')
        target.take_dest(10)
        #input('enter 키를 눌러 진행하십시오.')
        #print("                  ")
        print(f'{self.name}이(가) {target.name}에게 힘을 실은 일격을 날려 {damage}만큼 피해를 입혔다.')
        target.take_damage(damage)
        #input('enter 키를 눌러 진행하십시오.')
        #print("                  ")
        print(f'과도한 움직임으로 인해 {self.name}이(가) 기절을 1 얻는다.')
        self.stun_turn+=2

class 보안관(캐릭터):
    def __init__(self):
        self.bullet = 0
        super().__init__(name = "보안관",HP=90,ATK=20,DEF = 3)

    def 격발(self,target):
        damage = self.ATK
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        if self.bullet > 0:
            print(f'{self.name}이(가) 리볼버로 {target.name}을(를) 향해 탄환을 발사해 {damage}만큼 피해를 입혔다.')
            target.take_damage(damage)
            self.bullet-=1
            #input('enter 키를 눌러 진행하십시오.')
        elif self.bullet <= 0:
            print(f'{self.name}이(가) 장전된 탄환을 모두 격발했다.')
    
    def 밀어차기(self,target):
        damage = 8
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) 부츠로 {target.name}을(를) 차내어 {damage}만큼 피해를 주고 약화를 5 부여했다.')
        target.take_damage(damage)
        target.take_Weak(5)
        #input('enter 키를 눌러 진행하십시오.')
        print('탄환을 1발 장전했다.')
        self.bullet+=1
        if self.bullet >= 7:
            print('이미 모든 탄환이 장전되어있어 장전하지 못했다.')
            self.bullet = 6
        print(f'현제 장전된 탄환{self.bullet}')

    def 머리(self,target):
        self.bullet-=1
        if self.bullet == -1:
            print('장전된 탄환이 없다.')
        else:
            damage = 55
            a = random.randint(1,2)
            if self.take_Weakened > 0:
                damage-=self.take_Weakened
            if self.stun_turn > 0:
                print('이 기술은 기절의 공격력 감소 영향을 받지 않는 대신 치명상을 내지 못한다.')
                a = 1
            if a == 1:
                print(f'{self.name}이(가) 침착하지 못하게 방아쇠를 당겨 총알이{target.name}의 머리를 스쳐 지나갔다.')
                print(f'현제 장전된 탄환{self.bullet}')
            if a == 2:
                print(f'{self.name}이(가) 노련하게 {target.name}의 머리를 정확히 조준하여 {damage}의 피해를 입히고 기절을 1 부여했다.')
                target.take_damage(damage)
                target.take_stun(2)
                print(f'현제 장전된 탄환{self.bullet}')

    def 장전(self):
        print(f"{self.name}이(가) 총알을 2발 장전했다.")
        self.bullet+=2
        if self.bullet >= 7:
            input('enter 키를 눌러 진행하십시오.')
            print('이미 모든 탄환이 장전되어있어 장전하지 못했다.')
            self.bullet = 6
        print(f'현제 장전된 탄환{self.bullet}')

class 도적우두머리(캐릭터):  #적
    def __init__(self):
        super().__init__(name = "도적 우두머리",HP=178,ATK=15,DEF = 2)
        
    def 지휘(self,target):
        damage= self.ATK
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) 투박한 총의 방아쇠를 당겨 {target.name}에게 {damage}만큼의 피해를 입혔다.')
        target.take_damage(damage)

    def 베기(self,target):
        damage=self.ATK
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) {target.name}의 배에 단검을 찔러넣어 {damage}만큼의 피해를 입히고, 파괴를 {3} 부여했다.')
        target.take_damage(damage)
        target.take_dest(3)

    def 주먹(self,target):
        damage = self.ATK-5
        if self.stun_turn > 0:
            damage//=2
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) {target.name}에게 너클을 휘둘러 {damage}만큼 피해를 준다.')
        target.take_damage(damage)
    
    def 치명타(self,target):
        damage = self.ATK-5
        if self.stun_turn > 0:
            print('이 기술은 기절의 공격력 감소 영향을 받지 않는 대신 치명상을 내지 못한다.')
            #input('enter 키를 눌러 진행하십시오.')
        if self.take_Weakened > 0:
            damage-=self.take_Weakened
        print(f'{self.name}이(가) {target.name}가 있는 방향에 너클을 마구잡이로 휘두른다.')
        #input('enter 키를 눌러 진행하십시오.')
        for i in range(0,3):
            a = random.randint(1,2)
            if self.stun_turn > 0:
                a == 2
            if a == 1:
                b = random.randint(1,2)
                if b==1:
                    print(f'너클이 {target.name}의 뼈를 으스러뜨린다. {damage}만큼 피해를 준다.')
                else:
                    print(f'너클이 {target.name}의 몸에 적중했다. {damage}만큼 피해를 준다.')
            else:
                print(f'너클이 {target.name}을 스쳐간다.')
            #input('enter 키를 눌러 진행하십시오.')

class 도적일(캐릭터):        #적
    def __init__(self):
        super().__init__(name = "도적1",HP=94,ATK=12,DEF = 3)
    
    def 절단(self,target):
        damage = self.ATK+3
        self.기절()
        print(f'톱날 형태의 단검이 {target.name}의 살을 찢어 {damage}만큼 피해를 주었다.')
        target.take_damage(damage)
    
    def 썰기(self,target):
        damage = self.ATK
        self.기절()
        print(f'{self.name}이(가) 톱날 형태의 단검을 {target.name}의 어깨에 박아넣었다. {damage-5}만큼 피해를 주었다.')
        target.take_damage(damage-5)
        #input('enter 키를 눌러 진행하십시오.')
        print(f'{self.name}이(가) 단검으로 {target.name}의 어깨를 썰어 {damage}만큼 피해를 주었다.')
        target.take_damage(damage)

class 도적이(캐릭터):        #적
    def __init__(self):
        super().__init__(name = "도적2",HP=85,ATK=16,DEF = 0)
    
    def 저격(self,target):
        damage = int(self.ATK*1.5)
        self.기절()
        print(f'{self.name}이(가) {target.name}에게 머스킷을 발사해 {damage}만큼 피해를 주었다.')
        target.take_damage(damage)
    
    def 개머리판(self,target):
        damage = int(self.ATK//2)
        self.기절()
        print(f'{self.name}이(가) 머스킷의 개머리판으로 {target.name}의 턱을 노려 {damage}만큼 피해를 주고 약화를 5 부여했다.')
        target.take_damage(damage)
        target.take_Weak(5)