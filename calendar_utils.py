from datetime import datetime
import calendar
# calendar_utils.py
from validation import (
    check_empty_string,
    validate_year,
    validate_month,
    validate_day,
    validate_date,
    validate_date_string,
)

# ? ----------------------------- CALENDAR FEATURES -------------------------------


#! 1. SHOW CURRENT MONTH FUNCTION
def current_month():
    current_date = datetime.now()
    month = current_date.month
    year = current_date.year
    month_view = calendar.month(year, month)
    return month_view


#! 2. SHOW CUSTOM NONTH FUNCTION
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


#! 3. SHOW CUSTOME CALENDAR YEAR FUNCTION
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


#! 4. CHECK LEAP YEAR FUNCTION
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


#! 5. DAYS IN A MONTH
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


#! 6. SHOW DAY OF A GIVEN DATE
def show_weekday(year, month, day):
    # 1. Validate date
    success, actual_date = validate_date(year, month, day)
    if not success:
        return False, actual_date

    # 2. Generate result
    weekday_code = actual_date.weekday()
    day_name = calendar.day_name[weekday_code]
    month_name = calendar.month_name[actual_date.month]
    return True, f"The day for {actual_date.day} {month_name} {actual_date.year} is {day_name}."


#! 7. CHECK WEEKEND
def check_weekend(year, month, day):
    # 1. Validate date
    success, actual_date = validate_date(year, month, day)
    if not success:
        return False, actual_date

    # 2. Generate result
    weekday_code = actual_date.weekday()
    month_name = calendar.month_name[actual_date.month]
    if weekday_code in (5, 6):
        return True, f"{actual_date.day} {month_name} {actual_date.year} falls on a weekend."
    else:
        return True, f"{actual_date.day} {month_name} {actual_date.year} falls on a weekday."


#! 8. FIND DIFFERENCE BETWEEN TWO DATES
def date_difference(date1, date2):
    # 1. Validate date
    success1, date_1 = validate_date_string(date1)
    if not success1:
        return False, date_1

    success2, date_2 = validate_date_string(date2)
    if not success2:
        return False, date_2

    diff = date_2 - date_1
    days = abs(diff.days)
    return True, f"Difference between {date_1.strftime('%d %B %Y')} and {date_2.strftime('%d %B %Y')} is {days} days."
