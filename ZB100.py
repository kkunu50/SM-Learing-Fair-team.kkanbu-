import random
#리스트,튜플,딕셔너리
#모든 캐릭터의 스테이터스는 [체력, 공격력]순으로 적는다.
player = [100, 15]
nomal_zombie_status = [40, 5]
doctor_zombie_status = [50, 5]
soldier_zombie_status = [80, 10]
police_zombie_status = [70, 10]
thief_status = [60, 10]
player_inventory = []
player_status = { }
player_equipment = {"무기" : "맨손", "방어구": "반팔"}
player_weapon = {"전기톱" : 20, "마체테" : 10, "담임선생님의 단소" : 15, "맨손" : 0}
player_armor = {"롱패딩" : 50, "가죽재킷" : 40, "상명대학교 과잠" : 100, "트레이닝복" : 30, "코트" : 40, "반팔" : 0}
gold = {"골드" : 100}
day = [1]
#스토리 함수
def start_story1():
    print("20XX년 의문의 바이러스가 한국에 강타했다.\n")
    print("바이러스에 감염된 사람들은 사람들을 물기 시작했고, 사람들은 그것을 좀비라 칭했습니다. \n")
    print("국가는 비상사태를 선포했고, 전국이 한순간에 마비가 되었다. \n")
    print("당신은 겁을 먹고, 구조대를 기다리며 집에 모든 문을 막으며 집에서 나가지 않았습니다.\n")
    print("하지만 구조대는 오지 않았고, 생필품들이 바닥이 나기 시작했습니다.\n")
    print("당신은 생필품을 찾아 집을 떠나야 겠다는 생각이 들었고 밖 상황을 살피기 시작했습니다.\n")
    print("좀비를 관찰하다가 좀비가 낮에는 활동성이 크게 떨어지고, 소리와 냄새에만 반응한다는 것을 알게되었습니다.\n")
    print("그렇게 당신은 어떤 무기를 들고 나갈까 생각하며 나갈 준비를 했습니다.\n")
    print("그렇게 당신은 무기를 챙기고 밖으로 나갔습니다.\n")
    print("당신은 낮에만 활동을 했고, 좀비들의 신경을 안끌려고 노력을 했습니다.")
    print("----------------------------------------")
    input("")
    print("그렇게 좀비를 피해 다니다 생존자 집단을 만나게 되었습니다.\n")
    print("당신은 오랜만에 본 사람인지라 너무 반가웠고, 빠르게 다가갔습니다.\n")
    print("하지만 생존자 집단은 당신을 경계했습니다.\n")
    print("당신은 좀비가 아니란 걸 필사적으로 말했고, 좀비를 피해 도망다니다 여기를 발견하게 됐다고 말했습니다.\n")
    print("당신은 그들의 경계심을 풀기 위해 좀비에게 물리지 않았으며 안전하단 걸 보여주었습니다.\n")
    print("그제서야 생존자 집단은 당신을 받아주었고, 당신은 집단에서 생활하게 되었습니다..\n")
    print("생존자 집단 당신은 바깥에서 무슨 일을 했는지 물어봤습니다.(나중에 변경 불가능)")
    input("")
    job()
    
def start_story2():
    print("----------------------------------------")
    print("당신은", player_status["직업"], "(이)였다고 말했습니다. \n")
    print("그렇게 얘기를 하며 생활을 하고 있었습니다. \n")
    print("어느정도 시간이 흐른 후 생활에 필요한 물품들이 바닥이 나기 시작했습니다. \n")
    print("생존자 집단은 생존에 필요한 물품들을 가져와야 할 거 같다고 말하면서 갈 사람이 있는지 물어봤습니다. \n")
    print("당신은 고민을 했습니다. 좀비가 있는 끔찍한 곳을 가기 싫었기 때문입니다.\n")
    print("당신은 당신을 받아준 곳이니 은혜를 갚아야겠다는 생각이 했습니다.\n")
    print("그래서 당신은 자진해서 가겠다고 했습니다.\n")
    print("그렇게 당신은 생필품을 찾으러 밖에 나갔습니다.")
    input("")

#직업 함수
def job():
    print("----------------------------------------")
    print("1. 군인: 기본 체력이 높다(체력 +30)")
    print("2. 의사: 좀비 감염, 상태이상 각각 1회 치유가능.")
    print("3. 사냥꾼: 무기에 대한 이해도가 높아 공격력이 증가한다.(공격력 +10)")
    print("4. 탐험가: 함정에 대한 이해도가 높아 함정에 걸리지 않는다.")
    print("5. 도박사: 도박을 한다. 전투시 도망칠 확률이 높아지는 대신 실패하면 데미지를 2배 더 받는다.")
    print("6. 영업사원: 상점가에서 40%할인을 받는다.")
    print("----------------------------------------\n")
    while True:
        job_select = input("당신의 직업을 선택하세요(숫자로 입력): ")
        if job_select == "1":
            player_status["직업"] = "군인"
            player[0] += 30
            break
        elif job_select == "2":
            player_status["직업"] = "의사"
            gain_item("좀비바이러스 치료제")
            gain_item("타이레놀")
            break
        elif job_select == "3":
            player_status["직업"] = "사냥꾼"
            player[1] += 10
            break
        elif job_select == "4":
            player_status["직업"] = "탐험가"
            break
        elif job_select == "5":
            player_status["직업"] = "도박사"
            break
        elif job_select == "6":
            player_status["직업"] = "영업사원"
            break
    
#전투 함수
def nomal_zombie():
    print("당신은 보급품을 찾기위해 빈집으로 들어갑니다. \n")
    print("수색해봤지만 별로 얻을 만한 것은 없었습니다. \n")
    print("집에서 나가기 위해 현관문을 열자 좀비가 나타났습니다. \n")
    print("모습을 보아하니 일반좀비입니다.")
    print("----------------------------------------")
    Enemy = nomal_zombie_status.copy()
    fight(Enemy)

def doctor_zombie():
    print("당신은 병원에 들어가서 약을 찾기 시작합니다. \n")
    print("하지만 실수로 근처 수술도구를 떨어트렸습니다. \n")
    print("소리를 들은 좀비들이 몰려옵니다. \n")
    print("모습을 보아하니 의사좀비입니다.")
    print("----------------------------------------")
    Enemy = doctor_zombie_status.copy()
    fight(Enemy)

def soldier_zombie():
    print("당신은 무기를 찾기위해 군부대로 몰래 들어갑니다. \n")
    print("보급고를 발견했지만 근처 좀비에게 발각되고 말았습니다. \n")
    print("모습을 보아하니 군인좀비입니다.")
    print("----------------------------------------")
    Enemy = soldier_zombie_status.copy()
    fight(Enemy)

def police_zombie():
    print("당신은 경찰서를 발견하였습니다. \n")
    print("경찰서에서 동료를 발견할지도 모른다는 마음에 뛰어들어갔지만 \n")
    print("그런 당신을 반겨주는건 좀비였습니다! \n")
    print("모습을 보아하니 경찰좀비입니다.")
    print("----------------------------------------")
    Enemy = police_zombie_status.copy()
    fight(Enemy)

