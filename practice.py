# 퀴즈 3
url = "http://naver.com"
url=url[8:]
dot=url.index(".")
url=url[0:dot]
print("url{a}{en}!".format(a=str(len(url)+1),en=url.count("e")))

# 답안

url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3]+str(len(my_str))+ str(my_str.count("e"))+"!"
print(password)

# 숫자를 문자열로 바꾸기 위해서는 str 함수를 씌워줘야 함
# replace 함수를 적절하게 사용하면 편리함


# 퀴즈 4

from random import *

comment = range(1,21)
comment = list(comment)
shuffle(comment)
winner = sample(comment,4)
print(winner[0])
print(winner[1:])

