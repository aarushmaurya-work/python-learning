while True:
    num = input(f"Enter the number you want multiplication table of : ")
    try:
        num = int(num)
        break
    except ValueError:
        print("Invalid Input, try again")
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")