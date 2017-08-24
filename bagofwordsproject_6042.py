import math
import os
import re
list1=[]
for file in os.listdir():
	if file.endswith(".txt"):
		z = os.path.join(file)
		list1.append(z)
print(list1)
a=len(list1)
li=[]
for i in range(a):
	f=open(list1[i])
	read=f.read()
	s=read.lower()
	f.close()
	s = re.sub('[^a-z\']+'," ",s)
	r = list(s.split()) 
	li.append(r)
def dict(l1,l2):
	d1,d2 = {},{}
	for i in l1:
		if i in d1:
			d1[i]=d1[i]+1
		else:
			d1[i] = 1
	for j in l2:
		if j in d2:
			d2[j]=d2[j]+1
		else:
			d2[j] = 1
	return d1,d2
#Calculates dot product.
def dot(d1,d2):
	Dot = 0
	for i in d1:
		for j in d2:
			if i==j:
				Dot = Dot + (d1[i] * d2[j])	
	return Dot
#perform multiplication.
def Cross(d1,d2):
	sum1 = 0
	for i in d1:
		sum1=sum1+(d1[i]**2)
	SQ1 = math.sqrt(sum1)
	sum2 = 0
	for i in d2:
		sum2=sum2+(d2[i]**2)
		SQ2=math.sqrt(sum2)
		cross=SQ1*SQ2
	return(cross)
#perform distance between two files.
def euclid(Dot,cross):
	distance=(Dot/cross)*100
	return distance
Matrixlist = []
inc=0
for i in range(len(li)):
	finallist =[]
	for j in range(len(li)):
		d1,d2=dict(li[i],li[j])
		Dot=dot(d1,d2)
		cross=Cross(d1,d2)
		distance=euclid(Dot,cross)
		print(list1[i],'and',list1[j])
		finallist.append(distance)
		inc+= 1
	Matrixlist.append(finallist)
for i in range(len(Matrixlist)):
	print(Matrixlist[i])
