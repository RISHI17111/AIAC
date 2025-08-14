import csv

input_file = 'students.csv'  # Change this to your CSV file path

with open(input_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print(f"{'Name':<20} {'Total':<10} {'Average':<10}")
    for row in reader:
        marks = [float(row['Subject1']), float(row['Subject2']), float(row['Subject3'])]
        total = sum(marks)
        average = total / 3
        print(f"{row['Name']:<20} {total:<10.2f} {average:<10.2f}")