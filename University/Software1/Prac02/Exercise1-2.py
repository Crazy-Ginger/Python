equation = "6 * 1 - 2"
equation = equation.replace(" ", "")

new_equation = ""
for i in range (0, len(equation)):
    if i == 1:
        new_equation += equation[i] + "("
    elif i == len(equation)-1:
        new_equation += equation[i] + ")"
    else:
        new_equation += equation[i]
print (new_equation)
