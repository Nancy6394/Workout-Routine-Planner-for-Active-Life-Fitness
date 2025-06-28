import pandas as pd
from datetime import datetime

routines = {}
used_ids = set()

def generate_id():
    return f"ID{len(used_ids)+1:03d}"

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_routine():
    exercise = input("Enter exercise name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    while not is_valid_date(date):
        print("Invalid date format. Please enter in YYYY-MM-DD format.")
        date = input("Enter date (YYYY-MM-DD): ")
    try:
        reps = int(input("Enter number of reps: "))
    except ValueError:
        print("Reps must be an integer.")
        return

    routine_id = generate_id()
    while routine_id in used_ids:
        routine_id = generate_id()

    routines[routine_id] = {
        "exercise": exercise,
        "date": date,
        "reps": reps
    }
    used_ids.add(routine_id)
    print(f"\n✅ Routine {routine_id} added successfully.\n")

def view_routines():
    if routines:
        df = pd.DataFrame.from_dict(routines, orient='index')
        print("\n📋 Current Workout Routines:")
        print(df, "\n")
    else:
        print("\n⚠️ No routines found.\n")

def export_to_csv():
    if not routines:
        print("\n⚠️ No data to export.\n")
        return
    df = pd.DataFrame.from_dict(routines, orient='index')
    df.to_csv("workout_routines.csv")
    print("\n✅ Exported to workout_routines.csv\n")

def menu():
    while True:
        print("🏋️‍♂️ Workout Routine Planner")
        print("1. Add Routine")
        print("2. View Routines")
        print("3. Export to CSV")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_routine()
        elif choice == "2":
            view_routines()
        elif choice == "3":
            export_to_csv()
        elif choice == "4":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
menu()

