subject = input("What did you study? ")
minutes = input("How many minutes? ")

session = f"{subject} - {minutes} mins\n"

with open("sessions.txt", "a") as file:
    file.write(session)

print("\nStudy History:")

total = 0

with open("sessions.txt", "r") as file:
    for line in file:
        print(line.strip())

        parts = line.split(" - ")
        time_part = parts[1]

        mins = int(time_part.replace(" mins\n", ""))
        total += mins

print(f"\nTotal study time: {total} minutes")