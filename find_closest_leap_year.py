def is_leap_year(year: int) -> bool:
    """
   Determine if a given year is a leap year.

    Args:
        year (int): The year to evaluate.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    # Check leap year conditions: divisible by 4 and not 100, or divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_closest_leap_year(year: int) -> int:
    """
    Find the closest leap year to the given year.

    Args:
        year (int): The year to evaluate.

    Returns:
        int: The closest leap year to the input year. If the input year is a leap year, returns the same year.
    """
    if not is_leap_year(year):
        # Search backward and forward, stepping by 1 year
        before_year = year - 1
        after_year = year + 1

        while not is_leap_year(before_year):
            before_year -= 1

        while not is_leap_year(after_year):
            after_year += 1

    # Return the closer of the two leap years        
    return  before_year if (year - before_year <= after_year - year) else after_year

    
def main():
    """Main function to handle user input and display leap year information."""
    while True:
        user_input = input("Enter a year (or 'q' to quit): ").strip()
        if user_input.lower() == "q":
            break

        try:
            user_year = int(user_input)

            if user_year <= 0:
                raise ValueError("Please enter a positive integer.")

            if len(user_input) < 4:
                raise ValueError("Please enter a proper year.")
            
            if is_leap_year(user_year):
                print(f"{user_year} is a leap year.")
            else:
                closest_year = find_closest_leap_year(user_year)
                print(f"{user_year} is not a leap year. Closest leap year is: {closest_year}")
        
        except ValueError as e:
            if "positive" in str(e) or "proper" in str(e):
                print(f"Error: {e}")
            else:
                print("Error: please enter a valid integer.")

if __name__ == "__main__":
    main()

