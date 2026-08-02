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
            # 5. Validate year is a positive number
            if final_year < 1:
                return False, "Year must be a positive number!"
            else:
                # 6. Return year on success
                return True, final_year
        except ValueError:
            return False, "Year must be a number!"


#! 3. VALIDATING MONTH
def validate_month(month):
    # Validate month
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


#! 4. EMPTY STRING INPUT VALIDATION
def check_empty_string(**kwargs):

    """Validates that required string inputs are not empty."""

    # 1. Check empty inputs
    missing_fields = []

    # Collect all empty string
    for key, value in kwargs.items():
        if value.strip() == "":
            missing_fields.append(key.capitalize())

    total_missing = len(missing_fields)

    # 2. Handle the result
    if total_missing == 0:
        return True, None

    if total_missing == 1:
        return False, f"{missing_fields[0]} is missing!"

    elif total_missing == 2:
        return False, f"{missing_fields[0]} and {missing_fields[1]} are missing!"

    else:
        # Separate all the items except the last one with commas
        main_part = ", ".join(missing_fields[:-1])
        # Get the very last item
        last_item = missing_fields[-1]
        return False, f"{main_part} and {last_item} are missing!"


#! 5. SHOW CUSTOM NONTH FUNCTION
def show_custom_month(year, month):

    # 1. Check empty inputs
    input_success, input_result = check_empty_string(year=year, month=month)
    if not input_success:
        return False, input_result
    
    

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


#! 6. SHOW CUSTOME CALENDAR YEAR FUNCTION
def show_custom_year(year):

    # 1. Validate empty strings
    year_success, year_result = check_empty_string(year=year)
    if not year_success:
        return False, year_result
    

    # 2. Validate Year
    year_success, year_result = validate_year(year)
    if not year_success:
        return False, year_result

    # 3. Generate Calendar
    result = calendar.calendar(year_result)
    return True, result


#! 7. CHECK LEAP YEAR FUNCTION
def check_leap_year(year):
    # 1. Validate empty strings
    year_success, year_result = check_empty_string(year=year)
    if not year_success:
        return False, year_result


    # 2. Validate year
    year_success, year_result = validate_year(year)
    if not year_success:
        return False, year_result
    # 3. Check leap year
    result = calendar.isleap(year_result)
    if result:
        return True, f"{year_result} is a leap year."
    else:
        return False, f"{year_result}  is not leap year."


#! 8. DAYS IN A MONTH
def days_in_month(year, month):
    # 1. Validate empty strings
    input_success, input_result = check_empty_string(year=year, month=month)
    if not input_success:
        return False, input_result


    # 2. Validate year
    year_success, year_result = validate_year(year)
    if not year_success:
        return False, year_result

    # 3. Validate month
    month_success, month_result = validate_month(month)
    if not month_success:
        return False, month_result 

    # 4. Generate calendar
    result = calendar.monthrange(year_result, month_result)
    return True, f"{calendar.month_name[month_result]} {year_result} has {result[1]} days." 



#! 9. VALIDATE DAY HELPER FUNCTION
def validate_day(day):
    """
        Validates and parses a day input.
        Returns (True, Day) if valid, otherwise (False, error message).
    """
    
    # 1. Remove extra spaces
    cleaned_day = day.strip()
    
    # 2. Check empty strings
    if not cleaned_day:
        return False, "Day cannot be empty!"
    
    # 3. Checks float value
    elif "." in cleaned_day:
        return False, "Day cannot be a float value! "
    
    else:
        try:
            # 4. Convert string into integer
            final_day = int(cleaned_day)
                # 5. Validate day is a positive number
            if final_day < 1:
                return False, "Day must be a positive number!"
            else:
                # 6. Return day on success
                return True, final_day
        except ValueError:
            return False, "Day must be a number!"



        
#! 10. SHOW DAY OF A GIVEN DATE
def show_weekday(year, month, day):
    # 1. Validate empty strings
    input_success, input_result = check_empty_string(
        year=year, month=month, day=day
    )

    if not input_success:
        return False, input_result

    # 2. Validate year
    year_success, year_result = validate_year(year)
    if not year_success:
        return False, year_result
    
    # 3. Validate month
    month_success, month_result = validate_month(month)
    if not month_success:
        return False, month_result 

    # 4. Validate day
    day_success, day_result = validate_day(day)
    if not day_success:
        return False, day_result

    try:
        actual_date = datetime(year_result, month_result, day_result)
        weekday_code  = actual_date.weekday()
        day_name = calendar.day_name[weekday_code]
        month_name = calendar.month_name[month_result]
        return True, f"The day for {day_result} {month_name} {year_result} is {day_name}."
    except ValueError:
        return False, "Invalid date!"


    
    



