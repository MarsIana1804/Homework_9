
user_data = {"Marina" : "+1234567890"}

def exit():
    print("Good bye!")
    
def get_command(string_input):
    command = string_input.split(" ")[0].lower()
    return command

def add(string_input):

    try:
        new_pair = {string_input.split(" ")[1]: string_input.split(" ")[2]}
        user_data.update(new_pair)

    except Exception as e:
        print("An error occured:", e)


def change(string_input):
    user_data[string_input.split(" ")[1]] = string_input.split(" ")[2]

def get_phone(string_input):
    if user_data.get(string_input.split(" ")[1]) != None:
        print(string_input.split(" ")[1], user_data.get(string_input.split(" ")[1]))
    else:
        print(f"User {string_input.split(' ')[1]} not found.")




def bot():

    while True:

        user_input = input("Hello! ")
        cmd = get_command(user_input)

        if cmd in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        elif cmd == "hello":
            print("How can I help you?")

        elif user_input.lower() == "show all":
            print(user_data)

        

        elif cmd == "add":
            add(user_input)

        elif cmd == "change":
            change(user_input)        

        elif cmd == "phone":
            get_phone(user_input)

        
    



if __name__ == "__main__":
        
        bot()



