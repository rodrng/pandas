import pandas as pd

se1 = pd.Series([10,20,30,40], index=["홍길동","이순신","김유신","강감찬"]) #index 값을 굳이 주지않더라도 앞쪽? 왼쪽 끝? 인덱스열이생김 0 1 2 3
print(se1)
print("")
print(se1[["홍길동","김유신"]])
print("")
print(se1.index)
print(se1.values)
print(sorted(se1.index)) # 값을 정렬
print("-------------------------------------")

list1 = [1,2,12,1,2,1,1,1,5,78,5,3]
se2 = pd.Series(list1) # list1을 Series로 변환
se2_uique = pd.unique(se2) # unique 중복제거하는 함수
print(se2_uique)

print("-------------------------------------")
age ={"홍길동":23, "김유신":30, "이순신":40, "강감찬":31} # 사전구조(딕셔너리?)
se3 = pd.Series(age)
print(se3)