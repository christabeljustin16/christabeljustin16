import re

print("My Magical Caculator")
print("Type 'quit' to exit\n")
#I'm making my very first calculator
previous = 0
run = True

def performMath():
    global run
    global previous
    equation =""
    if previous == 0:
       equation = input("Enter equation:")
    else:
        equation = input(str(previous))


    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-z,.:() " "]', '', equation)

        if previous == 0:
             previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


        print("You typed",previous)

while run:
    performMath()