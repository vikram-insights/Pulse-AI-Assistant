#! 2. SHOW CUSTOME MONTH
def show_custome_month(year, month):
    current_date = datetime.now()
    month = current_date.month
    year = current_date.year
    custome_month_view = calendar.month(year, month)
    print(custome_month_view)


show_custome_month(1845, "July")

