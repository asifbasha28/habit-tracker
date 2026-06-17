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
    habit_dict = {}         # Creating dictionary

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
    print("Welcome to our Digital habit tracker...")          # Welcome message
    while True:
        try:
            print("\n1. Log today\n2. View history\n3. View stats\n4. Exit")
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
                view_stats()
            elif user_choice == 4:
                print("Have a nice day, keep going on...")
                break
            else:
                print("Please select a valid option only.")


def view_stats():
    try:
        with open('habit_log.txt', 'r', encoding='utf-8') as file:
            content = file.read().split('---')
            fajr_count = 0
            workout_count = 0
            quran_minutes = 0
            python_minutes = 0
            for day in content:
                activities = day.split('\n')
                # Yes or No
                for activity in activities:
                    if 'Fajr namaz: ✅' in activity:
                        fajr_count += 1
                    elif 'Workout: ✅' in activity:
                        workout_count += 1
                    elif 'Quran' in activity:
                        words = activity.split()
                        quran_minutes += int(words[5])
                    elif 'Python' in activity:
                        words = activity.split()
                        python_minutes += int(words[5])

            total_days = len(content) - 1
            avg_quran_mins = round(quran_minutes / total_days, 1)
            avg_python_mins = round(python_minutes / total_days, 1)
    except FileNotFoundError:
            print("There is no history, log you first day.")
    except ZeroDivisionError:
         print("No history exists, log your first day")
    else:
            if total_days == 1:
                print(f"You showed up for {total_days} day")
            else:
                print(f"You showed up for {total_days} days")        

            if fajr_count == 1:
                print(f"You prayed Fajr for {fajr_count} day")
            else:
                print(f"You prayed Fajr for {fajr_count} days")

            if workout_count == 1:
                print(f"You did workout for {workout_count} day")
            else:
                print(f"You did workout for {workout_count} days")   

            print(f"You read Quran for {avg_quran_mins} mins/day")             
            print(f"You worked on Python for {avg_python_mins} mins/day")             

choice()