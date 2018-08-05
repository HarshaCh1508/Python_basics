#defining a list
#Unlike the other languages python can store different datatypes in same list
a = [1, 2, -5, 8, 'Hello']
print(a)

#Adding another element to the list
#the element added can be any data type. You can even add another list
a.append([1,'world'])
print(a)

#Deleting an element from list
#It deletes the last element in the list
a.pop()
print(a)

#You can replace any element using the index value
#Like the other languages the index value starts with 0.
a[1]=6
print(a)

#Swapping elements in a list
l = ['banana', 'watermelon', 'apple']
#swapping banana and apple
temp = l[0]
l[0] = l[2]
l[2] = temp
print(l)
#without using temp variable
l[0], l[2] = l[2], l[0]
print(l)