def thief():
    print("여기엔 사람이 있었던 흔적이 있군요! \n")
    print("불을 피운지 얼마지나지 않아 보입니다. \n")
    print("다른 생존자를 볼 수도 있다는 마음에 잠깐 그곳에서 쉬기로 합니다. \n")
    print("잠시 뒤 인기척이 느껴져 뒤돌아보니 나이프를 든 도적이 있었습니다. \n")
    print("가진거 다 내놔!")
    print("----------------------------------------")
    Enemy = thief_status.copy()
    fight(Enemy)
    
def fight(Enemy):
    while True:
        print("플레이어의 체력", player[0], "플레이어의 공격력", player[1])
        print("적의 체력", Enemy[0], "적의 공격력", Enemy[1])
        print("----------------------------------------")
        while True:
            select = input("1. 공격한다 2. 도망간다 : ")
            if select == "1" or select == "2":
                break
        
        if select == "1":
            Enemy[0] = Enemy[0] - player[1]
            print("\n적에게", player[1], "의 데미지를 입혔습니다.")
            if Enemy[0] <= 0:
                print("----------------------------------------")
                print("적을 쓰러트렸습니다!\n")
                if Incident <= 13:
                    print("좀비 : 으어어어...")
                else:
                    print("도적 : 젠장 이번엔 봐줄테니 두고보라고!")
                gain_gold = random.randint(30, 60)
                print("\n적을 처치하고", gain_gold, "골드를 얻었습니다.")
                gold["골드"] = gold["골드"] + gain_gold
                input("")
                break
            
            player[0] = player[0] - Enemy[1]
            print("적에게", Enemy[1], "의 데미지를 입었습니다.")
            if player[0] <= 0 and Incident <= 13:
                player_status["감염"] = 1
                print("\n좀비에게 감염당했습니다. 3일안에 치료제를 복용해야 합니다.")
                player[0] = 5
                input("")
                break
            elif player[0] <= 0 and 14 <=Incident <= 15:
                print("도적이 휘두른 칼에 찔려 사망하였습니다.")
                print("당신은", day[0], "일 동안 생존했습니다.")
                input("")
                exit()

        elif select == "2":
            if player_status["직업"] == "도박사":
                exit_chance = random.randint(1,5)
                if exit_chance <= 4:
                    print("\n무사히 탈출했습니다.")
                    break
                else:
                    print("\n도망치는데 실패했습니다.")
                    print("\n적에게", Enemy[1] * 4, "의 데미지를 입었습니다. \n")
                    player[0] = player[0] - Enemy[1] * 4
                    if player[0] <= 0 and Incident <= 13:
                        player_status["감염"] = 1
                        print("\n좀비에게 감염당했습니다. 3일안에 치료제를 복용해야 합니다.")
                        player[0] = 5
                        input("")
                        break
                    elif player[0] <= 0 and 14 <=Incident <= 15:
                        print("도적이 휘두른 칼에 찔려 사망하였습니다.")
                        print("당신은", day[0], "일 동안 생존했습니다.")
                        input("")
                        exit()
                    continue
                
            else:
                exit_chance = random.randint(1,5)
                if exit_chance == 1:
                    print("\n무사히 탈출했습니다.")
                    input("")
                    break

                elif exit_chance == 2 or exit_chance == 3:
                    player[0] = player[0] - Enemy[1]
                    if player[0] <= 0 and Incident <= 13:
                        player_status["감염"] = 1
                        print("\n좀비에게 감염당했습니다. 3일안에 치료제를 복용해야 합니다.")
                        player[0] = 5
                        input("")
                        break
                    elif player[0] <= 0 and 14 <=Incident <= 15:
                        print("도적이 휘두른 칼에 찔려 사망하였습니다.")
                        print("당신은", day[0], "일 동안 생존했습니다.")
                        exit()
                        
                    print("\n적에게", Enemy[1], "의 데미지를 입었습니다. \n")
                    print("조금 상처를 입고 탈출했습니다.")
                    input("")
                    break
                    
                else:
                    print("\n도망치는데 실패했습니다.")
                    print("\n적에게", Enemy[1] * 2, "의 데미지를 입었습니다. \n")
                    player[0] = player[0] - Enemy[1] * 2
                    if player[0] <= 0 and Incident <= 13:
                        player_status["감염"] = 1
                        print("\n좀비에게 감염당했습니다. 3일안에 치료제를 복용해야 합니다.")
                        player[0] = 5
                        input("")
                        break
                    elif player[0] <= 0 and 14 <=Incident <= 15:
                        print("도적이 휘두른 칼에 찔려 사망하였습니다.")
                        print("당신은", day[0], "일 동안 생존했습니다.")
                        input("")
                        exit()
                    print("----------------------------------------")
                    continue
        print("----------------------------------------")

def fight_event(n):
    if n >= 1 and n <= 7:
        nomal_zombie()
    elif n == 8 or n == 9:
        doctor_zombie()
    elif n == 10 or n == 11:
        soldier_zombie()
    elif n == 12 or n == 13:
        police_zombie()
    elif n == 14 or n == 15:
        thief()

#이벤트 함수
def event(n):
    if (16 <= n <= 35):
        item_event(n)
    elif (36 <= n <= 40):
        rest_event(n)
        day[0] += 1
        print("======== day.", day[0], "========" )
        rest_event2()
    elif (41 <= n <= 46):
        colleague(n)
    elif (47 <= n <= 51):
        nomal_story(n)
    elif (52 <= n <= 56):
        condition(n)
    elif (57 <= n <= 61):
        choice(n)

#아이템 이벤트 함수
def gain_item(name):
    if name in player_inventory:
        print(name, "은 1개만 보유 할 수 있습니다!")
        input("")
    else:
        player_inventory.append(name)
        print(name, "을(를) 얻었습니다!")
        input("")

