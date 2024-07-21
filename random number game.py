import random

n=random.randint(1,50)
guess=0
a=-1
while(a!=n):
    a=int(input("Guess the number: "))
    if(a>n):
        print("\nthe number is lower")
    elif(a<n):
        print("\nthe number is higher")    
    else:
        print("\nyou guess the the correct number")
    guess+=1        
    
print(f"you guess the number in {guess} attemps")    
