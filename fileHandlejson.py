#in json file key value pairs are stored , Lets learn it .
import json
employee={
    "employee_Name":"Edward",
    "employee_ID":1234,
    "employee_Work":"AI Engineer"
}
file_path="C:\\Users\\Pratha\\OneDrive\\Desktop\\employee_data.json"
try:
    with open(file_path,"w") as file:
        json.dump(employee,file,indent=3)
        print("file was created successfully")
except FileExistsError:
    print("File already exists")