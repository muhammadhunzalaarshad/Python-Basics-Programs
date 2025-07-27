from typing import List
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


def find_leap_years_in_range(start_year: int, end_year: int) -> List[int]:
    """
    Identify all leap years within a specified range.

    Args:
        start_year (int): The starting year of the range (inclusive).
        end_year (int): The ending year of the range (inclusive).

    Returns:
        List[int]: A list of leap years in the given range.
    """
    # Adjust start to the next multiple of 4 to optimize iteration
    start = start_year + (4 - start_year % 4)  if start_year % 4 != 0  else start_year
    leap_years = []
    # Iterate every 4 years to check for leap years
    for year in range(start, end_year + 1, 4):
        if is_leap_year(year):
            leap_years.append(year) 
    return leap_years

def main() -> None:
    """ Handle user input to find leap years in a specified range and display results."""
    while True:
        start_input = input("Enter a start year: {or 'q' to quit}: ").strip()
        if start_input.lower() == "q":
            print("Exiting program.")
            break

        end_input = input("Enter an end year: {or 'q' to quit}: ").strip()
        if end_input.lower() == "q":
            print("Exiting program.")
            break

        try:
            start_year = int(start_input)
            end_year = int(end_input)

            if start_year <= 0 or end_year <= 0:
                raise ValueError("Please enter positive integer.")
            
            if start_year > end_year:
                raise ValueError("Start year must be less than or equal to end year.")
            
            leap_year = find_leap_years_in_range(start_year, end_year)

            if leap_year:
                print(f"Leap years between {start_year} and {end_year} are: {leap_year}")
            else:
                print(f"No leap years found between {start_year} and {end_year}")
        except ValueError as e:
            if "positive" in str(e) or "less" in str(e):
                print(f"Error: {e}")
            else:
                print(f"Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()


    
