def add(x, y):
    return x + y
e = add(4, 5)    
print(e)
#functions can be called many times
f = add(1258, 45682)
print(f)
def function(x):
    print(x)
    print('This will be only executed when a function is called')
    return 3*x
g = function(6)
h = function(7)
print(g)    
print(h)
#The variables g and h will hold only the values of return statements but still the print statements in the function get executed whenever the function is called.
i = add(g, h)
print(i) 

#BmI calculator using functions
name1 = 'Harsha'
weight_kg1 = 68
height_m1 = 1

name2 = 'chakri'
weight_kg2 = 63
height_m2 = 1.1

name3 = 'karthik'
weight_kg3 = 65
height_m3 = 0.8

def bmi_calculator(name, weight_kg, height_m):
    bmi = weight_kg / (height_m**2)
    print('bmi: ')
    print(bmi)
    if bmi < 25:
        return name + " is not overweighted"
    else:
         return name + " is overweighted"

result1 = bmi_calculator(name1, weight_kg1, height_m1)
result2 = bmi_calculator(name2, weight_kg2, height_m2)
result3 = bmi_calculator(name3, weight_kg3, height_m3)
print(result1)
print(result2)
print(result3)