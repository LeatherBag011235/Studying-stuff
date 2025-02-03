while True:
    try:
        number = int(input(f"Please, enter an integer:"))
        if number > 0:
            break
        else:
            print("Please enter a positive integer")
    except ValueError:
            print("Invalid input. Please enter a integer value.")

str_num = str(number)
reversed_str = str_num[::-1]

if str_num == reversed_str:
    print(f"{str_num} is a palindrome")
else:
    print(f"{str_num} is not a palindrome")