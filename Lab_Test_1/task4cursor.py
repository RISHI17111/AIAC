import csv

# Take input for file name and student name
input_file = input("Enter the CSV file name: ")
search_name = input("Enter the student name: ")

found = False

try:
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Name'].strip().lower() == search_name.strip().lower():
                marks = [float(row['Subject1']), float(row['Subject2']), float(row['Subject3'])]
                total = sum(marks)
                average = total / 3
                print(f"Name: {row['Name']}")
                print(f"Total: {total:.2f}")
                print(f"Average: {average:.2f}")
                found = True
                break
        if not found:
            print("Student not found.")
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
