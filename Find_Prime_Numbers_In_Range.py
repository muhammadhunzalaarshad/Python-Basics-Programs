from typing import List
def is_prime(number: int) -> bool:
    """
    Determine if a given number is prime.

    Args:
        number (int): The number to evaluate for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle non-prime and edge cases
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Check odd divisors up to square root of number
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True

def Find_prime_numbers_in_range(start_number: int, end_number: int) -> List[int]:
    """
    Identify all prime numbers within a specified range.

    Args:
        start_number (int): The starting number of the range (inclusive).
        end_number (int): The ending number of the range (inclusive).

    Returns:
        List[int]: A list of prime numbers in the given range.
    """
    prime_numbers = []
    start = max(2, start_number)
    # Use step of 1 for even start to include 2, or 2 for odd start to skip even numbers 
    step = 1 if start % 2 == 0 else 2
    for divisor in range(start_number, end_number + 1, step):
        if is_prime(divisor):
            prime_numbers.append(divisor)
    return prime_numbers

def main() -> None:
    """Handle user input to find prime numbers in a specified range and display results."""
    while True:
        start_input = input("Enter a start number: (or 'q' to quit): ").strip()
        if "q" in start_input.lower():
            print("Exiting program")
            break

        second_input = input("Enter an end number: (or 'q' to quit): ").strip()
        if "q" in second_input.lower():
            print("Exiting program")
            break
        
        try:
            start_number = int(start_input)
            end_number = int(second_input)

            if start_number <= 0 or end_number <= 0:
                raise ValueError("Please enter a positive integer.")
            
            if start_number > end_number:
                raise ValueError("Start number must be less than or equal to end number.")
            
            prime_numbers = Find_prime_numbers_in_range(start_number, end_number)
            if prime_numbers:
                print(f"Prime numbers between {start_number} and {end_number} are: {prime_numbers}")            
            else:
                print(f"No prime numbers found between {start_number} and {end_number}.")
        
        except ValueError as e:
            if "positive"  in str(e) or "less" in str(e):
                print(f"Error: {e}")
            else:
                print("Error: please enter a valid integer.")

if __name__ == "__main__":
    main()



