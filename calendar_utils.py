import calendar
from datetime import datetime

#! 1. SHOW CURRENT MONTH FUNCTION
def current_month():
    current_date = datetime.now()
    month = current_date.month
    year = current_date.year
    month_view = calendar.month(year, month)
    return month_view


#! 2. VALIDATING YEAR
def validate_year(year):
    """
    Validates and parses a year input.
    Returns (True, year) if valid, otherwise (False, error message).
    """

    # 1. Remove extra spaces
    cleaned_year = year.strip()

    # 2. Check empty strings
    if not cleaned_year:
        return False, "Year cannot be empty!"

    # 3. Checks float value
    elif "." in cleaned_year:
        return False, "Year cannot be a float value! "

    else:
        try:
            # 4. Convert string into integer
            final_year = int(cleaned_year)
            # 5. Validate year should not be less than 0
            if final_year < 1:
                return False, "Year must be a positive number!"
            else:
                # 6. Return year on success
                return True, final_year
        except ValueError:
            return False, "Year must be a number!"


#! 3. VALIDATING MONTH
def validate_month(month):
    # 3. Validate month
    if isinstance(month, str):
        cleaned_month = month.strip()

        if not cleaned_month:
            return False, "Error! Month cannot be empty."

        # If month is entered as a number in string form
        if cleaned_month.isdigit():
            month_num = int(cleaned_month)

            if not 1 <= month_num <= 12:
                return False, "Error! Month should be between 1 and 12."

        # If month is entered as a name
        else:
            try:
                month_num = datetime.strptime(cleaned_month, "%B").month
            except ValueError:
                try:
                    month_num = datetime.strptime(cleaned_month, "%b").month
                except ValueError:
                    return False, f"Error! '{month}' is not a valid month."

    # If month is entered as an integer
    elif isinstance(month, float):
        return False, "Month cannot be a float value"

    elif isinstance(month, int):
        if 1 <= month <= 12:
            month_num = month
        else:
            return False, "Error! Month should be between 1 and 12."

    else:
        return False, "Error! Wrong month type."

    return True, month_num


#! 4. SHOW CUSTOM NONTH FUNCTION
def show_custom_month(year, month):
    # 1. Check empty inputs
    if not year and not month:
        return False, "Error! Both year and month are missing."

    if not year:
        return False, "Error! Year is missing."

    if not month:
        return False, "Error! Month is missing."

    # 2. Validate year
    year_success, year_result = validate_year(year)
    if not year_success:
        return False, year_result  # Return the error message from helper

    # 3. Validate month
    month_success, month_result = validate_month(month)
    if not month_success:
        return False, month_result  # Return the error message from helper

    # 4. Generate calendar
    result = calendar.month(year_result, month_result)
    return True, result


#! 5. SHOW CUSTOME CALENDAR YEAR FUNCTION
def show_custom_year(year):
    if year == "":
        return False, "Year cannot be empty!"
    

    # 1. Validate Year
    year_success, year_result = validate_year(year)
    if not year_success:
        return False, year_result

    # 2. Generate Calendar
    result = calendar.calendar(year_result)
    return True, result
