#capatilize()
name="kaung myat hein"
result=name.capitalize()
print ("My name is ",result)
#can change the only

#center()
warning="your password is incorrect"
defaultfill=warning.center(55)
print(defaultfill)
optionalfill=warning.center(55,'#')
print(optionalfill)

#count()
paragraph="singing the same song.walking from the same direction"
count=paragraph.count('s')
print("Used the 's'",count ,"times.")
countinrange=paragraph.count('s',0,26)
print("Used the 's'",countinrange,"times in 1st sentence.")

#expandtabs(
string='kaung\tmyat\thein'
defaultabs=string.expandtabs()
print(defaultabs)
tabs=string.expandtabs(6)
print(tabs)

#partition()
name="My name is Kaung Myat Hein."
ispartition=name.partition('s')
print(ispartition)
arepartition=name.partition('are')
print(arepartition)
#as there is no are separator

#title()
name='kaung myat hein'
title=name.title()
print(title)
# capitalizes the first letter

#swapcase()
string='wAtErMeLon SuGaR'
swap=string.swapcase()
print(swap)
#swap each character.

#zfill()
#fill with 0
fruit='orange'
zfill=fruit.zfill(10)
print(zfill)

#replace()
string="Chicken wing Chicken wing Hot dogs and balogna Chicken and macaroni"
replace=string.replace('C','c',2)
print(replace)
#changed 2 C.