# Zadanie 1

def cipher(text, position):
    encryption = ""
    length = len(text)
    for x in range(length):
        character = text[x]

        ordinal = ord(character)
        if (character.isupper()):
            encryption += chr(((ordinal) + position - 65) % 26 + 65)

        elif (character.isdigit()):
            digit = (int(character) + position) % 10
            encryption += str(digit)

        elif (character.islower()):
            encryption += chr(((ordinal) + position - 97) % 26 + 97)

        else:
            encryption += character
    return encryption


text = input("Proszę podać tekst ")
position = 1
print(text)
encryption = (cipher(text, position))
print(encryption)

# Zadanie 2
print("")
print("Dostępne systemy:")
print("1 - binarny")
print("2 - oktalny")
print("3 - heksadecymalny")
System = int(input("Proszę wybrać system liczbowy z listy powyżej (proszę wpisać numer od 1 do 3): "))

value = int(input("Proszę podać liczbę: "))
if System == 1:
    def dectobin(value):
        if value >= 1:
            dectobin(value // 2)
        print(value % 2, end='')


    dectobin(value)

elif System == 2:
    def dectooct(value):
        if value >= 1:
            dectooct((int)(value / 8))
            print(value % 8, end='')


    dectooct(value)

# elif System == 3:


# Zadanie 3
print("")
print("")

cipher = (input("Proszę podać ciąg znaków do deszyfracji: np. 6A3B3A2B1A"))


def decryption(cipher):
    decrypt = ""
    number = ""
    for x in cipher:
        if x.isdigit():
            number += x
        else:
            intnum = int(number)
            decrypt += x * intnum
    return decrypt


de = (decryption(cipher))
print(de)
