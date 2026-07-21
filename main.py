from datetime_utils import get_datetime
from apis import get_weather, get_coordinates, get_bitcoin_price
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
            user_city = input("entr city name: ")
            lat, lon = get_coordinates(user_city)
            weather = get_weather(lat, lon)
            
            
            if weather is not None:
                
                temperature, temperature_unit, humidity, humidity_unit, wind_speed, wind_speed_unit = weather
                print("=" * 25)
                print(user_city)
                print("="* 25)
                print(f"Temperature : {temperature} {temperature_unit}")
                print(f"Humidity : {humidity} {humidity_unit}")
                print(f"Wind Speed : {wind_speed} {wind_speed_unit}")
            else:
                print("Error! City not found.")



        
                
        elif choice == 3:
            bitcoin_price = get_bitcoin_price()
            print(f"Current Price : $ {bitcoin_price}")

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
