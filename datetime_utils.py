from datetime import datetime



def get_datetime():
    # 1. Fecth  the today's date and time
    today = datetime.now()

    # 2. Converts the date in desired format
    current_date = today.strftime('%d-%b-%Y')

    # 3. Converts the date in desired format
    current_time = today.strftime('%H:%M:%S')

    return current_date, current_time
    