def item_event(n):
    if n == 16:
        print("당신은 길을 걷다 대형마트에 도착했습니다. \n")
        print("좀비를 피해 조용히 매장안으로 들어갑니다. \n")
        print("일단 들어오긴 했지만 한 곳만 들려 빠르게 나가야 할 것 같습니다. \n")
        while True:
            select = input("1. 식품코너로 간다 2. 공구코너로 간다 : ")
            print("----------------------------------------")
            if select == "1" or select == "2":
                break
        if select == "1":
            gain_item("인스턴트 식품")
            gain_item("물")

        elif select == "2":
            gain_item("자가발전 손전등")
            
    elif n == 17:
        print("당신은 길을 걷다 한 연구시설에 도착했습니다. \n")
        print("다 부서져가는 간판엔 항좀비바이러스 연구소라고 적혀있습니다. \n")
        print("당신은 이 연구소를 과거에 뉴스에서 본적이 있습니다. \n")
        print("분명 좀비바이러스 치료제를 개발하던 연구소 였을 거에요! \n")
        print("당신은 제 2연구실이라는 곳에 들어가 좀비바이러스치료제를 챙겼습니다. \n")
        print("이걸로 좀비에 감염되어도 한번정도는 치료할수 있겠군요! \n")
        gain_item("좀비바이러스 치료제")
        

    elif n == 18:
        print("당신은 길을 걷다 한 약국에 도착했습니다. \n")
        print("좀비바이러스가 발발하고 많은 사람들이 약국에 몰려 대부분의 약품이 없지만 \n")
        print("당신은 혹시라도 하는 마음에 이곳저곳 찾아봅니다. \n")
        print("열심히 찾아보다 구석에서 타이레놀을 찾았습니다! \n")
        print("만약 상태이상이 걸리면 타이레놀으로 치료 할 수 있습니다. \n")
        gain_item("타이레놀")

    elif n == 19:
        print("당신은 좀비바이러스로 인해 폐역이 되버린 지하철역으로 들어갑니다. \n")
        print("좀비바이러스로 발전소가 멈춰 전기가 들어오지 않아 앞이 보이지 않습니다. \n")
        print("손전등이라도 있었으면 좋았을텐데요... \n")
        while True:
            select = input("1. 안보이지만 감각을 믿고 탐색한다 2. 손전등을 사용한다. 3. 그냥 돌아간다 : ")
            print("----------------------------------------")
            if select == "1" or select == "2" or select == "3":
                break
        if select == "1":
            case = random.randint(1,5)
            if case <= 4:
                print("\n당신은 앞에 있는 좀비를 못 보고 그만 넘어집니다. \n")
                print("당신은 좀비에게 감염당했습니다. \n")
                print("3일내에 치료제를 복용하지 못하면 좀비가 됩니다.")
                player_status["감염"] = 1
                input("")
            elif case == 5:
                print("\n당신은 초인적인 감각을 발휘해 방독면을 찾았습니다! \n")
                gain_item("방독면")
                        
        elif select == "2":
            if "자가발전 손전등" in player_inventory:
                print("\n당신은 방독면을 찾았습니다! \n")
                gain_item("방독면")
            else:
                print("\n손전등을 보유하고 있지 않습니다. \n")
                print("----------------------------------------")
                item_event(19)

        elif select == "3":
            print("\n당신은 어두운 지하철 역을 빠져나왔습니다.")
            input("")
        
            

    elif n == 20:
        print("당신은 철물점 앞에 도착합니다. \n")
        print("철물점에는 다양한 도구가 있습니다. \n")
        while True:
            select = input("1. 전동공구를 찾는다 2. 수공구를 찾는다 : ")
            print("----------------------------------------")
            if select == "1" or select == "2":
                break
        if select == "1":
            gain_item("전기톱")
        elif select == "2":
            gain_item("마체테")
            
    elif n == 21:
        print("당신은 폐교가 된 모교 앞에 도착했습니다. \n")
        print("학교에는 좀비가 된 학생이 많아 위험합니다. \n")
        while True:
            select = input("1. 들어간다 2.돌아간다 : ")
            print("----------------------------------------")
            if select == "1" or select == "2":
                break
        if select == "1":
            case = random.randint(1,5)
            if case <= 3:
                print("\n당신은 좀비가 된 학생들을 피해 한 교실로 들어갔습니다 \n")
                print("하지만 그 교실은 이미 좀비가 된 학생들로 가득찼습니다. \n")
                print("당신은 좀비에게 감염당했습니다. \n")
                print("3일내에 치료제를 복용하지 못하면 좀비가 됩니다.")
                player_status["감염"] = 1
                input("")
            elif 4 <= case <= 5:
                print("\n당신은 좀비가 된 학생들을 피해 교무실로 들어갑니다. \n")
                print("당신은 학창시절에 자주 보았던 담임선생님의 단소를 찾았습니다. \n")
                print("당신은 잠깐 추억에 잠긴 후 학교를 빠져 나옵니다. \n")
                gain_item("담임선생님의 단소")

        else:
            print("당신은 모교를 뒤로하고 돌아섭니다.")
            input("")                

    elif n == 22:
        print("당신은 주유소 앞에 도착합니다. \n")
        print("주유소도 습격을 당해 주유탱크에서 기름이 새고 있습니다. \n")
        print("기름 냄새가 심해 당신은 어지럼증을 호소합니다. \n")
        while True:
            select = input("1. 어지럽지만 계속 들어가본다 2. 방독면을 쓴다 3. 돌아간다 : ")
            print("----------------------------------------")
            if select == "1" or select == "2" or select == "3":
                break
        if select == "1":
            case = random.randint(1,5)
            if case <= 4:
                print("\n당신은 심한 어지럼증을 호소하며 앞에 있는 좀비를 못 보고 그만 물렸습니다. \n")
                print("당신은 좀비에게 감염당했습니다. \n")
                print("3일내에 치료제를 복용하지 못하면 좀비가 됩니다. \n")
                player_status["감염"] = 1
                input("")
            elif case == 5:
                print("\n당신은 어지럼증을 참으며 기름통을 찾고 나옵니다. \n")
                gain_item("기름통")

        elif select == "2":
            if "방독면" in player_inventory:
                print("\n 당신은 기름통을 찾았습니다! \n")
                gain_item("기름통")
            else:
                print("\n 방독면을 보유하고 있지 않습니다. \n")
                item_event(19)

        elif select == "3":
            print("\n 당신은 어지럼증을 호소하며 주유소를 빠져나왔습니다.")
            input("")        

    elif n == 23:
        print("당신은 길을 걷다 부동산 앞에 도착합니다. \n")
        print("부동산이라면 이 지역의 지도를 가지고 있을겁니다. \n")
        print("그렇게 당신은 부동산으로 들어갑니다. \n")
        print("당신은 한쪽벽에 붙어있는 지도를 때서 나옵니다. \n")
        gain_item("지도")

    elif n == 24:
        print("당신은 옷가게를 찾아 들어갑니다. \n")
        print("여기서라면 좀비가 물어도 괜찮을 만한 옷이 있을겁니다. \n")
        case = random.randint(1,5)
        if case == 1:
            print("당신은 좀비에게 쫒기다 아무것도 얻지 못하고 나왔습니다.")
            input("")
        elif case == 2:
            print("당신은 패딩매장에서 롱패딩을 챙겨서 나왔습니다. \n")
            gain_item("롱패딩")
        elif case == 3:
            print("당신은 가죽재킷 매장에서 가죽재킷을 챙겨서 나왔습니다. \n")
            gain_item("가죽재킷")
        elif case == 4:
            print("당신은 코트매장에서 코트를 챙겨서 나왔습니다. \n")
            gain_item("코트")
        elif case == 5:
            print("당신은 스포츠 매장에서 트레이닝복을 챙겨서 나왔습니다. \n")
            gain_item("트레이닝복")

    elif n == 25:
        print("당신은 인스턴트 식품을 생산하던 폐공장으로 들어갑니다. \n")
        print("좀비바이러스로 발전소가 멈춰 전기가 들어오지 않아 앞이 보이지 않습니다. \n")
        print("손전등이라도 있었으면 좋았을텐데요... \n")
        while True:
            select = input("1. 안보이지만 감각을 믿고 탐색한다 2. 손전등을 사용한다. 3. 그냥 돌아간다 : ")
            print("----------------------------------------")
            if select == "1" or select == "2" or select == "3":
                break
        if select == "1":
            case = random.randint(1,5)
            if case <= 4:
                print("\n당신은 앞에 있는 좀비를 못 보고 그만 넘어집니다. \n")
                print("당신은 좀비에게 감염당했습니다. \n")
                print("3일내에 치료제를 복용하지 못하면 좀비가 됩니다.")
                player_status["감염"] = 1
                input("")
            elif case == 5:
                print("\n당신은 초인적인 감각을 발휘해 라디오를 찾았습니다! \n")
                print("언젠간 구해주러 온다는 소식이 들렸으면 좋겠네요.. \n")
                gain_item("라디오")
                        
        elif select == "2":
            if "자가발전 손전등" in player_inventory:
                print("\n 당신은 라디오을 찾았습니다! \n")
                print("언젠간 구해주러 온다는 소식이 들렸으면 좋겠네요... \n")
                gain_item("라디오")
            else:
                print("\n 손전등을 보유하고 있지 않습니다. \n")
                item_event(25)

        elif select == "3":
            print("\n 당신은 어두운 폐공장을 빠져나왔습니다.")
            input("")

    elif n == 26 :
        print("당신은 길을 걷다 편의점을 발견합니다. \n")
        print("도움이 될 만한 물품이 있을까 편의점에 들어갑니다. \n")
        while True:
            select = input("1. 의료코너로 간다. 2. 식품코너로 간다 : ")
            print("----------------------------------------")
            if select == "1" or select == "2":
                break
        if select == "1" :
            gain_item("붕대")
        elif select == "2" :
            gain_item("인스턴트 식품")

    elif n == 27 :
        print("당신은 아무도 없어 보이는 호텔에 들어갑니다. \n")
        print("아마 쓸만한 물건이 있을겁니다. \n")
        print("다행히 전기가 남아있어 호텔을 둘러볼 수 있습니다. \n")
        case = random.randint(1, 3)
        if case == 1 :
            print("빈 집에 아무것도 없어서 그냥 호텔 밖으로 나왔습니다.")
            input("")
        elif case == 2 :
            print("호텔을 둘러보니 라디오가 있어 가지고 나왔습니다. \n")
            gain_item("라디오")
        elif case == 3 :
            print("식량 창고에 먹을 것이 있어 챙겨 나왔습니다. \n")
            gain_item("물")
            gain_item("인스턴트 식품")

    elif n == 28 :
        print("당신은 지나가다 병원이 보여 들어갑니다. \n")
        print("치료에 도움이 될만한 물건이 있을겁니다. \n")
        case = random.randint(1, 2)
        if case == 1 :
            print("누가 다 가져갔는지 아무것도 없어 그냥 밖으로 나왔습니다.")
            input("")
        elif case == 2 :
            print("병원을 둘러보니 구급상자가 보여 가지고 나왔습니다. \n")
            gain_item("구급상자")

    elif n == 29 :
        print("당신은 지나가다 노래방을 발견해 들어갑니다. \n")
        print("아마 자판기에서 물을 발견할 수 있을겁니다. \n")
        print("자판기에서 물을 발견하여 가지고 나왔습니다. \n")
        gain_item("물")

    elif n == 30 :
        print("당신은 지나가다 피씨방을 발견해 들어갑니다. \n")
        print("아마 남은 식량이 있을겁니다. \n")
        print("인스턴트 식품과 물을 발견해 가지고 나왔습니다. \n")
        gain_item("물")
        gain_item("인스턴트 식품")

    elif n == 31 :
        print("당신은 지나가다 술집을 발견해 들어갑니다. \n")
        print("술은 상처 회복이나 화염병을 만드는데 도움이 될겁니다. \n")
        print("둘러보니 술이 있어 가지고 나왔습니다. \n")
        gain_item("술")

    elif n == 32 :
        print("당신은 지나가다 문구점을 발견했습니다. \n")
        print("생존에 필요한 물건이 있을겁니다. \n")
        case = random.randint(1, 3)
        if case == 1 :
            print("쓸만한 물건을 찾지 못해 그냥 나왔습니다.")
            input("")
        elif case == 2 :
            print("생존에 도움이 될 만한 마체테를 발견해 들고 나왔습니다. \n")
            gain_item("마체테")
        elif case == 3 :
            print("생존에 도움이 될 만한 건전지를 발견해 들고 나왔습니다. \n")
            gain_item("건전지")

    elif n == 33 :
        print("당신은 지나가다 지하실을 발견해 들어갑니다. \n")
        print("찾아보면 쓸만 한 물건이 있을겁니다. \n")
        case = random.randint(1, 2)
        if case == 1 :
            print("당신은 좀비에게 쫓기다 다행히 도망나왔습니다.")
            input("")
        elif case == 2 :
            print("지하실을 둘러보니 운 좋게 좀비바이러스 치료제를 발견했습니다. \n")
            gain_item("좀비바이러스 치료제")

    elif n == 34 :
        print("당신은 지나가다 교회를 발견해 들어갑니다. \n")
        print("생존에 도움이 될 만한 물건이 있을겁니다. \n")
        case = random.randint(1, 2)
        if case == 1 :
            print("당신은 식량을 발견해 챙겨 나왔습니다. \n")
            gain_item("인스턴트 식품")
            gain_item("물")
        elif case == 2 :
            print("당신은 생존에 도움이 될 만한 성냥을 발견해 가지고 나왔습니다. \n")
            gain_item("성냥")

    elif n == 35 :
        print("당신은 상명대학교를 발견해 신나는 마음으로 들어갑니다. \n")
        print("상명대학교라면 좋은 물건이 있을겁니다. \n")
        print("당신은 좋은 방어구인 상명대학교 과잠을 발견했습니다. \n")
        gain_item("상명대학교 과잠")

