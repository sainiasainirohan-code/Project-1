import random
print("""
   1. Rock
   2.Paper
   3.scissor
   4.exit
   """)
while True:
    choice=int(input("Enter your choice:"))
    computer=random.randint(1,3)
    print("Computer choice:",computer)
    if choice==1 and computer==2:
        print("You lost!")
    elif choice==1 and computer==3:
        print("You win!")
    elif choice==2 and computer==1:
        print("You  win!")
    elif choice==2 and computer==3:
        print("You lost!")
    elif choice==3 and computer==1:
        print("You lost!")
    elif choice==3 and computer==2:
        print("You win!")
    elif choice==computer:
        print("Tie!")
    elif choice==4:
        print("exit")
        break
    else:
        print("Choose option from 1 to 4 only")