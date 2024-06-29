#  Copyright (c) 2024. Sergii Nechuiviter
import requests


def print_help():
    print("You can type your message and press Enter to send it.")
    print("")
    print("If you start your message with '`' character, you can use some commands.")
    print("You can type '`h' and press Enter to see the help.")
    print("You can type '`q' and press Enter to quit the application.")
    print("You can try to enter '`' and your command in natural language for other system commands.")
    print("")


def process_user_message(message: str):
    return (f'You said: {message}\n'
            f'    Ok...')


def process_command(message: str):
    return (f'Command: {message}\n'
            f'    Command is not supported yet.')


if __name__ == "__main__":
    # Print invitation message
    print("Hello, this is a simple chat application.")
    print("")
    print_help()

    # Main processing loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to quit
        if user_input == '`q':
            break

        # Check if user wants to see help
        if user_input == "`h":
            print_help()
            continue

        try:
            # Check if user wants to send a command
            if user_input.startswith("`"):
                # Send the command to the server
                response = process_command(user_input)
            else:
                # send message to the server
                response = process_user_message(user_input)
        except APIException as e:
            print(e)

        print(response)

        continue

    # Print a final message
    print("Thank you for using the chat application.")
    print("Goodbye!")