#휴식이벤트
def rest_event(n):
    if n == 36:
        print("당신은 하루종일 잠을 못잤습니다. \n")
        print("피로감에 몸은 마음처럼 움직이지 않아 쉴 곳을 찾습니다. \n")
        print("전방에 빈 건물이 보여 휴식을 취합니다.")
        player[0] += 10
        input("")
    elif n == 37:
        print("당신은 활동을 하려고 밖을 살폈습니다. \n")
        print("하지만 좀비들이 너무 많아 나가기 힘들어 보입니다. \n")
        print("어쩔 수 없이  당신은 하루 더 주변을 살피며 숨어있기로 합니다.")
        player[0] += 10
        input("")
    elif n == 38:
        print("잦은 전투로 당신은 만신창이가 됐습니다. \n")
        print("체력적으로 힘들고, 피로도 많아졌습니다. \n")
        print("그래서 체력과 피로를 위해 하루만 재정비 시간을 갖기로 했습니다.")
        player[0] += 10
        input("")
    elif n == 39:
        print("당신은 갑자기 몸이 이상함을 느낍니다. \n")
        print("방금 먹었던 물이 생각이 납니다. \n")
        print("조금 씁쓸하다 했더니 술이였다는 것을 깨닫습니다. \n")
        print("술에 취했으니 어쩔 수 없이 하루 쉬기로 합니다.")
        player[0] += 10
        input("")
    elif n == 40:
        print("당신은 갑자기 머리가 아파옵니다. \n")
        print("코로나에 대한 증상은 거의 없지만 혹시 모른다는 생각을 합니다. \n")
        print("그래서 빈 건물에서 하루 동안 자가격리를 하기로 합니다.")
        player[0] += 10
        input("")
        
def rest_event2():
    print("당신은 눈을 떴습니다. \n")
    print("시간을 보니 하루가 지나있었고, 시간가는 줄 모르고 휴식을 취했다는 것을 알게되었습니다. \n")
    print("이러한 휴식 덕분에 당신은 HP를 10 회복하였습니다.")
    input("")
    
