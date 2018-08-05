#Using loops to print all the elements in a loop
a = [1,2,3,4,5]
for elements in a:
    print(elements)

#print sum of all the elements in a list using loops
total = 0
for elements in  a:
    total += elements
print(total)

#Printing sum of numbers in a specified range,say 1 to 10
#Range is a pre defined key word that gives range untill 10 but not 10
total=0
h=list(range(1, 10))
for i in h:
    total+=i
print(total)

#printing sum of numbers divisible b 3 and 5 upto 50
total_3=0
total_5=0
l=list(range(1, 50))
for i in l:
    if (i%3)==0:
        total_3+=i
print(total_3)
for i  in l:
    if (i%5)==0:
        total_5+=i
print(total_5)        