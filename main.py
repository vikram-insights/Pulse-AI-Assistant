from datetime_utils import get_datetime
from datetime import datetime
def main():
    
    while True:
        print("=" * 25)
        print("PULSE AI ASSISTANT")
        print("=" * 25)

        print("1. Current Date & Time")
        print("2. Weather")
        print("3. Bitcoin Price")
        print("4. Calculator")
        print("5. Currency Converter")
        print("6. Open Website")
        print("7. Exit")
        print("=" * 25)
    
        try:
            choice = int(input("Enter your choice :  "))
        
        except ValueError:
            print("Error! Please enter valid input.")
            continue


        if choice == 1:
            current_date, current_time = get_datetime()
            print(f"Date : {current_date}")
            print(f"Time : {current_time}")
        elif choice == 2:
            print("Weather Selected")
        elif choice == 3:
            print("Bitcoin Price Selected")
        elif choice == 4:
            print("Calculator Selected")
        elif choice == 5:
            print("Currency Converter Selected")
        elif choice == 6:
            print("Open Website Selected")
        elif choice == 7:
            print("Thank you for using Pulse.")
            print("Goodbye!")
            break
        else:
            print("Invalid Input!")
            print("Please select choice between 1-7.")
    
    
    
    
    
    
    
   
if __name__ == "__main__":
    main()
