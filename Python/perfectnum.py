# Get user input
user_input = input("Enter a positive integer: ")

# Check if the input is a positive integer
if user_input.isdigit():
    num = int(user_input)

    # Ensure the number is positive
    if num > 0:
        # Calculate the sum of divisors
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])

        # Check if the sum of divisors equals the original number
        if divisors_sum == num:
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")
    else:
        print("Please enter a positive integer.")
else:
    print("Invalid input. Please enter a valid integer.")