#동료모집 이벤트
def colleague(n):
    if n == 41:
        colleague_soldier()
    elif n == 42:
        colleague_doctor()
    elif n == 43:
        colleague_hunter()
    elif n == 44:
        colleague_salesman()
    elif n == 45:
        colleague_gambler()
    elif n == 46:
        colleague_explorer()

def colleague_soldier():
    print("당신은 전투에 지친 군인을 발견하게 됩니다. \n")
    print("군인은 혼자 살아남기 힘들다고 같이 가게 해달라고 합니다. \n")
    print("당신은 군인이 좋은 전력이 될 거라는 생각과 믿을 수 있는 사람인지에 대한 고민에 빠집니다. \n")
    while True:
        question = input("같이 가시겠습니까? 같이 가시려면 1을, 아니면 2를 입력하세요: ")
        print("----------------------------------------")
        if question == "1" or question == "2":
            break
    if question == "1":
        print("\n당신은 동료로 받아들이기로 결심했습니다.")
        input("")
        print("당신의 팀이 더 강해졌습니다. \n")
        print("당신의 체력 10 증가, 공격력 3 증가")
        player[0] += 10
        player[1] += 3
        input("")
    elif question == "2":
        print("\n당신은 그냥 혼자가겠다고 결심했습니다.")
        input("")

def colleague_doctor():
    print("당신은 수상한 인기척을 느꼈습니다. \n")
    print("당신은 그쪽으로 조심히 향했고, 쓰러져 있는 사람을 발견했습니다. \n")
    print("당신은 일단 그 사람이 깨어날 때까지 보살펴주었습니다. \n")
    print("그 사람은 당신에게 고마움을 표현했습니다. \n")
    print("또한, 그 사람은 자신이 의사여서 치료제와 타이레놀이 있어 같이 가자고 합니다. \n")
    print("당신은 믿을 만한 사람인지 의심이 들어 고민을 합니다. \n")
    while True:
        question = input("같이 가시겠습니까? 같이 가시려면 1을, 아니면 2를 입력하세요: ")
        print("----------------------------------------")
        if question == "1" or question == "2":
            break
    if question == "1":
        print("당신은 동료로 받아들이기로 결심했습니다. \n")
        gain_item("좀비바이러스 치료제")
        gain_item("타이레놀")
        print("좀비바이러스 치료제, 타이레놀을 각각 하나씩 획득했습니다.")
        input("")
    elif question == "2":
        print("당신은 그냥 혼자가겠다고 결심했습니다.")
        input("")
        
def colleague_hunter():
    print("당신은 길을 가다 갑자기 덫에 걸렸습니다. \n")
    print("곧 덫을 친 사람이 다가왔습니다. \n")
    print("그 사람은 잠을 잘 때 공격을 받지 않기 위해 함정을 설치했다고 합니다. \n")
    print("당신은 짜증이 났지만 일단 풀어달라고 하고, 그 사람은 풀어줬습니다. \n")
    print("그 사람은 자신은 사냥꾼이어서 좀비와의 싸움에서 유리할 거라고 하며 같이 다니자고 합니다. \n")
    print("당신은 이 정도 함정을 팔 사람이면 도움이 되겠다 생각해 그 사람과 같이 다니기로 합니다. \n")
    player[0] += 10
    player[1] += 2
    print("당신의 팀이 더 강해졌습니다. \n")
    print("당신의 체력 10 증가, 공격력 2 증가")
    input("")

def colleague_salesman():
    print("당신은 또 다른 생존자가 있나 수색을 합니다. \n")
    print("그러다 숨어있는 한 사람을 발견했습니다. \n")
    print("그 사람에게 자초지종을 설명을 들었습니다. \n")
    print("그 사람은 자신은 영업사원이었으며 집에 와보니 가족들이 다 죽어있었다고 합니다. \n")
    print("그래서 좀비를 피해 숨어있었다고 합니다. \n")
    print("당신은 그 사람을 안타깝게 생각해 같이 다니자고 합니다. \n")
    print("당신의 팀이 더욱 강력해졌습니다. \n")
    player[0] += 10
    player[1] += 5
    print("당신의 체력 10 증가, 공격력 5 증가")
    input("")
        
def colleague_gambler():
    print("당신은 길을 잃어버렸습니다. \n")
    print("거기서 한 사람을 발견하게 됩니다. \n")
    if "좀비바이러스 치료제" not in player_inventory:
        print("그 사람은 자신은 도박사이며 도박을 하나 하자 합니다. \n")
        print("치료제를 걸고 동전 던지기 도박을 하자 합니다. \n")
        while True:
            question = input("동의 하시면 1, 아니면 2를 입력하세요: ")
            print("----------------------------------------")
            if question == "1" or question == "2":
                break
        if question == "1":
            print("앞(1)이 나오면 당신 승리 뒤(2)가 나오면 도박사의 승리입니다.")
            input("")
            coin = random.randint(1,2)
            print(coin)
            if coin == 1:
                gain_item("좀비바이러스 치료제")
                print("당신은 승리하여 좀비바이러스 치료제 하나를 얻고 갈길을 갑니다.")
                input("")
            elif coin == 2:
                player[0] -= 10
                print("당신은 패배하여 HP를 10잃습니다.")
                print("")
        elif question == "2":
            print("당신은 거절을 하고 갈길을 갑니다.")
            input("")
            
    elif "타이레놀" not in player_inventory:
        print("그 사람은 자신은 도박사이며 도박을 하나 하자 합니다. \n")
        print("타이레놀을 걸고 동전 던지기 도박을 하자 합니다. \n")
        while True:
            question = input("동의 하시면 1, 아니면 2를 입력하세요: ")
            if question == "1" or question == "2":
                break
        if question == "1":
            print("앞(1)이 나오면 당신 승리 뒤(2)가 나오면 도박사의 승리입니다.")
            input("")
            coin = random.randint(1,2)
            print(coin)
            if coin == 1:
                gain_item("타이레놀")
                print("당신은 승리하여 타이레놀 하나를 얻고 갈길을 갑니다.")
                input("")
            elif coin == 2:
                player[0] -= 10
                print("당신은 패배하여 HP를 10잃습니다.")
                input("")
                
        elif question == "2":
            print("당신은 거절을 하고 갈길을 갑니다.")
            input("")
    else:
        print("그 사람은 볼 일 없으면 그냥 가라고합니다. \n")
        print("그래서 당신은 그냥 갈길을 갑니다.")
        input("")
        
def colleague_explorer():
    print("당신은 수상한 불이 보여 다가갑니다. \n")
    print("거기서 한 사람이 자고 있었습니다. \n")
    print("당신은 우선 경계를 했고, 그 사람을 깨웠습니다. \n")
    print("그 사람 역시 수상한 사람에게 경계를 했고, 두 사람은 대화를 시도합니다. \n")
    print("대화를 통해 두 사람은 좀비가 아닌 사람이란 걸 알게되었습니다. \n")
    print("그 사람은 자신이 탐험가이며 같이 다니자고 합니다. \n")
    print("당신은 고민에 빠졌습니다. \n")
    while True:
            question = input("같이 가시겠습니까? 같이 가시려면 1을, 아니면 2를 입력하세요: ")
            print("----------------------------------------")
            if question == "1" or question == "2":
                break
    if question == "1":
        player[0] += 10
        player[1] += 4
        print("당신은 동료로 받아들이기로 결심했습니다. \n")
        print("당신의 팀이 더 강해졌습니다. \n")
        print("당신의 체력이 10 증가, 공격력이 4 증가")
        input("")
    elif question == "2":
        print("당신은 그냥 혼자가겠다고 결심했습니다.")
        input("")

