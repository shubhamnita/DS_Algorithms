# Enter your code here. Read input from STDIN. Print output to STDOUT
A= set(map(int,input().split()))
n = int(input())
i=0
for i in range(n):
    s= set(map(int,input().split()))
    #print(s)
    #print(A&s)
    if len(A&s)==len(s) and len(A)>len(s):
        i=1
    else:
        i=0
        break
    
if i==1:
    print("True")
else:
    print('False')



######################################################################################33
#valid email or not
import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)