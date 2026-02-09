while True:
    num = input("Enter any natural number : ")
    try:
        num = int(num)
        if num < 1:
            print("Please enter a natural number")
        else:
            break
    except ValueError:
        print("Invalid Input, Try again!")
        continue
print(f"{(num*(num+1))/2}")