from datetime_utils import get_datetime
from apis import get_weather, get_coordinates, get_bitcoin_price
from calculator import add, subtract, multiplication, division, modulus, get_power
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
            
            while True:
                print("=" * 20)
                print("CALCULATOR")
                print("=" * 20)

                print("1. Add")
                print("2. Subtract")
                print("3. Multiplication")
                print("4. Division")
                print("5. Modulus")
                print("6. Power")
                print("7. Exit")

                try:
                    calc_choice = int(input("Enter your choice between (1-7) : "))
                except ValueError:
                    print("Error! Please enter valid choice.")
                    continue

                if calc_choice == 7:
                    print("Thank you for using calculator.")
                    break

                if calc_choice < 1 or calc_choice > 7:
                    print("Invalid choice input!")
                    print("Please select between (1-7).")
                    continue
                
                number = input("Enter numbers separated by spaces (e.g. 10 20 30) : ")

                if calc_choice == 1: 
                    try:
                        num_list = [float(num) for num in number.split()]
                        if num_list:
                            result = add(num_list)
                            print(f"Numbers entered: {num_list} ")
                            print(f"Total Sum : {result}")
                        else:
                            print("0 numbers entered.")

                    except ValueError:
                        print("Error!")
                        print("Please enter numbers only.")
                

                elif calc_choice == 2: 
                    try:
                        num_list = [float(num) for num in number.split()]
                        if num_list:
                            result = subtract(num_list)
                            print(f"Numbers entered: {num_list} ")
                            print(f"Subtraction Result : {result}")
                        else:
                            print("0 numbers entered.")
                
                    except ValueError:
                        print("Error!")
                        print("Please enter numbers only.")

                elif calc_choice == 3: 
                    try:
                        num_list = [float(num) for num in number.split()]
                        if num_list:
                            result = multiplication(num_list)
                            print(f"Numbers entered: {num_list} ")
                            print(f"Multiplication Result : {result}")
                        else:
                            print("0 numbers entered.")
                                
                    except ValueError:
                        print("Error!")
                        print("Please enter numbers only.")


                elif calc_choice == 4: 
                    try:
                        num_list = [float(num) for num in number.split()]
                        if num_list:
                            result = division(num_list)
                            print(f"Numbers entered: {num_list} ")
                            print(f"Division Result : {result:.2f}")
                        else:
                            print("0 numbers entered.")
                                                
                    except ValueError:
                        print("Error!")
                        print("Please enter numbers only.")


                elif calc_choice == 5: 
                    try:
                        num_list = [float(num) for num in number.split()]
                        if num_list:
                            result = modulus(num_list)
                            print(f"Numbers entered: {num_list} ")
                            print(f"Modulus Result : {result}")
                        else:
                            print("0 numbers entered.")
                                                                
                    except ValueError:
                        print("Error!")
                        print("Please enter numbers only.")


                elif calc_choice == 6: 
                    try:
                        num_list = [float(num) for num in number.split()]
                        power = int(input("Enter power (e.g 1, 2 10) : "))
                                         
                        if num_list:
                            result = get_power(num_list, power)
                                
                            print(f"Numbers entered: {num_list} ")
                            print(f"Power result respectively : {result}")
                        else:
                            print("0 numbers entered.")
                                                                
                    except ValueError:
                        print("Error!")
                        print("Please enter numbers only.")

                
                                
                                
                                                
                                
                
                

            

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
