
user_data = {"Marina" : "+1234567890"}
result = None

def input_error(wrap):
    def inner(*args):
        try:
            return wrap(*args)
        except IndexError:
            if len(*args) == 0:
                print("Enter user name")
            elif len(*args) == 1:
                print("Enter BOTH user name and phone number")
        except KeyError as k_e:
            print(k_e)
        except ValueError as v_e:
            print(v_e)

        except Exception as e:
            print(e)
            #return "Give name and phone number please"
    return inner

def hello_handler(*args):
    return "How can I help you?"


def add_handler(string_input):

    if string_input[0].isdigit():
        print("KeyError")
        raise KeyError("Number instead of name has been provided.Please enter the correct value.")
    elif string_input[1].isalpha():
        raise ValueError("Text instead of number has been provided.Please enter the correct phone number.")

    name = string_input[0].title()
    phone = string_input[1]
    #email = string_input[3]
    user_data[name] = phone
    return f"Contact {name} with phone {phone} has been saved!"

def get_phone_handler(string_input):

    if string_input[0].isdigit():
        #print("KeyError")
        raise KeyError("Number instead of name has been provided. Please enter the correct value.")
    elif string_input[1].isalpha():
        raise ValueError("Text instead of number has been provided.Please enter the correct phone number.")
    name = string_input[0].title() 
    phone = user_data.get(name)
    if user_data.get(name) != None:
        
        return f"Here is the phone number of contact {name}: {phone}."
    else:
        return f"User {name} not found."

def change_handler(string_input):
    if string_input[0].isdigit():
        #print("KeyError")
        raise KeyError("Number instead of name has been provided.Please enter the correct value.")
    elif string_input[1].isalpha():
        raise ValueError("Text instead of number has been provided.Please enter the correct phone number.")
    name = string_input[0].title()
    new_phone = string_input[1]
    user_data[name] = new_phone
    return f"Contact {name} has been changed to a new phone {new_phone}!"



def show_all_handler(*args):
    return user_data
    


def exit_handler(*args):
    return "Good bye!"




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
    try:
        for key, value in commands.items():
            for cmd in value:
                if cmd.startswith(elements[0].lower()):
                    return key, elements[1:]
            if elements[0].lower() in value:
                return key, elements[1:]
    except Exception as e:
        print(e)


def main():
    while True:
        user_input = input("Enter: ")
        if not user_input:
            continue
        try:
            cmd, data = command_parser(user_input)
            result = input_error(cmd)(data)
            if result != None:
                print(result)

            if cmd == exit_handler:
                break


        except Exception as e:
            result = None
            print("Enter the correct command.")

        
    


if __name__ == "__main__":
        
        main()



