from datetime import date

def add_session():
    today = date.today()

    subject = input("What did you study? ")
    category = input("Category: ")
    minutes = input("How many minutes? ")

    session = f"{today} | {subject} | {category} - {minutes} mins\n"

    with open("sessions.txt", "a") as file:
        file.write(session)

    print("Session saved.\n")


def view_stats():
    print("\nStudy History:")

    total = 0
    session_count = 0
    longest_session = 0

    category_totals = {}

    with open("sessions.txt", "r") as file:
        for line in file:
            print(line.strip())

            parts = line.split(" | ")

            category_part = parts[2]
            category_name, time_part = category_part.split(" - ")

            mins = int(time_part.replace(" mins", "").strip())

            total += mins
            session_count += 1

            if mins > longest_session:
                longest_session = mins

            if category_name in category_totals:
                category_totals[category_name] += mins
            else:
                category_totals[category_name] = mins

    average = total / session_count

    print(f"\nTotal study time: {total} minutes")
    print(f"Total sessions: {session_count}")
    print(f"Average session length: {average:.1f} minutes")
    print(f"Longest session: {longest_session} minutes")

    print("\nCategory Totals:")

    for category, mins in category_totals.items():
        print(f"{category}: {mins} mins")

    print()


while True:
    print("=== Study Tracker ===")
    print("1. Add Study Session")
    print("2. View Statistics")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_session()

    elif choice == "2":
        view_stats()

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid option.\n")