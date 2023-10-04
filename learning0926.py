"""
Created on 2023 09 20
@author : Gary
"""


# %%

class Dog:
    def __init__(self, weight, name, age):
        self._weight = weight
        # 設定物件本身(self)屬性(.name/age)為外部參數(name/age)
        self.name = name
        self.age = age

    # 宣告叫的方法
    def bark(self, times=1):
        return "汪" * times

    # 利用 @property，將方法設定為屬性
    # 你可以看到物件裡面，內部參數的傳遞都是靠self來傳
    # 將 class (類) 的方法轉換為 只能讀取的 屬性
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def asHumanAge(self):
        return self.age * 7


park = Dog(70, "Park", 3)
print(park.name)
park.name = "Billy"
print(park.name)
print(park.age)
print(park.bark())
print(park.bark(3))
print(park.asHumanAge)
print(park.weight)
park.weight = 40
print(park.weight)
# 檢查park這個實例裡面，含有什麼屬性和方法
print(dir(park))


#%%
try:
    a = int(input())
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Other error")
finally:
    print("finally")


# %%
lst = ["black", "yoyo", "dai"]
print(lst[0])
print(lst[1])
print(lst[0:1])
print(lst[-1])
lst.append("passerby")
print(lst[0:4])
print(lst[:3])
print(lst[2:])
lst.insert(2, "passerby")
print(lst)
lstPassersby = ["passerby1", "passerby2", "passerby3"]
lst.extend(lstPassersby)
print(lst)

lst.remove("passerby")
print(lst)

popped = lst.pop(1)
print(popped)
print(lst)

del lst[0]
print(lst)

del lst[-1]
print(lst)

del lst[:]
print(lst)

# [start:stop:step].
lst = ["one", "two", "three", "four", "five", "six"]
del lst[0::2]
print(lst)
lst = ["one", "two", "three", "four", "five", "six"]
del lst[::2]
print(lst)

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'David']
print(l)

print([s for s in l if s != 'Bob'])

print([s for s in l if s.endswith('e')])

# remove duplicate elements
print(list(set(l)))


for i in range(len(lst)):
    popped = lst.pop()
    print(popped + "(QQ)")

print(lst)

lstHash = lst + lstPassersby
print(lstHash)

lst.sort()
print(lst)
lst = [5, 4, 8, 7]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

sorted_list = sorted(lst)
print("sorted_list: ", sorted_list, "\nlst: ", lst, sep='')

print(max(lst))
print(sum(lst))
print(min(lst))

print(lst.index(8))

for index, num in enumerate(lst, start=10):
    print(index, num)

lst = "               8                   ".split()
print(lst)
#%%

#list comprehension

count = [i for i in range(1, 11)]
square = [i*i for i in range(1, 11)]
print(count, '\n', square, sep='')
print(len(count), '\n', len(square), sep='')

sentence = "the rocket came back from mars"
vowels = [i for i in sentence]
vowels2 = [i for i in sentence if i in "aeiou"]
print(vowels)
print(vowels2)

#set&dict's comprehesion is the same