import random
def user_choice():
    print("Enter Range 'from' 'to' number")
    print("StartINT")
    startint = int(input())
    print("EndINT")
    endint = int(input())
    return startint, endint

def randomnumber(startint,endint):
    randint = random.randrange(startint,endint)
    print(f"Your Random Number is: {randint}")

def main():
    startint,endint=user_choice()
    randomnumber(startint,endint)

if __name__ == "__main__":
    main()