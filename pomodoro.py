import time
from datetime import datetime

def start_pomodoro(hours, minutes):
    # Reject negative numbers
    if hours < 0 or minutes < 0:
        return False, "❌Duration cannot be negative"

    # Reject minutes greater than 59
    if minutes > 59:
        return False, "❌Minutes should be between 0 and 59!"

    # Reject empty/zero timer
    if hours == 0 and minutes == 0:
        return False, "❌Timer duration must be greater than 0! "


    # Calculate total seconds
    total_seconds = (hours * 3600) + (minutes * 60)
    return True, total_seconds


def countdown(total_seconds):
    while total_seconds > 0:
        # Converting total seconds in hours, minutes & seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        # To display hours, minutes & seconds
        print(f"\rTimer : {hours:02d}:{minutes:02d}:{seconds:02d}", end="")
        # To wait 1 second
        time.sleep(1)
        # Decreasing 1 from total seconds every iteration
        total_seconds -= 1
    print()
    print("\n🍅 Pomodoro Completed!")
    # To display completed time
    print(f"Completed At : {datetime.now().strftime('%d %B, %Y %I:%M %p')}")
    
