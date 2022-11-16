#리스트 자료형

odd=[1,3,5,7,9]

# 리스트 안에는 어떤 자료형도 포함될 수 있음

c=[13,14,'zz',[1231]]

# 리스트의 인덱싱 & 슬라이싱

a=[1,2,3]
print(a[-1]) # 답은 3 거꾸로 간다

# 다중 리스트

b=[1,2,['a','b']]
print(b[-1][1]) #b

c=[1,2,3,4,5]
print(c[0:2])

# 리스트 연산하기

a=[1,2,3]
b=[4,5,6]
print(a+b)

# 리스트 반복하기
a=[1,2,3]
print(a*3)
print(len(a))
del a[1:]
print(a)

# 리스트 관련 함수!!

a=[1,2,3]
a.append(4)
print(a) # 리스트 마지막 번째에 추가됨

a=[1,4,6,2]
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(6)) # 요소의 위치를 반환해주는 index 함수
print(a.count(2)) # 요소의 개수를 카운트해주는 함수
b=[3,4,5]
a.extend(b)
print(a)



# Tuple 자료형

# 튜플이 리스트와 다른점
# 1. 괄호 생략 가능 2. , 사용해야함 3. ()사용 ** 4. 수정이 불가능함 !(불변)

# 기본적인 함수들은 리스트와 동일함 다만, 삭제나 변경하는 함수인 del이나 append 등은 안됨


#Dictionary 자료형

# 딕셔너리 자료형의 특징은 key:value로 대응된다는 점 즉 key와 value가 하나의 쌍으로 존재한다

dic={'name':'Junsookim','location':'rocaf'}
dic['height']=173 # 딕셔너리 쌍을 추가하는 방법

#2시간17분