#일반스토리
def nomal_story(n):
    if n == 47:
        print("당신은 길을 걷다 대피소에 도착했습니다.\n")
        print("또 다른 생존자가 있다는 희망에 기쁘고 혼자가 아니라는 생각에 안도가 됩니다!\n")
        print("생존자들이 조금 이상하네요..! 좀비처럼 행동합니다..!\n")
        print("아.. 이 대피소 좀비에게 점령당한 것 같습니다.. \n")
        print("좀비들 모르게 도망갑니다.")
        input("")
    elif n ==48:
        print("당신은 길을 걷다 햄버거 가게에 도착했습니다.\n")
        print("햄버거 가게이니 배를 채울 수 있는 음식이 있을거에요!\n")
        print("기쁜 마음으로 가게 안으로 들어갑니다.\n")
        print("아.. 이미 누군가가 털어 갔습니다. \n")
        print("조용..! 무슨 소리가 들리지 않나요? 아.. 좀비가 있습니다.\n")
        print("좀비들 모르게 도망갑니다.")
        input("")
    elif n == 49:
        print("당신은 길을 걷다 가전제품 판매점에 도착했습니다. \n")
        print("재난 상황에는 라디오가 필요하니 찾아봅니다.\n")
        print("라디오가 없군요.. 건전지도 필요할 수 있으니 찾아봅니다.\n")
        print("건전지도 없군요.. 조용..! 저기 누구가 있는거 같아요! \n")
        print("좀비인거 같아요.. 좀비들 모르게 도망갑니다.")
        input("")
    elif n == 50:
        print("당신은 길을 걷다 미용실에 도착했습니다.\n")
        print("머리를 못 감은지가 오래됬군요..!\n")
        print("오랜만에 시원하게 머리를 감습니다. \n")
        print("평소 가지고 싶었던 미용 가위를 발견했습니다!\n")
        print("하지만 지금은 불필요한 물건이니 그대로 놓고 갑니다.")
        input("")
    elif n == 51:
        print("어? 저기 생존자 아닌가요? 생존자가 보입니다!\n")
        print("하지만 좀비일 수 있다는 생각을 항상 합니다..!\n")
        print("또 다른 생존자가 있나요..? 근데 생존자 행동이 조금 이상합니다..\n")
        print("좀비에 감염당한 것 같습니다..! 당신을 발견하고 여기로 오고 있는거 같습니다. \n")
        print("당신은 빠르게 도망칩니다.")
        input("")

#상태이상 이벤트
def condition(n):
    if n == 52:
        print("날씨가 추워졌습니다. 빨리 롱패딩을 입어야겠어요!\n")
        print("롱패딩을 입지 않으면 체력이 10이 줄어듭니다.")
        print("----------------------------------------")
        input("")
        if "롱패딩" in player_inventory:
            print("다행히 롱패딩이 있어 추위를 막기 위해서 옷을 입습니다.")
            input("")
        else:
            player[0]=player[0] - 10
            print("롱패딩을 가지고 있지 않습니다.\n")
            print("체력이 10 줄어",player[0],"의 체력이 남았습니다.")
            input("")
            
    elif n == 53:
        print("며칠째 아무것도 먹지 못했습니다..\n")
        print("지금 어느것이든 먹어야 하겠어요.\n")
        print("지금 먹지 않으면 힘이 없어 공격력이 5 줄어듭니다.")
        print("----------------------------------------")
        input("")
        if "인스턴트 식품" in player_inventory:
            print("다행히 대형마트에서 얻은 인스턴트 식품이 있어 배를 채웁니다.")
            player_inventory.remove("인스턴트 식품")
            input("")
        else:
            player[1] = player[1] - 5
            print("인스턴트 식품을 가지고 있지 않습니다.\n")
            print("공격력이 5 줄어",player[1],"의 공격력이 됐습니다.")
            input("")

    elif n == 54:
        print("좀비를 피해 다니느라 잠을 자지 못해 머리가 아픈거 같군요.. \n")
        print("지금 타이레놀을 먹지 못하면 힘이 부족해 공격력이 5 줄어듭니다.")
        print("----------------------------------------")
        input("")
        if "타이레놀" in player_inventory:
            player_inventory.remove("타이레놀")
            print("다행히 약국에서 얻은 타이레놀이 있어 복용합니다.")
            input("")
        else:
            player[1] = player[1]- 5
            print("타이레놀을 가지고 있지 않습니다.\n")
            print("공격력이 5 줄어",player[1],"의 공격력이 됐습니다.")
            input("")
        
    elif n == 55:
        print("길을 걷다 처음 와본 장소에 도착했습니다.\n")
        print("주변에 좀비들이 많습니다.\n")
        print("지도를 가지고 지리를 파악해서 도망가야 하겠어요.\n")
        print("지도가 없으면 좀비들과 맞서 싸워야 합니다. \n")
        print("하지만 좀비와 싸우는 상황을 대비하지 못하여 좀비에게 공격을 당해 체력이 10 줄어듭니다.")
        print("----------------------------------------")
        input("")
        if "지도" in player_inventory:
            player_inventory.remove("지도")
            print("다행히 지도가 있어 좀비를 피해 도망갑니다.\n")
            input("")
        else:
            player[0]=player[0] - 10
            print("지도를 가지고 있지 않습니다.\n")
            print("좀비에게 공격당해 체력이 10 줄어",player[0],"의 체력이 남았습니다.")
            input("")
        
    elif n == 56:
        print("좀비들을 피해 도망치느라 땀이 많이 났군요.\n")
        print("몸에서 수분이 많이 빠진거 같습니다.\n")
        print("지금 물을 마셔야 할 거 같아요.\n")
        print("물을 마시지 않으면 체력이 10 줄어듭니다.\n")
        print("물을 마시면 수분이 보충되어 체력이 10 올라갑니다.")
        print("----------------------------------------")
        input("")
        if "물" in player_inventory:
            player_inventory.remove("물")
            player[0] = player[0] + 10
            print("다행히 대형마트에서 얻은 물이 있어 수분을 보충합니다.\n")
            print("물을 마셔서 체력이",player[0],"로 올라갔습니다.")
            input("")
        else:
            player[0] = player[0] - 10
            print("물을 가지고 있지 않습니다.\n")
            print("물을 마시지 못해  체력이",player[0],"로 줄었습니다.")
            input("")

