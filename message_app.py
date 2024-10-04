# message_app.py

def display_messages():
    try:
        with open('messages.txt', 'r') as file:
            print("Messages from friends:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No messages yet.")

def input_message():
    message = input("Enter your message: ")
    with open('messages.txt', 'a') as file:
        file.write(message + '\n')
    print("Your message has been saved!")

def main():
    while True:
        print("\n1. Input a message")
        print("2. Display messages")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            input_message()
        elif choice == '2':
            display_messages()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
