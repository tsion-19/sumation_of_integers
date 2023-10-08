# sum_integers.py
total = 0

while True:
   
    print('\nEOFError occurred')
    try:
        num =int(input("Enter a positive integer (0 to stop): "))
        if num == 0:
            break
        elif num < 0:
            print("Please enter a positive integer.")
        else:
            total += num
    except EOFError as e:
        print("Invalid input. Please enter a positive integer.")

print("Sum of the positive integers entered:", total)
