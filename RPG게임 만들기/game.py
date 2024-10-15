import limbus_player
import random
class 게임시작:
    def __init__(self):
        
        self.아군 = limbus_player.검객()
        self.적군 = limbus_player.격투가()
        self.juk =0
        self.적군무리 = []
        self.아군무리 = []
        self.아군이름 = []

        #도적단
        self.적군무리.append(limbus_player.도적우두머리())
        self.적군무리.append(limbus_player.도적일())
        self.적군무리.append(limbus_player.도적이())

    def 대상지정(self):
        for i in range(0,len(self.적군무리)):
            if self.적군무리[i].HP >0:
                print(i+1,self.적군무리[i].name,self.적군무리[i].HP)
        b = int(input('누구를 공격하시겠습니까?'))
        return b-1

    def 아군지정():
        a = random.randint(1,4)
        return a

    def 게임(self):
        while True:
            print('아군이 될 각기 다른 캐릭터를 4명 선택하세요.')
            print('고른 순서대로 행동하는 아군이 결정됩니다.(예시:아군1 -> 적군1 -> 아군 2)')
            print("         ")

            if limbus_player.격투가().name in self.아군이름:
                print('1.선택하셨습니다.')
                print("         ")
            else:
                print('1.격투가(공격과 수비가 적절히 합쳐진 탱커)')
                print("         ")

            if limbus_player.결투가().name in self.아군이름:
                print('2.선택하셨습니다.')
                print("         ")
            else:
                print('2.결투가(적의 방어력을 무시하는 강한 공격으로 압박하는 딜러)')
                print("         ")

            if limbus_player.보안관().name in self.아군이름:
                print('3.선택하셨습니다.')
                print("         ")
            else:
                print('3.보안관(탄환을 사용해 순간적으로 많은 피해를 주는 딜러)')
                print("         ")

            if limbus_player.검객().name in self.아군이름:
                print('4.선택하셨습니다.')
                print("         ")
            else:
                print('4.검객(여러가지 스킬을 사용해 스킬을 강화하는 올라운더)')
                print("         ")
                
            if limbus_player.마술사().name in self.아군이름:
                print('5.선택하셨습니다.')
                print("         ")
            else:
                print('5.마술사(운에 의존하는 딜러)')
                print("         ")
            
            if limbus_player.광혈인().name in self.아군이름:
                print('6.선택하셨습니다.')
                print("         ")
            else:
                print('6.광혈인(체력이 떨어질수록 버프를 받는 탱커)')
                print("         ")
            
            if limbus_player.광혈사냥꾼().name in self.아군이름:
                print('7.선택하셨습니다.')
                print("         ")
            else:
                print('7.광혈사냥꾼(출혈 디버프로 지속적인 피해를 주는 딜러)')
                print("         ")

            sel = int(input('캐릭터 앞의 번호를 입력해 선택합니다.'))
            print("         ")
            print("         ")
            print("         ")
            print("         ")
            print("         ")
            print("         ")
            print("         ")
            print("         ")
            print("         ")
            print("         ")
            if sel == 1 and limbus_player.격투가().name not in self.아군이름:
                self.아군무리.append(limbus_player.격투가())
                self.아군이름.append(limbus_player.격투가().name)

            elif sel == 2 and limbus_player.결투가().name not in self.아군이름:
                self.아군무리.append(limbus_player.결투가())
                self.아군이름.append(limbus_player.결투가().name)

            elif sel == 3 and limbus_player.보안관().name not in self.아군이름:
                self.아군무리.append(limbus_player.보안관())
                self.아군이름.append(limbus_player.보안관().name)

            elif sel == 4 and limbus_player.검객().name not in self.아군이름:
                self.아군무리.append(limbus_player.검객())
                self.아군이름.append(limbus_player.검객().name)

            elif sel == 5 and limbus_player.마술사().name not in self.아군이름:
                self.아군무리.append(limbus_player.마술사())
                self.아군이름.append(limbus_player.마술사().name)
            
            elif sel == 6 and limbus_player.광혈인().name not in self.아군이름:
                self.아군무리.append(limbus_player.광혈인())
                self.아군이름.append(limbus_player.광혈인().name)
            
            elif sel == 7 and limbus_player.광혈사냥꾼().name not in self.아군이름:
                self.아군무리.append(limbus_player.광혈사냥꾼())
                self.아군이름.append(limbus_player.광혈사냥꾼().name)
            else:
                print('중복 선택 혹은 지정되지 않은 번호의 입력은 허용되지 않습니다.')
                input('enter 키를 눌러 진행하십시오.')
                print("         ")
            if len(self.아군이름) == 4:
                break
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        print("         ")
        i=0
        turn = 1
        while True:
            for mai in range(0,4):
                #아군 인원수 체크
                if len(self.아군무리)-1 < i:
                    i = 0
                #아군 사망 확인
                for j in range(0,4):
                    if self.아군무리[i].HP <= 0:
                        print(f'{self.아군무리[i].name} 사망.')
                        self.아군무리.remove(self.아군무리[i])
                #턴수 확인
                if mai ==4:
                    turn+=1

                print(f'현제 턴:{turn}')
                print(f'참고-모든 캐릭터가 한번씩 행동해야 한 턴이 넘어갑니다')
                input('enter 키를 눌러 진행하십시오.')
                print("         ")
                print(f'아군의 체력')
                print("         ")
                for ha in range(0,len(self.아군무리)):
                    print(f'{self.아군무리[ha].name}:{self.아군무리[ha].HP}')
                input('enter 키를 눌러 진행하십시오.')
                print("         ")
                #아군 턴
                print(f'행동 차례:{self.아군이름}')
                print("         ")
                print(f"{self.아군이름[i]}의 턴.")
                print("         ")
                input('enter 키를 눌러 진행하십시오.')
                print("         ")
                print("행동을 선택하세요.")
                print("         ")
                #격투가일시..
                if self.아군무리[i].name == "격투가":
                    print(f'현제 격투가의 공격력{self.아군무리[i].ATK}')
                    print(f'현제 격투가의 체력과 방어력 {self.아군무리[i].HP},{self.아군무리[i].DEF}')
                    print("         ")
                    print('(방어력:적의 피해를 방어력만큼 감소시켜 받음)')
                    print("         ")
                    print("격투가의 스킬")
                    print("         ")
                    print("1.2연타 (공격력의 절반으로 한번,공격력 그대로 한번씩 공격한다.)")
                    print("         ")
                    print("2.기절시키기 (공격력의 절반으로 공격하고,기절을 1 부여한다.)")
                    print("         ")
                    print("3.반격 (상대의 공격력만큼의 피해를 받고 공격력+20의 피해로 공격한다.)")
                    print("         ")
                    print("기절:수치만큼의 턴이 진행될동안 공격력을 절반으로 감소시킨다.")
                    a = int(input())
                    print("         ")

                    #스킬칸(복잡해요..)
                    if a == 1:
                        self.아군무리[i].스킬_2연타(self.적군무리[self.대상지정()])
                    if a == 2:
                        self.아군무리[i].기절시키기(self.적군무리[self.대상지정()])
                    if a == 3:
                        self.아군무리[i].반격(self.적군무리[self.대상지정()])
                    if self.아군무리[i].HP <=0:
                        print('격투가 사망.')
                    #격투가 코딩 끝

                #결투가일시..
                elif self.아군무리[i].name == "결투가":
                    print(f'현제 결투가의 공격력 {self.아군무리[i].ATK}')
                    print(f'현제 결투가의 체력과 방어력 {self.아군무리[i].HP},{self.아군무리[i].DEF}')
                    print("         ")
                    print('(방어력:적의 피해를 방어력만큼 감소시켜 받음)')
                    print("         ")
                    print("결투가의 스킬")
                    print("         ")
                    print("1.쾌속돌진 (확률적으로 치명타를 날려 공격력의 2배에 달하는 피해를 주거나,15의 피해를 받고 원래 공격력만큼 공격한다.)")
                    print("         ")
                    print("2.압박 (11의 공격력으로 3번까지 공격하며,1,2번째엔 1,마지막 공격에 3의 파괴를 부여한다.)")
                    print("         ")
                    print("3.파괴 (파괴를 10 부여하고 30의 피해를 주며,자신에게 기절을 1 부여한다.)")
                    print("         ")
                    print("**주의** '쾌속돌진' 기술은 기절 상태일 때 치명타를 날리지 못한다.")
                    print("기절:수치만큼의 턴이 진행될동안 공격력을 절반으로 감소시킨다.")
                    print("파괴:이번 턴동안 상대의 방어력을 감소시킨다.")
                    a = int(input())
                    print("         ")
                    
                    #스킬칸(복잡해요..)
                    if a == 1:
                        self.아군무리[i].쾌속돌진(self.적군무리[self.대상지정()])
                    if a == 2:
                        self.아군무리[i].압박(self.적군무리[self.대상지정()])
                    if a == 3:
                        self.아군무리[i].파괴(self.적군무리[self.대상지정()])
                    if self.아군무리[i].HP <= 0:
                        print('결투가 사망.')
                         
                    #결투가 코딩 끝

                #보안관일시..
                elif self.아군무리[i].name == "보안관": 
                    print(f'현제 보안관의 공격력 {self.아군무리[i].ATK}')
                    print(f'현제 보안관의 체력과 방어력 {self.아군무리[i].HP},{self.아군무리[i].DEF}')
                    print(f'현제 보안관의 탄환:{self.아군무리[i].bullet}')
                    print("         ")
                    print('(방어력:적의 피해를 방어력만큼 감소시켜 받음)')
                    print('(탄환:보안관의 특정 기술에 사용되며, 6발까지 장전할 수 있다.)')
                    print("         ")
                    print("보안관의 스킬")
                    print("         ")
                    print("1.격발 (탄환을 모두 소모해 발당 20의 피해를 준다.)")
                    print("         ")
                    print("2.밀어차기 (8의 피해를 입히고, 약화를 5 부여하며 탄환을 1발 장전한다.)")
                    print("         ")
                    print("3.구멍내기 (머리를 조준해 50%의 확률로 55의 피해를 입히고 기절을 1 부여하며 탄환을 1발 소모한다.)")
                    print("         ")
                    print('4.장전 (탄환을 2발 장전한다.)')
                    print("         ")
                    print("**주의** '구멍내기' 기술은 기절 상태일 때 머리를 조준하지 못한다.")
                    print("기절:수치만큼의 턴이 진행될동안 공격력을 절반으로 감소시킨다.")
                    print("약화: 이번 턴동안 공격력을 수치만큼 감소시킨다.")
                    a = int(input())
                    print("         ")

                    #스킬칸(복잡해요..)
                    if a == 1:
                        self.아군무리[i].격발(self.적군무리[self.대상지정()])
                    if a == 2:
                        self.아군무리[i].밀어차기(self.적군무리[self.대상지정()])
                    if a == 3:
                        self.아군무리[i].구멍내기(self.적군무리[self.대상지정()])
                    if a == 4:
                        self.아군무리[i].장전()
                    #보안관 코딩 끝

                #검객일시..
                elif self.아군무리[i].name == "검객": 
                    print(f'현제 검객의 공격력 {self.아군무리[i].ATK}')
                    print(f'현제 검객의 체력과 방어력 {self.아군무리[i].HP},{self.아군무리[i].DEF}')
                    print(f'현제 검객의 콤보:{self.아군무리[i].combo}')
                    print("         ")
                    print('(방어력:적의 피해를 방어력만큼 감소시켜 받음)')
                    print('(콤보:수치가 3에 도달했을 때, 다음 공격이 강화된다.(수치당 공격력이 5 증가한다.))')
                    print("         ")
                    print("검객의 스킬")
                    print("         ")
                    if self.아군무리[i].combo < 3:
                        print("1.가르기 (공격력+5 만큼의 피해를 준다.)")
                        print("         ")
                        print("2.찔러넣기 (공격력-5 만큼의 피해를 2번 입히며, 첫 번째 공격이 파괴를 5 부여한다)")
                        print("         ")
                        print("3.내려쳐베기 (팔을 잘라내 공격력만큼의 피해를 입히고 약화를 3 부여한다.)")
                    elif self.아군무리[i].combo == 3:
                        print('스킬 강화')
                        print("1.발도술 (공격력의 세 배 만큼의 피해를 준다.)")
                        print("         ")
                        print("2.약점 간파 (공격력-5만큼의 피해를 3번 입힌다.)")
                        print("         ")
                        print("3.머리가르기 (머리를 내려베어 공격력의 두 배 만큼의 피해를 입히고 기절을 2 부여한다.)")
                    print("         ")
                    print("**주의** '콤보' 패시브는 같은 스킬을 2번 연속으로 사용할 시 수치가 0이 된다.")
                    print("기절:수치만큼의 턴이 진행될동안 공격력을 절반으로 감소시킨다.")
                    print("약화:이번 턴동안 공격력을 수치만큼 감소시킨다.")
                    print("파괴:이번 턴동안 상대의 방어력을 감소시킨다.")
                    a = int(input())
                    print("         ")

                    #스킬칸(복잡해요..)
                    if a == 1:
                        self.아군무리[i].가르기(self.적군무리[self.대상지정()])
                    if a == 2:
                        self.아군무리[i].찔러넣기(self.적군무리[self.대상지정()])
                    if a == 3:
                        self.아군무리[i].내려쳐베기(self.적군무리[self.대상지정()])
                    #검객 코딩 끝

                #마술사일시..
                elif self.아군무리[i].name == "마술사":
                    print('클로버-마술사는 매턴 체력,공격력,방어력 중 하나의 수치에 영구적으로 -7~+7 만큼의 값을 더한다.')
                    input('enter 키를 눌러 진행하십시오.')
                    print("         ")
                    self.아군무리[i].도박()
                    input('enter 키를 눌러 진행하십시오.')
                    print("         ")
                    print(f'현제 마술사의 공격력 {self.아군무리[i].ATK}')
                    print(f'현제 마술사의 체력과 방어력 {self.아군무리[i].HP},{self.아군무리[i].DEF}')
                    print('(방어력:적의 피해를 방어력만큼 감소시켜 받음)')
                    print("         ")
                    print("마술사의 스킬")
                    print("         ")
                    print("1.스페이드 (공격력만큼의 피해를 3번 준다.)")
                    print("         ")
                    print("2.다이아 (자신의 방어력만큼 상대에게 파괴를 부여하고, 공격력+방어력 만큼의 피해를 입힌다)")
                    print("         ")
                    print("3.하트 (자신에게 5~20만큼의 고정피해를 주고,자신이 사망했다면 77의 체력을 얻고 부활한다.)")
                    print("         ")
                    print("파괴:이번 턴동안 상대의 방어력을 감소시킨다.")
                    a = int(input())
                    print("         ")

                    #스킬칸(복잡해요..)
                    if a == 1:
                        self.아군무리[i].스페이드(self.적군무리[self.대상지정()])
                    if a == 2:
                        self.아군무리[i].다이아(self.적군무리[self.대상지정()])
                    if a == 3:
                        self.아군무리[i].하트()
                    if self.아군무리[i].HP <= 0:
                        print(f'{아군무리[i].name} 사망.')
                    #마술사 코딩 끝

                #광혈인일시..
                if self.아군무리[i].name == "광혈인":
                    print(f'현제 광혈인의 공격력{self.아군무리[i].ATK}')
                    print(f'현제 광혈인의 체력과 방어력 {self.아군무리[i].HP},{self.아군무리[i].DEF}')
                    print("         ")
                    print('(방어력:적의 피해를 방어력만큼 감소시켜 받음)')
                    print("         ")
                    print("광혈인의 스킬")
                    print("         ")
                    print("1.혈전 (잃은 체력 10당 1의 공격력을 얻고, 공격력만큼 피해를 주며 상대의 공격력만큼 피해를 받는다.)")
                    print("         ")
                    print("2.물어찢기 (잃은 체력 5당 1의 공격력을 얻고, 공격력만큼 피해를 주며 공격력만큼 체력을 회복한다.)")
                    print("         ")
                    print("3.흡수 (공격력만큼 피해를 주고, 상대의 방어력과 공격력을 영구적으로 2 훔친다.)")
                    print("         ")
                    print("약화:이번 턴동안 상대의 공격력을 수치만큼 감소시킨다.")
                    print("파괴:이번 턴동안 상대의 방어력을 수치만큼 감소시킨다.")
                    a = int(input())
                    print("         ")

                    #스킬칸(복잡해요..)
                    if a == 1:
                        self.아군무리[i].혈전(self.적군무리[self.대상지정()])
                    if a == 2:
                        self.아군무리[i].물어찢기(self.적군무리[self.대상지정()])
                    if a == 3:
                        self.아군무리[i].흡수(self.적군무리[self.대상지정()])
                    if self.아군무리[i].HP <=0:
                        print('광혈인 사망.')
                    #광혈인 코딩 끝

                #광혈사냥꾼일시..
                if self.아군무리[i].name == "광혈사냥꾼":
                    print(f'현제 광혈사냥꾼의 공격력{self.아군무리[i].ATK}')
                    print(f'현제 광혈사냥꾼의 체력과 방어력 {self.아군무리[i].HP},{self.아군무리[i].DEF}')
                    print("         ")
                    print('(방어력:적의 피해를 방어력만큼 감소시켜 받음)')
                    print("         ")
                    print("광혈사냥꾼의 스킬")
                    print("         ")
                    print("1.출혈유발 (공격력만큼 피해를 주고 출혈을 6 부여한다.)")
                    print("         ")
                    print("2.벌집 (공격력+대상의 출혈 수치만큼 피해를 주고 대상의 출혈 수치를 2배로 늘린다.)")
                    print("         ")
                    print("3.피빼기 (공격력의 절반만큼의 피해와 파괴를 3 부여하고, 대상의 출혈을 3 소모해 대상의 출혈만큼 피해를 준다.(최대 5번))")
                    print("         ")
                    print("출혈:턴이 끝날때 수치만큼 고정 피해를 받고 수치가 2/3로 줄어든다.")
                    print("파괴:이번 턴동안 상대의 방어력을 수치만큼 감소시킨다.")
                    a = int(input())
                    print("         ")

                    #스킬칸(복잡해요..)
                    if a == 1:
                        self.아군무리[i].출혈유발(self.적군무리[self.대상지정()])
                    if a == 2:
                        self.아군무리[i].벌집(self.적군무리[self.대상지정()])
                    if a == 3:
                        self.아군무리[i].피빼기(self.적군무리[self.대상지정()])
                    if self.아군무리[i].HP <=0:
                        print('광혈사냥꾼 사망.')
                    #광혈인 코딩 끝

                #상태이상 확인
                if i == 4:
                    for o in range(0,len(self.아군무리)):
                        self.아군무리[o].take_stun(0)
                        self.아군무리[o].take_dest(0)
                        self.아군무리[o].take_Weak(0)
                i+=1

                #적 턴
                #적 사망인원 체크
                for O in range(0,len(self.적군무리)):
                    if self.적군무리[O].HP <= 0:
                        print(f'{self.적군무리[O].name} 사망.')
                        self.적군무리.remove(self.적군무리[self.juk])
                #적 무리 인원수 체크
                if len(self.적군무리)-1 < self.juk:
                    self.juk = 0

                print('아군 턴 끝.')
                input('enter 키를 눌러 진행하십시오.')
                print("                  ")
                print(f"{self.적군무리[self.juk].name}(적)의 턴.")

                #도적우두머리
                if self.적군무리[self.juk].name == "도적 우두머리":
                    if self.적군무리[self.juk].HP > 50:
                        aattack = [1,1,2,2,2,3]
                    elif self.적군무리[self.juk].HP <= 25 or len(self.적군무리) == 1:
                        print('우두머리가 큰 혼란을 느낀다.')
                        print("                  ")
                        aattack = [4,3,3,4,4,4]
                    elif self.적군무리[self.juk].HP <= 50 or len(self.적군무리) == 2:
                        print('우두머리의 계획이 틀어진다.')
                        print("                  ")
                        aattack = [2,3,3,1,4,4]
                    a = random.choice(aattack)
                    if a == 1:
                        self.적군무리[self.juk].지휘(self.아군무리[random.randint(0,3)])
                        #도적단 강화
                        if len(self.적군무리) >= 1:
                            input('enter 키를 눌러 진행하십시오.')
                            print("                  ")
                            print(f'{self.적군무리[self.juk].name}의 신호를 받은 도적단원들이 5의 공격력을 얻는다.')
                            for m in range(1,len(self.적군무리)):
                                input('enter 키를 눌러 진행하십시오.')
                                print("                  ")
                                self.적군무리[m].ATK += 5
                                print(f'{self.적군무리[m].name}이(가) 5의 공격력을 얻었다.')
                    if a == 2:
                        self.적군무리[self.juk].녹슨칼날(self.아군무리[random.randint(0,3)])
                    if a == 3:
                        self.적군무리[self.juk].틀어질계획(self.아군무리[random.randint(0,3)])
                    if a == 4:
                        self.적군무리[self.juk].계산실수(self.아군무리[random.randint(0,3)])

                #도적1
                elif self.적군무리[self.juk].name == "도적단 처형자":
                    if self.적군무리[self.juk].HP > 25:
                        aattack = [1,1,1,2,2]
                    elif self.적군무리[self.juk].HP <= 25:
                        print('처형자는 최후를 직감했다.')
                        print("                  ")
                        aattack = [3]
                    a = random.choice(aattack)
                    if a == 1:
                        self.적군무리[self.juk].절단(self.아군무리[random.randint(0,3)])
                    if a == 2:
                        self.적군무리[self.juk].썰기(self.아군무리[random.randint(0,3)])
                    if a == 3:
                        self.적군무리[self.juk].이판사판(self.아군무리[random.randint(0,3)])

                #도적2
                elif self.적군무리[self.juk].name == "도적단 총사수":
                    if self.적군무리[self.juk].HP > 25:
                        aattack = [1,1,1,2,2]
                    elif self.적군무리[self.juk].HP <= 25:
                        print('총사수의 유약한 정신은 피칠갑된 자신의 신체조차 돌보지 못한다.')
                        print("                  ")
                        aattack = [3]
                    a = random.choice(aattack)
                    if a == 1:
                        self.적군무리[self.juk].저격(self.아군무리[random.randint(0,3)])
                    if a == 2:
                        self.적군무리[self.juk].개머리판(self.아군무리[random.randint(0,3)])
                    if a == 3:
                        self.적군무리[self.juk].붕괴()
                        print("도적단 총사수 사망")


                #만약 격투가라면..
                if self.적군무리[self.juk].name == "격투가":
                    if self.적군무리[self.juk].HP > 50:
                        aattack = [1,1,1,2,3,3]
                    elif self.적군무리[self.juk].HP <= 50:
                        print('격투가가 위기를 감지하고 수비적인 자세를 취한다.')
                        print("                  ")
                        aattack = [1,1,2,2,2,3]
                    a = random.choice(aattack)
                    if a == 1:
                        self.적군무리[self.juk].스킬_2연타(self.아군무리[random.randint(0,3)])
                    if a == 2:
                        self.적군무리[self.juk].기절시키기(self.아군무리[random.randint(0,3)])
                    if a == 3:
                        self.적군무리[self.juk].반격(self.아군무리[random.randint(0,3)])
                    #격투가 코딩 끝.
                
                #만약 결투가라면..
                if self.적군무리[self.juk].name == "결투가":
                    if self.적군무리[self.juk].HP > 75:
                        aattack = [1,1,1,2,2,2]
                    elif self.적군무리[self.juk].HP <= 75:
                        print('결투가는 몸에 무리를 주어 전투에 임하기 시작했다.')
                        aattack = [1,1,2,1,3,3]
                    a = random.choice(aattack)
                    if a == 1:
                        self.적군무리[self.juk].쾌속돌진(self.아군무리[random.randint(0,4)])
                    if a == 2:
                        self.적군무리[self.juk].압박(self.아군무리[random.randint(0,4)])
                    if a == 3:
                        self.적군무리[self.juk].파괴(self.아군무리[random.randint(0,4)])
                    #결투가 코딩 끝.

                if self.juk == len(self.적군무리):
                    for l in range(0,len(self.아군무리)):
                        self.적군무리[l].take_stun(0)
                        self.적군무리[l].take_dest(0)
                        self.적군무리[l].take_Weak(0)
                self.juk+=1
                input('enter 키를 눌러 진행하십시오.')
                print("                  ")



gamee = 게임시작()
gamee.게임()

        #print('아군이 될 캐릭터를 선택하세요.')
        #print('1.격투가(공격과 수비가 적절히 합쳐진 탱커)')
        #print('2.결투가(적의 방어력을 무시하는 강한 공격으로 압박하는 딜러)')
        #print('3.보안관(탄환을 사용해 순간적으로 많은 피해를 주는 딜러)')
        #print('4.검객(여러가지 스킬을 사용해 스킬을 강화하는 올라운더)')
        #sel = input('캐릭터 앞의 번호를 입력해 선택합니다.')
        #if sel == 1:
        #    self.아군 = limbus_player.격투가()
        #elif sel == 2:
        #    self.아군 = limbus_player.결투가()
        #elif sel == 3:
        #    self.아군 = limbus_player.보안관()
        #elif sel == 4:
        #    self.아군 = limbus_player.검객()