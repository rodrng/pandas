import random


def lotto_make(): # 아래 애들을 함수로 만들어서 input으로 입력 받아 원하는 게임 횟수만큼 for문으로 돌려줌
        lotto_list = []  # 빈 리스트 선언

        # for i in range(6): # 아무 반복문을 써도 되는데 얘는 지금 중복되도 출력됨 6개만 출력이아니라 5개 or 4개 ~

        while len(lotto_list) < 6:
            lotto_num = random.randint(1,45) # 1~45 사이의 정수 출력

            if lotto_num not in lotto_list:
                lotto_list.append(lotto_num)

        lotto_list.sort() # 로또 번호 오름차순 정렬
        print("나의 로또번호:", lotto_list)

su = int(input("시행 횟수:"))
for i in range(su):
    lotto_make()