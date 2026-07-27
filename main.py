from datetime_utils import get_datetime
from apis import get_weather, get_coordinates, get_bitcoin_price, convert_currency
from calculator import add, subtract, multiplication, division, modulus, get_power
from datetime import datetime
from webs_utils import open_website
from reminder_utils import add_reminder, save_reminders, load_reminders, delete_reminder, view_reminders,update_reminder

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
        print("7. Reminder")
        print("8. Exit")
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
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            source = input("Enter source currency (e.g., INR) : ").upper().strip()
            target = input("Enter target currency (e.g., USD) : ").upper().strip()

            result = convert_currency(amount, source, target)

            #! Print only if conversion was successful
            if result is not None:
                print("-" * 30)
                print(f"{amount} {source} = {result:.2f} {target}") 
                print("-" * 30)       


            

        elif choice == 6:
            while True:
                print("======== MENU ========")
                print("1. YouTube")
                print("2. Google")
                print("3. LeetCode")
                print("4. GitHub")
                print("5. Instagram")
                print("6. Vikram's Instagram")
                print("7. Muskan's Instagram")
                print("8. Custom URL")
                print("9. Swiggy")
                print("10. Exit")
                print("=" * 22)

                choice = input("Choice (1-10): ").strip()

                if choice == "1":
                    open_website("youtube")
                elif choice == "2":
                    open_website("google")
                elif choice == "3":
                    open_website("leetcode")
                elif choice == "4":
                    open_website("github")
                elif choice == "5":
                    open_website("instagram")
                elif choice == "6":
                    open_website("vikram")
                elif choice == "7":
                    open_website("muskan")
                elif choice == "8":
                    custom_url = input("\nEnter custom URL: ")
                    open_website(custom_url)
                elif choice == "9":
                    open_website("swiggy")
                elif choice == "10":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice!")

        elif choice == 7:
            while True:
                print("========== REMINDER =========")
                print("1. Add  Reminder")
                print("2. View Reminder")
                print("3. Delete Reminder")
                print("4. Update Reminder")
                print("5. Back")
                print("=" * 30)

                try:
                    rem_choice = int(input("Enter choice (1-5): "))
                except ValueError:
                    print("Invalid choice! Please select between (1-5).")
                    continue

                if rem_choice == 5:
                    print("Goodbye.")
                    break  


                
                

                if rem_choice == 1:
                    task = input("What is the task? : ")
                    if not task:
                        print("Task cannot be empty❗")
                        continue
                    
                    try:
                        date = input("Enter Date (DD-MM-YYYY): ")
                        actual_date = datetime.strptime(date, "%d-%m-%Y")
                    except ValueError as e:
                        print("Invalid date format! Please use (DD-MM-YYYY)")
                        continue
                                    
                    try:
                        time = input("Enter Time (HH:MM): ")
                        actual_time = datetime.strptime(time, "%H:%M")
                    except ValueError as e:
                        print("Invalid time format!\nPlease use (HH:MM)")
                        continue
                    
                    add_reminder(task, actual_date.strftime("%d-%m-%Y"), actual_time.strftime("%H:%M"))
                    print("Reminder set successfully✅.")

                elif rem_choice == 2:
                    reminders = view_reminders()
                    if reminders:
                        for index, reminder in enumerate(reminders, start=1):
                            print("=" * 30)
                            print("Reminders loaded successfuly✅.")
                            print("=" * 30)
                            print(f"Reminder {index}")
                            print(f"Task : {reminder['title']}")
                            print(f"Date : {reminder['date']}")
                            print(f"Time : {reminder['time']}")
                            print("=" * 30)
                            
                
                    else:
                        print("No reminder found!")

                elif rem_choice == 3:
                    try:
                        number = int(input("Enter reminder number : "))
                    except ValueError as e:
                        print("Invalid number: ")
                        continue
                    result = delete_reminder(number)
                    print("Reminder deleted successfully✅.")

                elif rem_choice == 4:
                    try:
                        index = int(input("Entre reminder number : "))

                    except ValueError as e:
                        print("Invlaid input!")
                        continue
                    task = input("Please leave blank to keep previous task : ")
                    data = input("Enter Date (DD-MM-YYYY) OR Leave blank to keep previous date : ")
                    time = input("Enter Date (HH:MM) OR Leave blank to keep previous time : ")

                    result = update_reminder(index, task, data, time)
                    print("-" * 50)
                    print(result)
                    print("-" * 50)
                   
                    
        

                    



        elif choice == 8:
            print("-" * 30)
            print("Thank you for using Pulse.")
            print("Goodbye!")
            print("-" * 30)
            break
        
        else:
            print("Invalid Input!")
            print("Please select choice between 1-8.")

    
if __name__ == "__main__":
    main()
