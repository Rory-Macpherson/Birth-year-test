from datetime import date

# Get name
name = input("What is your name? ")


while True:
    try:
        age = int(input("How old are you? "))
        if 0 <= age <= 120:  # reasonable age check
            break
        else:
            print("Please enter a realistic age between 0 and 120.")
    except ValueError:
        print("Please enter a number, not text.")

# Get birth month
while True:
    try:
        birth_month = int(input("What month were you born? (1-12) "))
        if 1 <= birth_month <= 12:
            break
        else:
            print("Please enter a month between 1 and 12.")
    except ValueError:
        print("Please enter a number, not text.")

# Get birth day safely
while True:
    try:
        birth_day = int(input("What day were you born? (1-31) "))
        # Simple check for day range
        if 1 <= birth_day <= 31:
            break
        else:
            print("Please enter a valid day (1-31).")
    except ValueError:
        print("Please enter a number, not text.")

# Calculate birth year
today = date.today()
birth_year = today.year - age

# Adjust if birthday hasn't happened yet this year
if (today.month, today.day) < (birth_month, birth_day):
    birth_year -= 1

print(f"Hello {name}, you were born in {birth_year}!")
