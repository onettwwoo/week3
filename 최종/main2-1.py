import time
import random

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")

name = input("너의 이름은? ")
island = input("섬 이름은? (ㅇㅇ섬으로 입력됩니다.) ")

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}
script = ('어머 안녕~ 반가워~ 그렇지 뭐~', '안녀엉~ 반가워어~', '안녕하세유~ 반가워유~')

action_boolean = 1

# 4가지 반복하기
while action_boolean:
  print("\n어떤 것을 해볼까요? ")
  answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")

    # 0. 게임 종료
  if answer_action == "0":
    print("잘 가~")
    break

  # 1. 상점가기를 선택한경우
  elif answer_action == "1":
    print("상점에 온 걸 환영해구리!")
    time.sleep(1)
    print("\n현재 상점에는 이런 물건들이 있어구리")
    time.sleep(1)

    i = 1
    for key, value in store.items():
      print(int(i), ". ", str(key), ":", str(value), "벨")
      i += 1

    num = int(input("어떤 물건을 구입하겠어구리? (숫자로 입력) "))

    if not my_bell < int(list(store.values())[num-1]):
      print(list(store.keys())[num - 1], "을(를) 구입하셨습니다!")
      my_pocket.append(list(store.keys())[num - 1])

      my_bell = my_bell - int(list(store.values())[num - 1])
      store.pop(list(store.keys())[num - 1], None)
      print("남은 벨: ", my_bell)

    else :
      print("이런 .. 돈이 모자라구리 ..")

  # 2. 주민 찾아가기를 선택한 경우
  elif answer_action == "2":

    print("우리 마을에 있는 주민이야")
    i = 1
    for friend in animal:
        print(i, ". ", friend)
        i+=1
        
    animal_action = int(input("어떤 주민을 찾아갈까? ")) #고른 동물 숫자
    
    animal_who = list(animal.keys())[animal_action-1] #고른 동물 이름
    print(animal_who, "에게 무엇을 할까? ")
    
    answer_animal_action = int(input("1. 말걸기 2. 선물하기 3. 때리기")) #고른 동작
          

    # 2-1. 말걸기를 선택한 경우
    if answer_animal_action == 1:
      print(animal_who, ": ", script[animal_action-1])
      
      animal[animal_who] += 1
      print(animal_who, "친밀도 +1")
      
    
    # 2-2. 선물하기를 선택한 경우
    elif answer_animal_action == 2:
      print("내 주머니엔 이렇게 있어")
      print(my_pocket)
      i = 1
      for something in my_pocket:
        print(i, ". ", something)
        i+=1
        
      answer_gift = int(input("어떤 것을 선물할까? "))
      print(animal_who, "에게", my_pocket[answer_gift-1],"을(를) 선물했다!")
      my_pocket.pop(answer_gift-1)
      
      animal[animal_who] += 5
      print(animal_who, "친밀도 +5")
                        



    # 2-3. 떄리기를 선택한 경우
    elif answer_animal_action == 3:
      print(animal_who, "을(를) 때렸다! ")
      print(animal_who, ": ..?\n")
      animal[animal_who] -= 1
      print(animal_who, "친밀도 -1")

  

  # 3. 나무 흔들기를 선택한 경우
  elif answer_action == "3":

    print("나무를 흔듭니다.")
    print("응 ..?")

    cases = ["100벨", "사과", "벌"]
    result = (cases[int(random.randrange(0, 3))])

    # 100벨이 떨어질경우
    if result == "100벨":
      print("100벨이 떨어졌습니다!")
      print("100벨 벌었어 !!")

      my_bell = my_bell + 100

    # 사과가 떨어질경우
    elif result == "사과":
      print("사과가 떨어졌습니다!")
      print("사과를 얻었어 !!")
      print("사과를 주머니에 넣었습니다.")

      my_pocket.append("사과")

    # 벌이 나타날경우
    elif result == "벌":
      print("벌이 나타났습니다!")
      print("아야 .. 벌에게 물렸어 ..")



  # 4. 정보보기를 선택한 경우
  elif answer_action == "4":

    # 이름 출력
    print("- 이름 : ", name)
    # 남은 벨 출력
    print("- 남은 벨 : ", my_bell)
    # 주머니 출력
    if not my_pocket:
      print("- 내 주머니 : 비었음")
    else:
      print("- 내 주머니 : ", my_pocket)
    # 주민 친밀도 출력
    print("- 주민과 친밀도: ")
    
    i = 1
    for key, value in animal.items():
      print(int(i), ". ", str(key), ":", str(value))
      i += 1

  # 잘못된 입력을 했을경우
  else: 
    print("잘못된 입력입니다.")
