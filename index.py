# 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

# 파이썬 기본편 강의

print("Hello Python")
print((3>5)|(5>3))
print(3**3)

# 숫자 처리함수

print(abs(-5)) # 절댓값
print(pow(4,2)) # 4^2 = 16 제곱
print(max(5,12)) # 최댓값
print(min(5,12)) # 최솟값
print(round(3.4)) # 반올림

from math import *
print(floor(4.99)) # 내림 4
print(ceil(4.33)) # 올림 5
print(sqrt(16)) # 제곱근 4

# 랜덤함수

from random import *
print(random()) # 0.0~1.0 미만 임의의 값 생성
print(random()*10) # 0.0~10.0 미만 임의의 값 생성
print(int(random()*10)) # 0~10 미만 임의의 값 생성

print(int(random()*45)+1)

print(randrange(1,46)) # 1~45 이하의 임의의 값 생성 + 하나 크게 설정해야

print(randint(1,45)) # 1~45 이하의 값 

# 문자열

sentence ='나는 소년입니다'
print(sentence)
sentence2 ="파이썬"
print(sentence2)

sentence3 = """
나는 소년이고http://naver.com
파이썬은 쉽다!
"""
print(sentence3)

# 슬라이싱

jumin = "031202-1234567"


print(jumin[7])
print(jumin[0:2]) # 0부터 1까지 (0,1)
print(jumin[:6]) #처음부터 6 직전까지
print(jumin[7:]) #7부터 끝까지
print(jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리함수

python = "Python is Amazing"
print(python.lower)
print(python.upper)
print(python[0].isupper()) # 첫번째 글자가 대문자인지 아닌지

print(len(python)) # 문자열 길이
print(python.replace("Python","Java")) #문자열 바꾸는 함수

index=python.index("n")
print(index) # n이 몇번째에 있는지 출력하는 함수
index=python.index("n",index+1) # index+1이 시작 위치! 6번째부터 계산해서 있는지 없는지 확인
print(index) 

print(python.find("n"))
print(python.count("n")) #n이 몇번 나왔는지 세는 함수

# 문자열 포맷 방식


# 방법 1

print("나는 %d살입니다." %20)
print("나는 %s을 좋아해요." % "파이썬") #문자열
