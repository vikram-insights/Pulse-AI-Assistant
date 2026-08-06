import requests
import os
from dotenv import load_dotenv
from validation import validate_year, check_empty_string, validate_month


load_dotenv()
api_key = os.getenv("CALENDARIFIC_API_KEY")
url = "https://calendarific.com/api/v2/holidays"


#? 1. GET LIST OF INDIAN FESTIVALS BY YEAR
def get_indian_holidays(year):
    # 1. Validate year
    year_success, year_result = validate_year(year)
    if not year_success:
        return False, year_result

    # 2. Creating parameters
    params = {
        "api_key" : api_key,
        "country" : "IN",
        "year" : year_result
    }

    
    # 3. Get data from the API
    try:
        response = requests.get(url, params=params, timeout=3)
        response.raise_for_status()
        data = response.json()
        holidays = data["response"]["holidays"]
        return True, holidays
    except requests.RequestException:
        return False, "❌ Failed to fetch holiday data."



#? 2. FIND THE FESTIVAL BY NAME
def find_festival(year,name):
    # 1. Validate empty strings
    input_success, input_result = check_empty_string(year=year,name=name)
    if not input_success:
        return False, input_result

    # 2. Validate year and get the result from api
    year_success, holidays = get_indian_holidays(year)
    if not year_success:
        return False, holidays

    # 3. Get the list of the Indian festivals

    for holiday in holidays:
        if name.strip().lower() in holiday["name"].strip().lower():
            holiday_name = holiday["name"]
            date = holiday["date"]["iso"]
            return True, (holiday_name, date)
    else:
        return False, "❌ No holidays found with this name"


#? 3. LIST OF HOLIDAYS BY MONTH
def festivals_by_month(year, month):
    # 1. Validate month
    month_success, month_result = validate_month(month)
    if not month_success:
        return False, month_result

    # 2. Validate the year and get the result from the api
    year_success, holidays = get_indian_holidays(year)
    if not year_success:
        return False, holidays

    month_holidays = []

    for holiday in holidays:
        if holiday["date"]["datetime"]["month"] == month_result:
            holiday_name = holiday["name"]
            date = holiday["date"]["iso"]
            month_holidays.append({
                "name" : holiday_name,
                "date" : date
            })
        

    if month_holidays:
        return True, month_holidays
    return False, "❌ No holidays founda for this month"
        
    




    

    


    