#함정이벤트 함수
def choice(n):
    if n == 57:
        print("길을 걷다 운이 좋게 인스터트 식품과 물을 발견했습니다. \n")
        print("인스턴트 식품과 물을 가지러 갈까요?\n")
        while True:
            select = input("1. 가지러 간다. 2. 함정일 수 있으니 그냥 지나간다 : ")
            print("----------------------------------------")
            if select == "1":
                if player_status["직업"] == "탐험가":
                    print("당신은 탐험가 였던 실력을 발휘하여 함정을 피하고 아이템을 얻었습니다! \n")
                    gain_item("인스턴트 식품")
                    gain_item("물")
                    break
                player[0] = player[0] - 30
                print("다른 생존자가 설치한 함정이었습니다.\n")
                print("다른 생존자에게 공격을 받아 체력이", player[0],"가 되었습니다.")
                if player[0] <= 0:
                    print("----------------------------------------")
                    print("다른 생존자가 설치한 함정에 그만 사망하고 말았습니다.")
                    print("당신은", day[0], "일 동안 생존했습니다.")
                    input("")
                    exit()
                input("")
                break
            elif select == "2":
                print("함정일 수 있으니 그냥 지나갑니다.")
                input("")
                break

    elif n == 58:
        print("길을 걷다 운이 좋게 라디오를 발견했습니다. \n")
        print("라디오를 가지러 갈까요?\n")
        while True:
            select = input("1. 가지러 간다. 2. 함정일 수 있으니 그냥 지나간다 : ")
            print("----------------------------------------")

            if select == "1":
                if player_status["직업"] == "탐험가":
                    print("당신은 탐험가 였던 실력을 발휘하여 함정을 피하고 아이템을 얻었습니다! \n")
                    gain_item("라디오")
                    break
                player[0] = player[0] - 30
                print("다른 생존자가 설치한 함정이었습니다.\n")
                print("다른 생존자에게 공격을 받아 체력이", player[0],"가 되었습니다.")
                if player[0] <= 0:
                    print("----------------------------------------")
                    print("다른 생존자가 설치한 함정에 그만 사망하고 말았습니다. \n")
                    print("당신은", day[0], "일 동안 생존했습니다.")
                    input("")
                    exit()
                input("")
                break
            elif select == "2":
                print("함정일 수 있으니 그냥 지나갑니다.")
                input("")
                break

    elif n == 59:
        print("길을 걷다 어느 아이템이 있을 것 같은 상자를 발견했습니다. \n")
        print("상자를 열어 볼까요?\n")
        while True:
            select = input("1. 열어본다. 2. 함정일 수 있으니 그냥 지나간다 : ")
            print("----------------------------------------")
            if select == "1":
                if player_status["직업"] == "탐험가":
                    print("당신은 탐험가 였던 실력을 발휘하여 함정을 피하고 골드를 얻었습니다! \n")
                    gain_gold = random.randint(30, 60)
                    print(gain_gold, "골드를 얻었습니다.")
                    gold["골드"] = gold["골드"] + gain_gold
                    input("")
                    break
                player[0] = player[0] - 30
                print("다른 생존자가 설치한 함정이었습니다.\n")
                print("다른 생존자에게 공격을 받아 체력이", player[0],"가 되었습니다.")
                if player[0] <= 0:
                    print("----------------------------------------")
                    print("다른 생존자가 설치한 함정에 그만 사망하고 말았습니다. \n")
                    print("당신은", day[0], "일 동안 생존했습니다.")
                    input("")
                    exit()
                input("")
                break
            elif select == "2":
                print("함정일 수 있으니 그냥 지나갑니다.")
                input("")
                break

    elif n == 60:
        print("길을 걷다 강물을 발견하였습니다.\n")
        print("목이 마르니 강물을 마실까요?\n")
        while True:
            select = input("1. 마신다. 2.그냥 지나간다 : ")
            print("----------------------------------------")

            if select == "1":
                if player_status["직업"] == "탐험가":
                    print("당신은 탐험가 였던 실력을 발휘하여 수질이 좋지 못한걸 깨닫고 돌아섭니다.")
                    input("")
                    break
                print("좀비들로 인하여 수질이 좋지 않았군요..! 배탈이 난 것 같습니다.\n")
                print("지금 당장 타이레놀을 복용해야 하겠어요..!\n")
                print("타이레놀을 복용하지 않으면 데미지를 입게 됩니다.")
                input("")
                if "타이레놀" in player_inventory:
                    player_inventory.remove("타이레놀")
                    print("타이레놀이 있어 버틸 수 있을 것 같아요!")
                    input("")
                    break
                else:
                    player[0] = player[0] - 30
                    print("배탈이 나서 체력이", player[0],"가 되었습니다.")
                    if player[0] <= 0:
                        print("----------------------------------------")
                        print("당신은 배탈이 악화되어 그만 사망하고 말았습니다. \n")
                        print("당신은", day[0], "일 동안 생존했습니다.")
                        input("")
                        exit()
                    input("")
                    break
            elif select == "2":
                print("함정일 수 있으니 그냥 지나갑니다.")
                input("")
                break


    elif n == 61:
        print("길을 걷다 운이 좋게 타이레놀을 발견했습니다. \n")
        print("타이레놀을 가지러 갈까요?\n")
        while True:
            select = input("1. 가지러 간다. 2. 함정일 수 있으니 그냥 지나간다 : ")
            print("----------------------------------------")

            if select == "1":
                if player_status["직업"] == "탐험가":
                    print("당신은 탐험가 였던 실력을 발휘하여 함정을 피하고 아이템을 얻었습니다! \n")
                    gain_item("타이레놀")
                    break
                player[0] = player[0] - 30
                print("다른 생존자가 설치한 함정이었습니다.\n")
                print("다른 생존자에게 공격을 받아 체력이", player[0],"가 되었습니다.")
                if player[0] <= 0:
                    print("----------------------------------------")
                    print("다른 생존자가 설치한 함정에 그만 사망하고 말았습니다. \n")
                    print("당신은", day[0], "일 동안 생존했습니다.")
                    input("")
                    exit()
                input("")
                break
            elif select == "2":
                print("함정일 수 있으니 그냥 지나갑니다.")
                input("")
                break

