FILENAME = 'book.txt'


def read_phonebook():
    try:
        with open(FILENAME, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return[]
    # return[]





def save_phonebook(phonebook):
    with open(FILENAME, 'w') as file:
        # for entry in phonebook:
            file.write(f"{phonebook}\n")
    print("Save file.")



def display_phonebook():
    for list in read_phonebook():
        print(list)



def save_book(phonebook):
    return


def validate_number(phone_number:str):
    return phone_number.isdigit() and len(phone_number) != 9


def add_entry(name, phone_number:str):
    if not phone_number.isdigit() or len(phone_number) !=9:
        print("Invalid phone number.")
        return
    add_new = f"{name}; {phone_number}"
    save_phonebook(add_new)
    print("Added phone number.")


def remove_entry(phone_number):
    save_phonebook ([entry for entry in read_phonebook() if phone_number not in entry])


def modify_entry(old_phone_number, new_name, new_phone_number):
    if validate_number(new_phone_number):
        print("Invalid phone number.")
        return False
    lista = read_phonebook()
    for key, row in enumerate(lista):
        if old_phone_number in row:
            lista [key] = f"{new_name}; {new_phone_number}"
            save_phonebook(lista)
            print("Save")
            return True
    return 




read_phonebook()
add_entry("Orest", "123456789")
display_phonebook()
modify_entry("123456789", "Ania", "000000000")
remove_entry("123456789")
display_phonebook()



while True:
    print("0. Exit")

    choice = input("Enter your choice:")

    if choice == "0":
        print("Exit")
        break


    