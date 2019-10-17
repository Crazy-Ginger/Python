code = "01091"


correct = False

while correct == False:
    guess = input("What's your guess: ")
    if len(guess) != len(code):
        print("Wrong!")
        continue
    print (code)
    print (guess)

    for i in range (len(code)):
        
