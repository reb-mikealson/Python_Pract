import csv
employees=[
    ["Logan","20","Hockey Player"],
    ["Garret","21","Hockey Captain"],
    ["Dean","22","Hockey Coach"],
    ["Tucker","23","Hockey Trainer"]
]
file_path="C:\\Users\\Pratha\\OneDrive\\Desktop\\offCampus.csv"
try:
    with open(file_path, "w", newline="") as file:
        writer=csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print("Data written to the CSV file successfully.")
except FileExistsError:
    print("File already exists.")