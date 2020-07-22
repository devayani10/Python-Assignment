#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = 47
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")


# In[2]:


n=int(input("enter the number"))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(s)


# In[ ]:




