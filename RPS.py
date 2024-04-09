import random 

score=0


def rps():
    global score
    l=["Rock","Scissors","Paper"]

    A= random.choice(l)
    a=A.lower()

    B=input("What's your choice:")
    b=B.lower()



    if a=="rock" and b=="rock" or a=="scissors" and b=="scissors" or a=="paper" and b=="paper":
        print("Its a draw")

    elif a=="rock" and b=="scissors" or a=="scissors" and b=="paper" or a=="paper" and b=="rock":
        print("You lose🥲")

    elif a=="scissors" and b=="rock" or a=="paper" and b=="scissors" or a=="rock" and b=="paper":
        score=score+1
        print("You won😀") 

    sum()

def sum():    
    print("Select an option")
    print("1.Play again")
    print("2.Exit and Get your score")
    choice=int(input("Enter your choice:"))


    if choice==1:
        rps()

    else:
        print("Your Score is:",score)
        print("Thanks for playing")


sum()







    







