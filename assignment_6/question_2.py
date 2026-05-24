#Build rock, paper, scissor game
import random
l=["rock","paper","scissor"]
uscore=0
cscore=0
name=input("Enter your name:")
print("Welcome",name,"!")
print("1=Rock\n2=Paper\n3=Scissor")
for i in range(5):
    uch=int(input(f"{name} enter your choice:"))
    cch=random.choice(l)
    if (uch==1):
        uch="rock"
    elif(uch==2):
        uch="paper"
    elif(uch==3):
        uch="scissor"
    else:
        print("boo")

    print(f"Your choice:{uch}")
    print(f"Enemy's choice:{cch}")        

    if (uch==cch):
        print("Game Draw\n")
        uscore+=1
        cscore+=1
    elif((uch=="rock" and cch=="scissor") or (uch=="paper" and cch=="rock") or (uch=="scissor" and cch=="paper")):
        print("You won!\n")
        uscore+=2
    elif((cch=="rock" and uch=="scissor") or (cch=="paper" and uch=="rock") or (cch=="scissor" and uch=="paper")):
        print("You lost:(\n") 
        cscore+=2
    else:
        print("Invalid input\n")
       

print("Your Score=",uscore)
print("Enemy Score=",cscore)   
if(uscore>cscore):
    print("Congrats! You won")
elif(cscore>uscore):
    print("You lost")      
else:
    print("It was a tie")     

