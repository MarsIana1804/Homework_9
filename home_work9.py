
user_data = {"Marina" : "+1234567890"}

def hello_handler(*args):
    return "How can I help you?"

def add_handler(string_input):

    name = string_input[0].title()
    phone = string_input[1]
    #email = string_input[3]
    user_data[name] = phone
    return f"Contact {name} with phone {phone} has been saved!"

def get_phone_handler(string_input):
    name = string_input[0].title() 
    phone = user_data.get(string_input[0])
    if user_data.get(string_input[0]) != None:
        
        return f"Here is the phone number of contact {name}: {phone}."
    else:
        return f"User {string_input[0]} not found."

def change_handler(string_input):
    name = string_input[0].title()
    new_phone = string_input[1]
    user_data[name] = new_phone
    return f"Contact {name} has been changed to a new phone {new_phone}!"



def show_all_handler(*args):
    return user_data
    


def exit_handler(*args):
    return "Good bye!"

    
# def get_command(string_input):
#     command = string_input.split(" ")[0].lower()
#     return command




    print("An error occured:", e)







# def input_error(wrap):
#     def inner(*args):
#         try:
#             return wrap(*args)
             
#         except IndexError:
#             return "Give name and phone number please"
#     return inner





#@input_error

   
    # name_phone = {string_input.split(" ")[1].title(): string_input.split(" ")[2]}
    # user_data.update(name_phone)
    return f"Contact {name} with phone {phone} has been saved!"


commands = {
    add_handler: ["add", "додай", "+"],
    exit_handler: ["good bye", "close", "exit", "bye bye"],
    hello_handler: ["hello", "hi"],
    change_handler: ["change"],
    show_all_handler: ["show all"],
    get_phone_handler: ["phone"]
}

def command_parser(raw_str: str):
    elements = raw_str.split()
    for key, value in commands.items():
        for cmd in value:
            if cmd.startswith(elements[0].lower()):
                return key, elements[1:]
        if elements[0].lower() in value:
            return key, elements[1:]


#@input_error
def main():
    while True:
        user_input = input("Enter: ")
        if not user_input:
            continue
        cmd, data = command_parser(user_input)
        
        result = cmd(data)
        print(result)

        if cmd == exit_handler:
            break

        #print(user_data)


        # cmd = get_command(user_input)

        

        # elif cmd == "hello":
        #     print("How can I help you?")

        # elif user_input.lower() == "show all":
        #     print(user_data)

        

        # elif cmd == "add":
        #     add(user_input)

        # elif cmd == "change":
        #     change(user_input)        

        # elif cmd == "phone":
        #     get_phone(user_input)

        
    



if __name__ == "__main__":
        
        main()



