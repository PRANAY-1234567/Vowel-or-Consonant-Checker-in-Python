ch = input("Enter any alphabet : ")

if len(ch) == 1 and ch.isalpha():
    ch = ch.upper()

    match ch:
        case 'A' | 'E' | 'I' | 'O' | 'U':
            print("Vowel")
        case _:
            print("Consonant")
else:
    print("Error")

