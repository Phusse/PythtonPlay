def is_palindrome(word):
    cleaned_word = ''.join(filter(str.isalnum, word)).lower()
    return cleaned_word == cleaned_word[::-1]

while True:
    user_input = input("Enter a word or phrase (or 'quit' to exit): ")

    if user_input.lower() == "quit":
        break
    elif is_palindrome(user_input):
        print(f"{user_input} is a palindrome")
    else:
        print(f"{user_input} is not a palindrome")