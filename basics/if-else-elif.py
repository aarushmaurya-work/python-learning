#if is use to set conditions

age = int(input(f"Enter your age : "))
if age < 1 :
    print("Invalid Age") #if is independent, and the first condition check
elif age < 18 :
    print("Access Denied") #elifs are the check after the if is False, all the Elifes are checked one by one as per the order
else: 
    print("Welcome!")#if every condition check is Flase, then the else block is executed