#상점시스템
def store() :
    while True :
        print("\n상점 \n")
        print("----------------------------------------")
        print("현재 보유중인 아이템 : ", player_inventory)
        print("----------------------------------------")
        print("\n구입 가능한 상품")
        store_list ={"1. 인스턴트 식품" : 50, "2. 물" : 30, "3. 좀비바이러스 치료제" : 500, "4. 타이레놀" : 300, "5. 방독면" : 100, "6. 마체테" : 200, "7. 전기톱" : 300}
        if player_status["직업"] == "영업사원":
            store_list ={"1. 인스턴트 식품" : 30, "2. 물" : 18, "3. 좀비바이러스 치료제" : 300, "4. 타이레놀" : 240, "5. 방독면" : 60, "6. 마체테" : 120, "7. 전기톱" : 240}
        print(store_list)
        print("----------------------------------------")
        print("상점을 종료하고 싶으면 1~7을 제외한 아무 키나 입력해주세요.")
        menu = input("\n 무엇을 구매하시겠습니까? ")

        if menu == "1" :
            if "인스턴트 식품" not in player_inventory and gold["골드"] >= store_list["1. 인스턴트 식품"] :
                gold["골드"] = gold["골드"] - store_list["1. 인스턴트 식품"]
                print("인스턴트 식품을 구매하였습니다.")
                gain_item("인스턴트 식품")
            else :
                print("구매하지 못했습니다.(이미 소지하고 있거나 골드가 부족합니다!)")
        elif menu == "2" :
            if "물" not in player_inventory and gold["골드"] >= store_list["2. 물"] :
                gold["골드"] = gold["골드"] - store_list["2. 물"]
                print("물을 구매하였습니다.")
                gain_item("물")
            else :
                print("구매하지 못했습니다.(이미 소지하고 있거나 골드가 부족합니다!)")
        elif menu == "3" :
            if "좀비바이러스 치료제" not in player_inventory and gold["골드"] >= store_list["3. 좀비바이러스 치료제"] :
                gold["골드"] = gold["골드"] - store_list["3. 좀비바이러스 치료제"]
                print("좀비바이러스 치료제를 구매하였습니다.")
                gain_item("좀비바이러스 치료제")
            else :
                print("구매하지 못했습니다.(이미 소지하고 있거나 골드가 부족합니다!)")
        elif menu == "4" :
            if "타이레놀" not in player_inventory and gold["골드"] >= store_list["4. 타이레놀"] :
                gold["골드"] = gold["골드"] - store_list["4. 타이레놀"]
                print("타이레놀을 구매하였습니다.")
                gain_item("타이레놀")
            else :
                print("구매하지 못했습니다.(이미 소지하고 있거나 골드가 부족합니다!)")
        elif menu == "5" :
            if "방독면" not in player_inventory and gold["골드"] >= store_list["5. 방독면"] :
                gold["골드"] = gold["골드"] - store_list["5. 방독면"]
                print("방독면을 구매하였습니다.")
                gain_item("방독면")
            else :
                print("구매하지 못했습니다.(이미 소지하고 있거나 골드가 부족합니다!)")
        elif menu == "6" :
            if "마체테" not in player_inventory and gold["골드"] >= store_list["6. 마체테"] :
                gold["골드"] = gold["골드"] - store_list["6. 마체테"]
                print("마체테를 구매하였습니다.")
                gain_item("마체테")
            else :
                print("구매하지 못했습니다.(이미 소지하고 있거나 골드가 부족합니다!)")
        elif menu == "7" :
            if "전기톱" not in player_inventory and gold["골드"] >= store_list["7. 전기톱"] :
                gold["골드"] = gold["골드"] - store_list["7. 전기톱"]
                print("전기톱을 구매하였습니다.")
                gain_item("전기톱")
            else :
                print("구매하지 못했습니다.(이미 소지하고 있거나 골드가 부족합니다!)")
        else :
            print("상점을 종료합니다.")
            break
        print("남은 골드 : ", gold["골드"], "골드")

#장비시스템
def equipment() :
    print("\n장비 \n")
    while True:
        print("----------------------------------------")
        print("현재 보유중인 아이템 : ", player_inventory)
        print("현재 장착중인 아이템 : ", player_equipment)
        select = input("무엇을 장착하시겠습니까?(end입력시 종료) : ")
        print("----------------------------------------")
        if select in player_weapon:
            player[1] = player[1] - player_weapon[player_equipment["무기"]] + player_weapon[select]
            player_inventory.append(player_equipment["무기"])
            player_equipment["무기"] = select
            player_inventory.remove(select)
            print("플레이어의 공격력이", player[1],"이 되었습니다.")
        elif select in player_armor:
            player[0] = player[0] - player_armor[player_equipment["방어구"]] + player_armor[select]
            player_inventory.append(player_equipment["방어구"])
            player_equipment["방어구"] = select
            player_inventory.remove(select)
            print("플레이어의 체력이", player[0],"이 되었습니다.")
        elif select == "end":
            break
        else :
            print(select, "는(은) 장착 할 수 없는 아이템 입니다!")

#100일 생존 성공 엔딩함수
def ending():
    print("당신은 총 100일동안 밖에서 생존하며 물자를 모았습니다. \n")
    print("당신은 당신이 모은 보급품은", player_inventory, "입니다. \n")
    print("당신은 생존자집단으로 돌아가 보급품을 꺼내며 당신이 겪은 일들을 말합니다. \n")
    print("그때 한 사람이 생존자 집단쪽으로 다가왔고, 당신은 경계하기 시작했습니다. \n")
    print("그 사람은 좀비가 아니란 걸 필사적으로 말했고, 좀비를 피해 도망다니다 여기를 발견하게 됐다고 말했습니다. \n")
    print("그 사람이 좀비에 물리지 않았다는 것을 필사적으로 증명한 후 당신은 경계심을 풀었습니다. \n")
    print("생존자 집단에 인원이 늘어나자 보급품은 금세 다 쓰게 되어 다시 보급품을 구하러 가야했습니다. \n")
    print("당신은 보급품을 구하러 나갈사람이 있는지 물어보았고, 저번에 새로 온 사람이 자진해서 가겠다고 했습니다. \n")
    print("그렇게 당신은 새로 온 사람을 배웅해줍니다. \n")
    print("당신이 안전하게 보급품을 가져올수 있길...")
    print("======== end ========" )
    input("")
    print("\n제작 : 이민혁, 이승훈, 이창건, 임정택 \n")
    print("플레이해주셔서 감사합니다!")
    input("")
    exit()
    
#메인 진행부분
input("아무거나 입력해주세요(게임시작) : ")
print("----------------------------------------")
start_story1()
start_story2()
for i in range(0,100):
    print("======== day.", day[0], "========" )
    if "감염" in player_status:
        if day[0] > 100:
            print("당신은 좀비바이러스를 치료하지 못하여 좀비가 되었습니다.")
            input("")
            exit()
        if player_status["감염"] <= 3:
            if (day[0] % 20 == 0):
                print("다른 생존자 집단에 방문하였습니다. \n")
                print("상점과 장비 시스템을 이용할 수 있습니다.")
                while True:
                    day20 = input("1. 상점 2. 장비 시스템 : ")
                    if day20 == "1" or day20 == "2":
                        break
                if day20 == "1":
                    store()
                elif day20 == "2":
                    equipment()
                day[0] += 1
                continue
            else:
                Incident = random.randint(16, 61)
                event(Incident)
                    
            if "좀비바이러스 치료제" in player_inventory:
                print("----------------------------------------")
                print("좀비바이러스를 치료하였습니다!")
                del player_status["감염"]
                player[0] = 50
                print("----------------------------------------")
                input("")
                day[0] += 1
                continue
            
        else:
            print("좀비에 감염된 상처가 악화되어 좀비가 되고 말았습니다!")
            print("당신은", day[0], "일 동안 생존했습니다.")
            input("")
            exit()
            
        player_status["감염"] = player_status["감염"] + 1
        day[0] += 1
        continue
    
    if day[0] > 100:
        break

    if (day[0] % 20 == 0):
        print("다른 생존자 집단에 방문하였습니다. \n")
        print("상점과 장비 시스템을 이용할 수 있습니다.")
        while True:
            day20 = input("1. 상점 2. 장비 시스템 : ")
            if day20 == "1" or day20 == "2":
                break
        if day20 == "1":
            store()
        elif day20 == "2":
            equipment()
        day[0] += 1
        continue
        
    Incident = random.randint(1, 61)
    if (Incident >= 1 and Incident <= 15):
        fight_event(Incident)
    elif (Incident >= 16 and Incident <= 61):
        event(Incident)
    day[0] += 1

ending()
