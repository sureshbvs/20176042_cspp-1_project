import math
import os
import re
class Bag_of_Words(object):
	global list1
	list1=[]
#reading file from the path and appending to list	
	for file in os.listdir():
		if file.endswith(".txt"):
			z = os.path.join(file)
			list1.append(z)
	print(list1)
	a=len(list1)
	global li
	li=[]
#Reading file and convert to lower case and removing special characters.
	for i in range(a):
		f=open(list1[i])
		read=f.read()
		s=read.lower()
		f.close()
		s = re.sub('[^a-z\']+'," ",s)
		r = list(s.split()) 
		print(r)
		li.append(r)
#frequency count in dictionary
	def dict(self,l1,l2):
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
	
# Pass the file1 words frequency and file2 words frequency and calculate the dotproduct
# Input: two dictionaries with their word frequencies
# Output: dot product of those two files
	def dot(self,d1,d2):
		Dot = 0
		for i in d1:
			for j in d2:
				if i==j:
					Dot = Dot + (d1[i] * d2[j])	
		return Dot
#perform multiplication.
	def Cross(self,d1,d2):
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
	def euclid(self,Dot,cross):
		distance=(Dot/cross)*100
		return distance
#Input matrix list
Matrixlist = []
inc=0
for i in range(len(li)):
	finallist =[]
	for j in range(len(li)):
		m = Bag_of_Words()
		d1,d2=m.dict(li[i],li[j])
		Dot=m.dot(d1,d2)
		cross=m.Cross(d1,d2)
		distance=m.euclid(Dot,cross)
		print(list1[i],'and',list1[j])
		finallist.append(distance)
		inc+= 1
	Matrixlist.append(finallist)
#prints list in matrix form
for i in range(len(Matrixlist)):
	print(Matrixlist[i])
