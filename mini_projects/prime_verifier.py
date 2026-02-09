while True:
    num = input("Enter any natural number : ")
    try:
        num = int(num)

        if num == 1:
            print("1 is neither prime, nor composite")
            continue
        elif num < 1:
            print("This is not a natural number, try again!")
            continue
        else:
            break

    except ValueError:
        print(f"'{num}' is not a valid natural number")

for i in range(2, num):
    if num%i == 0:
        print("It is a composite number")
        break
else:
    print("It is a prime number")
    