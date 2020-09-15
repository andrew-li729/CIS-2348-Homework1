# Andrew Li
# 1824794

print("Birthday Calculator")
print("Please enter all values numerically.\n")


current_day = int(input("Enter current day: "))      # asks user for date input and converts to int
current_month = int(input("Enter current month: "))
current_year = int(input("Enter current year: "))

print("Current day: {1}/{0}/{2}\n".format(current_day, current_month, current_year))  # prints date more readably

birth_day = int(input("Enter birth day: "))        # asks for inputs like above, but for birthday
birth_month = int(input("Enter birth month: "))
birth_year = int(input("Enter birth year: "))

print("Birthday: {1}/{0}/{2}\n".format(birth_day, birth_month, birth_year))

age = 0  # initializes age

if current_month <= birth_month:  # checks if birthday has passed compared to current day
    if current_day < birth_day:   # if the current month and day is before birthday, user has not aged a full year
        age = (current_year - birth_year) - 1  # program "rounds down" age to last fully completed year
    else:
        age = current_year - birth_year  # age

print("You are", age, "years old.")  # prints age

if current_day == birth_day and current_month == birth_month:  # if month and day match, it is user's birthday
    print("Happy Birthday!")
