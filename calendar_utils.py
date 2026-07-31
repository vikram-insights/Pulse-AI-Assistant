import calendar
from datetime import datetime

#! 1. SHOW CURRENT MONTH FUNCTION
def current_month():
    current_date = datetime.now()
    month = current_date.month
    year = current_date.year
    month_view = calendar.month(year, month)
    return month_view



#! 2. SHOW CUSTOM MONTH
def show_custom_month(year, month):

    # 1. Check empty inputs
    if not year and not month:
        return False, "Error! Both year and month are missing."

    if not year:
        return False, "Error! Year is missing."

    if not month:
        return False, "Error! Month is missing."

    # 2. Validate year
    if isinstance(year, float):
        return False, "Error! Year cannot be a float value"

    if year < 1:
        return False, "Error! Year must be positive."
    
    if not isinstance(year, int):
        return False, "Error! Year must be a number."



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
    elif isinstance(month, int):
        if 1 <= month <= 12:
            month_num = month
        else:
            return False, "Error! Month should be between 1 and 12."

    else:
        return False, "Error! Wrong month type."

    # 4. Generate calendar
    result = calendar.month(year, month_num)

    return True, result
