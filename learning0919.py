"""
@author : Gary
"""
"""
判斷輸入的數值是否大於0 如果大於0則輸出訊息:
您輸入的數值  大於0
無論是否大於0. 最後皆輸出結束
"""
num = eval(input("Please enter a value:"))
if num > 0:
    print("The value", num, "is greater than 0")
else:
    print("The value", num, "is lesser than 0")

"""
成績判斷
大於等於90 -> 優
80~89 -> 甲
70~79 -> 乙
60~69 -> 丙
未滿60 -> 不及格
"""
score = eval(input("請輸入成績:"))
if score >= 90:
    print("優")
else:
    if score >= 80:
        print("甲")
    else:
        if score >= 70:
            print("乙")
        else:
            if score >= 60:
                print("丙")
            else:
                print("不及格")

"""
閏年判斷
可以除以400 或 可以除以4卻不能除以100 的西元年分為閏年
"""
year = eval(input("請輸入西元年"))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("閏年")
else:
    print("非閏年")


def Fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return Fib(N - 1) + Fib(N - 2)


for i in range(10):
    print(Fib(i), end=' ')

"""
樂透 (1~49亂數取6，不重複)
"""
import random

lotto = []
n = 1
while n <= 6:
    randomNumber = random.randint(1, 49)
    if randomNumber not in lotto:
        lotto.append(randomNumber)
        n += 1
lotto.sort()
for i in lotto:
    print(i, end=" ")
lotto.sort(reverse=True)
print()
for i in lotto:
    print(i, end=" ")


#Tuple (不可修改裡面參數)
num =(10,20,30,40,50)
fruits=('apple', 'orange', 'banana')
val_tuple=(100, )
print(num[0])
print(num[4])
print(fruits[1])
print(val_tuple[0])
for i in num:
    print(i)
# num[0] = 30
# print(num[0])
num = (30,20,30,40,50)
print(num[0])

hexChar = input()
hexChar = hexChar.upper()
if hexChar >='0' and hexChar<='9':
    print(ord(hexChar)-ord('0'))
elif hexChar >='A' and hexChar <='F':
    print(ord(hexChar)-ord('A')+10)
else:
    print("error")

math = {'Kevin','Kevin', 'Peter', 'Eric'}
math.add('trin')
physics = {'Peter', 'Nelson', 'Tom'}

print(math & physics) #同時參加數學與物理夏令營的成員
print(math | physics) #有參加
print(math - physics) #只參加數學
print(math ^ physics) #有參加但沒有都參加

#Dict

fruits = {'西瓜':20, '香蕉':10, '水蜜桃':25}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
print("水蜜桃一斤 = ", fruits['水蜜桃'], "元")
print("牛肉麵一碗 = ", noodles['牛肉麵'], "元")

#add to dict
fruits['橘子'] = 17
print(fruits)
print("橘子一斤 = ", fruits['橘子'], "元")

for fruit, price in fruits.items():
    print("水果", fruit,"價格", price)

print(tuple(fruits.keys()))
print(tuple(fruits.values()))

print(fruits.get('香蕉', "error"))
print(fruits.get('木瓜', "error"))

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}

for name in sorted(players.keys()):
    print(name)
    print("Hi,", name, "I like ur performance in", players[name])
    print(f"Hi, {name},I like ur performance in {players[name]}")

sports = {'Curry':['籃球', '美式足球'],
          'James':['football', 'baseball', 'basketball']}

for name , Psports in sports.items():
    print("%s喜歡的運動是:" %name)
    for sport in Psports:
        print(" ", sport)


wechat_account = {'cshung':{'name':'李大年',
                            'city':'台北'},
                  'kevin':{'name':'王大同',
                           'city':'北京'}
                  }
for account, account_info in wechat_account.items():
    print("user name = ", account)
    print("name      = ", account_info['name'])
    print("city      = ", account_info['city'])


survey_dict = {}
market_survey = True
while market_survey:
    name = input("\nPlease enter ur name : ")
    travel_location = input("Enter ur fantastic tourist attraction : ")
    survey_dict[name] = travel_location
    repeat = input("Is anyone continuing?(y/n) ")
    if repeat != 'y':
        market_survey = False
print(survey_dict)
print("\nThere's result")
for user, location in survey_dict.items():
    print(user, "Tourist attraction: ", location)
