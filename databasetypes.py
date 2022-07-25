#database types----> list,tuple,dictionary

#list-->unordered database
#all type of data store--->string,number,mixed
#list denote--->[]

fruits=['apple','mango','kiwi']
print(fruits)
print(type(fruits))

#how to add data to list

#append
#insert

fruits.append('banana')
print(fruits)

fruits.insert(1,'papaya')
print(fruits)

#how to remove data from list

#pop
#remove

#fruits.pop()
#print(fruits)

fruits.remove('kiwi')
print(fruits)

#extend

l1=[1,2,3]
l2=[4,5,6]

#print(l1+l2)
#print(l1)

l2.extend(l1)
print(l2)