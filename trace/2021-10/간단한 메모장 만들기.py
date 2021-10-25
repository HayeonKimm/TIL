#!/usr/bin/env python
# coding: utf-8

# # 간단한 메모장 만들기

# In[1]:


# C:/doit/memo.py

f1 = open("memo.py",'w')
f1.write("""


import sys

option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)
""")
f1.close()


# sys.argv는 프로그램을 실행할 때 입력된 값을 읽어 들일 수 있는 파이썬 라이브러리이다.   
# 
# 
# sys.argv[0]는 입력받은 값 중에서 파이썬 프로그램 이름인 memo.py이므로 우리가 만들려는 기능에는 필요 없는 값이다.   
# 
# 
# 그리고 순서대로 sys.argv[1]은 프로그램 실행 옵션 값이 되고 sys.argv[2]는 메모 내용이 된다.

# In[2]:


f1 = open('memo.py','r')
print(f1.read())


# In[4]:


# bash에서 실행했다.
# python memo.py -a "Life is too short"


# In[7]:


import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt','%w')
    f.write(memo)
    f.write('\n')
    f.close()


# 옵션이 -a인 경우에만 memo 값을 읽어 memo.txt 파일에 그 값을 쓰도록 코드를 작성했다.   
# 
# 
# 여기에서 메모는 항상 새로운 내용이 작성되는 것이 아니라 한 줄씩 추가되어야 하므로 파일열기 모드를 a로 했다.   
# 
# 
# 그리고 메모를 추가할 때마다 다음 줄에 저장되도록 줄바꿈 문자(\n)도 추가로 파일에 쓰게 했다.

# In[9]:


# type memo.txt
# git bash 에서 돌아가지 않는다. txt 파일이 존재하지 않는다.


# In[10]:


# 두개의 옵션 버전


import sys
option =sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
    
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
    
    # 옵션으로 –v가 들어온 경우 memo.txt 파일을 읽어서 출력한다.
    

