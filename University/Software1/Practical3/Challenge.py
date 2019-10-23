from random import randint as rand
code = ""
for i in range (5):
    code += str(rand(0,9))


correct = False

while correct == False:
    flags = 0
    feedback = ""
    guess = input ("What's your guess: ")
    if guess == code:
        print ("You got it, well done")
        correct = True
        break
    elif len(guess) != len(code):
        continue
    
    for i in range(len(code)):
        if guess[i] == code[i] and flags < 3:
            flags += 1
            feedback += "R"

    for i in range(len(code)):
        for j in range(len(code)):
            if code[i]==guess[j] and flags < 3:
                flags += 1
                feedback += "B"
    print("Well no luck this time but here's your feedback")
    print (feedback)
            
