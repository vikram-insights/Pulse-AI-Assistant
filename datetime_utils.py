from datetime import datetime



def get_datetime():
    today = datetime.now()
    current_date = today.strftime('%d-%b-%Y')
    current_time = today.strftime('%H:%M:%S')
    return current_date, current_time
    

