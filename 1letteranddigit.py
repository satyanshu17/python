#calc number of digit and letter 
sentence=(input('input a sentence'))
digit=letter=0
for i in sentence:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    else:
        pass
print(letter)
print(digit)
