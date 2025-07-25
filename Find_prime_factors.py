from typing import List
def is_prime(number: int) -> bool:
    """
    Determine if a given number is prime.

    Args:
        number (int): The number to evaluate for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Check for non-prime and potential prime numbers
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Test odd divisors up to the square root of number
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True

def find_prime_factors(number: int) -> List[int]:
    """
    Identify all prime factors of a given number.

    Args:
        number (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors in ascending order.
    """
    prime_factors = []
    divisor = 2
    # Continue dividing until number is reduced to 1
    while number > 1:
        while number % divisor == 0:
            number //= divisor
            prime_factors.append(divisor)
        divisor += 1
    return prime_factors

def main():
    """Handle user input and display prime number or prime factors results."""
    while True:
        user_input = input("Enter a number (or 'q' to quit): ").strip()
        if user_input.lower() == "q":
            print("Exiting program.")
            break

        try:
            user_number = int(user_input)
            if user_number <= 0:
                raise ValueError("Please enter a positive integer.")
            
            if is_prime(user_number):
                print(f"{user_number} is a prime number.")
            else:
                prime_factors = find_prime_factors(user_number)
                if user_number > 1:
                    print(f"{user_number} is not a prime numbers. prime factors: {prime_factors}")
                else:
                    print(f"{user_number} is not a prime number.")

        except ValueError as e:
            if "positive" in str(e):
                print(f"Error: {e}")
            else:
                print("Error: please enter a valid integer.")

if __name__ == "__main__":
    main()

