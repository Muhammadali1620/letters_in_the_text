def letters_in_the_text(text):
    letters = {}
    result = ""
    for i in text:
        if not i.isalpha():
            print("Xariflarda kiriting!")
            return letters_in_the_text(input("So'z kiriting: "))
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    for key, value in letters.items():
        result += f"{key} = {value}\n"
    return result


text = input("So'z kiriting: ")
print(letters_in_the_text(text))