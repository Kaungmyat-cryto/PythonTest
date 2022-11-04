#append
#[list1[list2]]
firstname=['Kaung','Myat']
lastname=['Hein']
firstname.append(lastname)
print(firstname)

#extend
#[list1,interable]
firstname=['Kaung','Myat']
lastname=['Hein']
firstname.extend(lastname)
print(firstname)

#pop
#return and then removed
#default is -1
name=['Kaung','myat','hein']
#default
new=name.pop()
print(new)
print(name)
#chosen argument
name=['Kaung','myat','hein']
newest=name.pop(0)
print(newest)
print(name)

#sort
alphabet=['d','a','c','b','e']
#ascending
alphabet.sort()
print(alphabet)
#descending
alphabet.sort(reverse=True)
print(alphabet)


#count
#count return the number of character
no = ['1','0','0','1','0','2']
count = no.count('0')
print('The count of i is:', count)


