name="Harsha"
weight_kg=68
height_m=2

bmi=weight_kg/height_m**2
print("bmi: ")
print(bmi)
if bmi<25:
    print(name)
    print(" is not overweighted.")
else:
    print(name)
    print(" is overweighted.")    