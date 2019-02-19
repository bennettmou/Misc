# Found at https://www.youtube.com/watch?v=AWek49wXGzI

name = "Paul"
height_m = 1.7
weight_kg = 77

bmi = weight_kg / (height_m ** 2)
print("BMI: " + str(bmi)) # Has to be a string

if bmi < 25:
    print(name + (" is not overweight. You hairy little toothpick."))
else:
    print(name + (" is overweight! BOOO!!! You lumpy, lumpy man."))

# Cleaned up to have details on the same line.
# Also a little self ribbing.