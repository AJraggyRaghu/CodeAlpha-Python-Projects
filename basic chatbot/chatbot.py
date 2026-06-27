import datetime
import random

print("=" * 45)
print("       WELCOME TO MY PYTHON CHATBOT")
print("=" * 45)

name = input("Enter your name: ").title()

print("Hello,", name + "!")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer get cold? It forgot to close Windows!",
    "Python is my favorite language because it has no bite!"
]

while True:

    user = input(name + ": ").lower()

    if user == "hello":
        print("Bot: Hello,", name + "!")

    elif user == "hi":
        print("Bot: Hi,", name + "!")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: My name is CodeAlpha ChatBot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "what is python":
        print("Bot: Python is an easy and powerful programming language.")

    elif user == "date":
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    elif user == "time":
        now = datetime.datetime.now()
        print("Bot: Current time is", now.strftime("%H:%M:%S"))

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "calculator":
        num1 = float(input("Enter first number: "))
        op = input("Enter (+,-,*,/): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Answer =", num1 + num2)
        elif op == "-":
            print("Answer =", num1 - num2)
        elif op == "*":
            print("Answer =", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Answer =", num1 / num2)
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operator.")

    elif user == "help":
        print("\nAvailable Commands")
        print("-------------------------")
        print("hello")
        print("hi")
        print("how are you")
        print("what is your name")
        print("who created you")
        print("what is python")
        print("date")
        print("time")
        print("joke")
        print("calculator")
        print("bye\n")

    elif user == "thank you":
        print("Bot: You're welcome,", name + "!")

    elif user == "bye":
        print("Bot: Goodbye,", name + "!")
        print("Have a wonderful day.")
        break

    else:
        print("Bot: Sorry,", name + ", I didn't understand that.")