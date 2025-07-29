def gcd_fumc(number_1: int, number_2: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

    Args:
        number_1 (int): The first integer.
        number_2 (int): The second integer.

    Returns:
        int: The GCD of the two numbers.
    """
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1

def lcm_func(number_1: int, number_2: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers using their GCD.

    Args:
        number_1 (int): The first integer.
        number_2 (int): The second integer.

    Returns:
        int: The LCM of the two numbers.
    """
    gcd = gcd_fumc(number_1, number_2)
    return (number_1 * number_2) / gcd

def main() -> None:
    """
    Main function to calculate the LCM of two user-provided numbers.

    Prompts the user to enter two numbers, calculates their LCM, and handles input validation.
    Exits when the user enters 'q'.
    """
    while True:
        first_input = input("Enter a first number (or 'q' to quit): ").strip()
        if first_input.lower() == "q":
            print("Exiting program.")
            break

        second_input = input("Enter a second number (or 'q' to quit): ").strip()
        if second_input.lower() == "q":
            print("Exiting program.")
            break

        try:
            first_number = int(first_input)
            second_number = int(second_input)

            if first_number <= 0 or second_number <= 0:
                raise ValueError("Please enter a valid integer.")
            
            lcm = lcm_func(first_number, second_number)

            print(f"{f"LCM of {first_number} and {second_number} is: {int(lcm)}"}")
        except ValueError as e:
            if "positive" in str(e):
                print(f"Error: {str}")
            else:
                print("Error: please enter a valid integer")

if __name__ == "__main__":
    main()



