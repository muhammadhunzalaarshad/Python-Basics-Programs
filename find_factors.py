from typing import List
def is_prime(number: int) -> bool:
    """
    Check if the given number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

def find_factors(number: int) -> List[int]:
    """
    Find factors of a given numbers.

    Args:
        number (int): take a number for find factors.

    returns: 
        List: returns all factors of the given number.
    """
    factors = []
    for divisor in range(1, int(number ** 0.5) + 1):
        if number % divisor == 0:
            factors.append(divisor)
            if number // divisor != divisor:            
                factors.append(number // divisor)
    return sorted(factors)

def main():
    """Main function to handle user input and display result"""
    while True:
        user_input = input("Enter a number (or 'q' to quit): ").strip()
        if user_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            user_number = int(user_input)
            if user_number <= 0:
                raise ValueError("Please enter a positive integer.")
            
            if is_prime(user_number):
                print(f"{user_number} is a prime number.")
            else:
                factors = find_factors(user_number)
                print(f"{user_number} is not a prime number. factors: {factors}")

        except ValueError as e:
            if "positive" in str(e):
                print(f"Error: {str(e)}")
            else:
                print("Error: please enter a valid integer.")

if __name__ == "__main__":
    main()
