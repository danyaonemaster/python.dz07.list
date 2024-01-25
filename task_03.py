def run():
    print("\nTask_03\n")

    user_input = input("Enter your text: ")

    user_input_lowercase = user_input.lower()

    user_input_stripped = user_input_lowercase.replace(" ", "")

    if user_input_stripped[::-1] == user_input_stripped:
        print("text is a palindrome")
    else:
        print("text is not a palindrome")
