import json
filename = "./data/Charater_Json"
def Choices():
    print ("Charater")
    print ("Data Management System")
    print ("(1) View Data")
    print ("(2) Add Data")
    print ("(3) Delete Data")
    print ("(4) Edit Data")
    print ("(5) Exit")

def view_data():
    with open (filename, "r") as f:
        temp = json.load(f)
        i = 0
        for entry in temp:
            name = entry["name"]
            gender = entry["gender"]
            narration = entry["narration"]
            print (f"Index Number {i}")
            print (f"Character name  : {name}")
            print (f"Character gender: {gender}")
            print (f"Narration type  : {narration}")
            print ("\n\n")
            i=i+1

def add_data():
    item_data = {}
    with open (filename, "r") as f:
        temp = json.load(f)
    item_data["name"] = input("Name charater: ")
    item_data["gender"] = input("gender of charater: ")
    item_data["narration"] = input("type of narration: ")
    temp.append(item_data)
    with open (filename, "w") as f:
        json.dump(temp, f, indent=4)

def delete_data():
    view_data()
    new_data = []
    with open (filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print ("Which index number would you like to delete?")
    delete_option = input(f"Select a number 0-{data_length}")
    i=0
    for entry in temp:
        if i == int(delete_option):
            pass
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
    with open (filename, "w") as f:
        json.dump(new_data, f, indent=4)

def edit_data():
    view_data()
    new_data = []
    with open (filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print ("Which index number would you like to delete?")
    edit_option = input(f"Select a number 0-{data_length}")
    i=0
    for entry in temp:
        if i == int(edit_option):
            name = entry["name"]
            gender = entry["gender"]
            narration = entry["narration"]
            print (f"Current Name of charater  : {name}")
            name = input("What would you like the new charater name to be? ")
            print (f"Current gender: {gender}")
            gender = input("What would you like the new gender to be? ")
            print (f"Current narration type  : {narration}")
            narration = input("What would you like the new narretion type to be? ")
            new_data.append({"name": name, "gender": gender, "narrattion": narration})
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
    with open (filename, "w") as f:
        json.dump(new_data, f, indent=4)

while True:
    Choices()
    choice = input("\nEnter Number: ")
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        delete_data()
    elif choice == "4":
        edit_data()
    elif choice == "5":
        break
    else:
        print ("You did not select a number, please read more carefully.")