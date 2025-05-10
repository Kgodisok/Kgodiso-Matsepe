#Matsepe Kgodiso
# 2025 May 10
array_of_month = [None, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
array_of_day = ["st", "nd", "rd","th"]
CURRENT_YEAR = 2025
CURRENT_MONTH = 5
CURRENT_DAY = 6
class Bday:
    def year():
        while True:
            try:
                the_year = int(input("Enter Year: "))
                return the_year
            except ValueError:
                print("The year must be in numbers only.")



    def month():
        while True:
            try:
                the_month = int(input("Enter the month in numbers: "))
                if the_month < 1 or the_month > 12:
                    print("Month must be between (1 AND 12). ")
                else:
                    return the_month
            except ValueError:
                print("The Month must be in numbers only.")



    def day():
        while True:
            try:
                the_day = int(input("Enter day in numbers: "))
                if the_day < 1 or the_day > 31:
                    print("Day must be between (1 AND 31).")
                else:
                    return the_day
            except ValueError:
                print("The day must be in numbers only.")



    def daying(the_day):
        if the_day == 1 or the_day == 21 or the_day == 31:
            return f"{str(the_day) + str(array_of_day[0])}"
        elif the_day  == 2 or the_day == 22:
            return f"{str(the_day) + str(array_of_day[1])}"
        elif the_day == 3 or the_day == 23:
            return f"{str(the_day) + str(array_of_day[2])}"
        else:
            return f"{str(the_day) + str(array_of_day[3])}"



    def monthing(the_month):
        return f"{array_of_month[the_month]}"



    def age(the_year, the_month, the_day):
        if the_day == CURRENT_DAY and the_month == CURRENT_MONTH:
                return f"{CURRENT_YEAR - the_year}"
        else:
            return f"{CURRENT_YEAR - 1 - the_year}"


    the_year = year()
    the_month = month()
    the_day = day()
    my_day = daying(the_day)
    my_month = monthing(the_month)
    aging = age(the_year, the_month, the_day)
    print(f"You were born on the {my_day} {my_month} {the_year} and you are {aging}.")