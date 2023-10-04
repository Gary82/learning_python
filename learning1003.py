"""
Created on 2023/09/21

@author: Gary
"""

# %%
# r : 只讀 , r+ : 讀寫(不創建檔案)
path = "D:\\project\\python\\file.txt"
f = open(path, 'r+')
# f = open(path)
words = f.read()
print(words)
f.write("\nfile1")
f.close()

#%%
# w : 只寫不能讀 , w+ : 讀寫(沒檔案會創建檔案)
path = "D:\\project\\python\\file2.txt"
f = open(path, 'w+')
words = f.read()
print('w+ before:', words)
f.write("file2")
f.seek(0)
words = f.read()
print('w+ after: ', words)
f.close()
#
# #%%

#%%
# a : 追加(不可讀) , a+ : 讀寫(沒檔案會創建檔案)
path = "D:\\project\\python\\file2.txt"
f = open(path, 'a+')
f.seek(0)
words = f.read()
print('a+ before:', words)
f.write("\nfile")
f.seek(0)
words = f.read()
print('a+ after: ', words)
f.close()

#%%

from pathlib import Path

f = Path("D:\\project\\python\\file.txt")
f1 = Path("D:\\project\\python\\file2.txt")
if f.exists():
    print(f.stat())
if f1.exists():
    print(f1.stat())
# write
f1.write_text("Hello python !")
# del
f1.unlink()
# f.close()


path = "D:\\project\\python\\file.txt"
with open(path, 'r') as f:
    # word = f.read()
    # print(word)
    print(f.readline())


#%%

path = "C:\\Users\\bruce\\OneDrive\\Documents\\pyLearn\\class\\create.txt"
f = open(path, 'a')
f.write("HaHaHa")
f.close()

#%%

path = "file_hello.txt"
with open(path, 'r') as f:
    # word = f.read()
    # print(word)
    print(f.readline())
