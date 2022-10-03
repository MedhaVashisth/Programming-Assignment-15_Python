#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python3 program to print all the numbers
# divisible by 5 or 7 for a given number

# Result generator with N
def NumGen(n):
	
	# iterate from 0 to N
	for j in range(1, n+1):

		# Short-circuit operator is used
		if j % 5 == 0 or j % 7 == 0:
			yield j

# Driver code
if __name__ == "__main__":
	
	# input goes here
	N = 50

	# Iterating over generator function
	for j in NumGen(N):
		print(j, end = " ")


# In[2]:


for num in range(4,15,2):
#here inside range function first no dentoes starting, second denotes end and third denotes the interval
	print(num)


# In[6]:


# A simple recursive CPP program to print
# first n Tribonacci numbers.

def printTribRec(n) :
	if (n == 0 or n == 1 or n == 2) :
		return 0
	elif (n == 3) :
		return 1
	else :
		return (printTribRec(n - 1) +
				printTribRec(n - 2) +
				printTribRec(n - 3))
		

def printTrib(n) :
	for i in range(1, n) :
		print( printTribRec(i) , " ", end = "")
		
acd@gmail.con
# Driver code
n = 10
printTrib(n)


# This code is contributed by Nikita Tiwari.


# In[11]:


import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))


# In[13]:


class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())      # prints 25 as given argument

print(Square().area())  # prints zero as default area


# In[ ]:




