import requests
from validation import validate_year



api_key = "dYjYDbsHdEYnaPfFtzd955l5NesyI0gb"
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
