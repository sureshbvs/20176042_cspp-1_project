class lcs(object):
	def lcs(self,s1,s2):
	    res = ""
	    l1=len(s1)
	    l2=len(s2)
	    for i in range(l1):
	        for j in range(l2):
	            point=0
	            res1=''
	            while ((i+point < l1) and (j+point<l2) and s1[i+point] == s2[j+point]):
	                res1=res1+s2[j+point]
	                #print(res1)
	                point=point+1
	            if (len(res1) > len(res)):
	                res = res1

	    return res
#taking file from the path
filelist = []
import os
for file in os.listdir():
	if file.endswith(".txt"):
		y = os.path.join(file)
		filelist.append(y)
print(filelist)
#file reading
#remove special characters and convert string to words in  list.
import re
lst=[]
for i in range(len(filelist)):
	file = open(filelist[i], 'r')
	text = file.read()
	file.close()
	text = re.sub('[^a-z\ \']+', " ", text)
	text = text.replace(" ","")
	words = list(text.split())
	lst.append(words)
Matrixlist= []
for i in range(len(lst)):
	arr2 =[]
	for j in range(len(lst)):
#object creation
		obj=lcs()
		print(lst)
#convert list to string and passed to lcs function
		result= obj.lcs(" ".join(str(x) for x in lst[i])," ".join(str(x) for x in lst[j]))
		str1 = " ".join(str(x) for x in lst[i])
		len1 = len(str1)
		str2 = " ".join(str(x) for x in lst[j])
		len2 = len(str2)
		totallength = len1 + len2
		print(result)
		print(len(result))
		finalresult = ((len(result) * 2) / totallength) * 100
		print(finalresult)
		arr2.append(finalresult)
	Matrixlist.append(arr2)
#printing matrix
for i in range(len(Matrixlist)):
	print(Matrixlist[i])