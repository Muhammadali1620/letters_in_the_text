def letters_in_the_text(text):
    letters = {}
    result = ""
    for i in text:
        if i.isalpha():
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    for key, value in letters.items():
        result += f"{key} = {value}\n"
    return result


text = input("So'z kiriting: ")
print(letters_in_the_text(text))