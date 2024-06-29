import datetime

# Initialize lists to store information
info_li = []
treatment_li = []
medicines = []
foods_to_eat = []
filename = []

# Get today's date
td = datetime.date.today()

# Input patient details
name = input("Name: ")
filename.append(name)  # Store name for filename

# Open file with patient name as filename
with open(f"{filename[0]}.txt", 'w') as file:
    age = input("Age: ")
    weight = input("Weight: ")
    address = input("Address: ")
    phone = input("Mobile: ")
    sex = input("Sex: ")
    illness = input("Illness in Brief: ")
    medical_history = input("Medical History: ")

    # Collect treatment explanation
    treatment_explain = input("Describe treatment and illness: ")
    treatment_li.append(treatment_explain)

    # Collect medicines
    while True:
        medicine = input("Enter name of Medicines Given (enter '/' to finish): ")
        if medicine == "/":
            break
        else:
            medicines.append(medicine)

    # Collect foods to eat
    while True:
        foods = input("Enter name of foods to eat most (enter '/' to finish): ")
        if foods == "/":
            break
        else:
            foods_to_eat.append(foods)

    # Collect special note
    note = input("Give Special Note: ")

    # Write collected information to file
    file.write(f"""
                ~~~~~~ FAITH HOSPITAL ~~~~~~
Phone: +91 987655432    Email: faith@hospital.com

Patient Details
Name: {name}       Age: {age}       Sex: {sex}
Weight: {weight}   Address: {address}
Phone: {phone}     Date: {td}
Illness: {illness}
Medical History: {medical_history}

About Illness:
{treatment_explain}

Medicines Given:
""")
    for med in medicines:
        file.write(f"- {med}\n")

    file.write("\nFoods to Eat:\n")
    for food in foods_to_eat:
        file.write(f"- {food}\n")

    file.write(f"\nNote: {note}\n")

    file.write("~~~~ Get Well Soon ~~~~")

    file.close()