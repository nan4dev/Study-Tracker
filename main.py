subject = input("What did you study? ")
minutes = input("How many minutes? ")

session = f"{subject} - {minutes} mins\n"

with open("sessions.txt", "a") as file:
    file.write(session)

print("Session saved.")