import datetime

def view_history():
    try:
        with open ('habit_log.txt', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("There is no history, log you first day.")
    else:
        print(content)

def habit_check():          # Creating an user defined function
    current_date = datetime.datetime.now()
    habit_dict = {}         # Creaing dictionary

    # Taking inputs and adding them to dictionary
    try:
        fajr_result = input("Did you pray Fajr on time? (yes/no): ").strip().lower()
        quran_recitation = int(input("How many minutes of Quran did you read?: "))
        workout = input("Did you move your body today? (yes/no): ").strip().lower()
        python = int(input("How many minutes did you study Python?: "))
        sentence = input("Write One sentence about your day: ")
    except ValueError:
        print("Invalid input. Please enter a number where required.")
    else:
        # For fajr
        if fajr_result == 'yes':
            habit_dict['Fajr salah'] = '✅'
        else:
            habit_dict['Fajr salah'] = '❌'
        
        # Quran
        habit_dict['Quran'] = quran_recitation

        # Workout
        if workout == 'yes':
            habit_dict['Workout'] = '✅'
        else:
            habit_dict['Workout'] = '❌'
        
        # Skill (Python)
        habit_dict['Python'] = python

        # Thought of the day
        habit_dict['Thought of day'] = sentence

        summary = (
        f"\nToday's activity is:\n"
        f"Fajr namaz: {habit_dict['Fajr salah']}\n"
        f"Today you read Quran for {habit_dict['Quran']} minutes.\n"
        f"Workout: {habit_dict['Workout']}\n"
        f"You worked on Python for {habit_dict['Python']} minutes.\n"
        f"Thought of the day is - {habit_dict['Thought of day']}\n"
        )

        print(summary)

        with open('habit_log.txt', 'a', encoding='utf-8') as file:
            file.write(str(current_date.date()))
            file.write(summary)
            file.write("---\n")

def choice():
    print("Welcome to our Digital habit tracker...\n")          # Welcome message
    while True:
        try:
            print("1. Log today\n2. View history\n3. Exit")
            user_choice = int(input("Please select an option from above given options: "))
        except ValueError:
            print("Please enter the option in integer form only.")
            continue
        else:
            if user_choice == 1:
                habit_check()
            elif user_choice == 2:
                view_history()
            elif user_choice == 3:
                print("Have a nice day, keep going on...")
                break
            else:
                print("Please select a valid option only.")

choice()