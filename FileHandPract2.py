txt_data="I like Ghevar and Rasmalai"
file_path="C:\\Users\\Pratha\\OneDrive\\Desktop\\sweets.txt"
with open(file_path,"w") as file:
    file.write(txt_data+"\n")
    print("Data written to the file successfully.")