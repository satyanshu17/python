user={'Name':'chetan','age':31}
print(user)


#items method

if ('chetan','name') in user.items():
    print('present')

else:
    print('not present')

#how to apply loops in dictionary
for i in user:
    print(i)

#keys method

for i in user.keys():
    print(i)

#values method

for i in user.values():
    print(i)

#item methods

for i,j in user.items():
    print(f'{i}:{j}')

for i in user.items():
    print(i)

