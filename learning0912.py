print()
print(ord('B')) # Unicode code point of the character 'B'
print(ord('&'))
print(chr(67)) # Convert the integer 67 into its corresponding character. In Unicode, 67 represents the character 'C
print(chr(8365))
print(len("this is my python program"))
print(max("this is my python program"))
print(min("this is my python program"))
print("from" in "information")
print("python" in "information")
print("from" not in "information")
#%%
s="Today is a beautiful day"

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace("beautiful", "sunny"))
print(str.capitalize("python"))
print(str.title("a book"))

print()
s="Hello"
print(s.center(10, '#'))
print(s.ljust(10, '♥'))
print(s.rjust(10, '♧'))
print("-100".zfill(6))
print("100".zfill(6))

# Aha! No homework

#%%

print()
print(format(168, "<10"))
print(format(168, ">10"))
print(format(168, "^10"))
print(format(168, "@^10"))
print(format(1234567890, ","))
print(format(65, "#b"))
print(format(65, "#o"))
print(format(65, "#x"))
print(format(168, "+010"))
import random
a = random.randint(1, 314159)
print(a)
print(random.random()*100)
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print('-----------------------------------')
# n = eval(input("input value for triangle high: "))
n = 8
for i in range(1,n+1):
    for j in range(i):
        print('*',end="")
    print()
print('----------------------------------')
for i in range(n,0,-1):
    for j in range(i):
        print('*',end="")
    print()

print("Hello World!")
x = 5
y = 6.1
z = "123"
print(x+y+eval(z))
print(str(x)+str(y)+z)
name = "Gary"
apple_val = 3.005
apple_val2 = 3.0051
print("%s有%.2f個蘋果"%(name,apple_val))
print("%s有%.2f個蘋果"%(name,apple_val2))
print("%s有%d個蘋果"%(name,apple_val2))
where_is_my_money = 87
hytech = "海科🚀"
score = 87.8787878787
import math
print("%d%s%.2f" % (where_is_my_money,hytech[0:2],math.floor(score*100)/100.0))


car1 = ["toyota","honda","benz","bmw"]
car2 = ["ford","nissan"]
car3 = car1+car2
print(car3)

print(list(range(0,11)))
print(8, "hello", 8)
print(8, "hello", 8, sep="&")

price=3.1415
print("price:%2.9f" %price)

x=30
print("x=/%-16d/" %x)

y=12.5
print("y=/%-7.2f/" %y)
z=123.456
print("z=/%06.5f/" %z)
print("z=/{:06.5f}/".format(z))

