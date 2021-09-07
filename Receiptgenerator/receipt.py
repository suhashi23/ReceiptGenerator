sum = 0
l = []
while(True):
    userinpt = input("Enter the item price and press q to quit:")
    if (userinpt!='q'):
        sum += int(userinpt)
        l.append(int(userinpt))
        for i in range(len(l)):
            print(l[i])
        print(f"Order total so far: {sum}")
    else:
        print(f"Your total bill is {sum}")
        print("Thanks for coming in our shop, Have a Good day!")
        break