#list=['satyanshu','saurabh','prasoon']

#output--->['prasoon','saurabh','satyanshu']
list1=['satyanshu','saurabh','prasoon']
rev=[]
#new=[]

for i in list1:
    rev.append(i[::-1])
    print(rev)
print(list1[::-1])