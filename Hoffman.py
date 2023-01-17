text_input = str(input("Proszę wprowadzić tekst: "))
print("Tekst: " + text_input)


dictionary = dict()
for x in text_input:
    dictionary[x] = 0
print("Słownik: " + str(dictionary))

text_length = len(text_input)
print("Długość tekstu przed kompresją: " + str(text_length))

char_list = []
for x in text_input[::]:
    if x not in char_list:
        char_list.append(x)
unique_char = len(char_list)
print("Liczba unikalnych liter: " + str(unique_char))


strtobin = ''.join(format(ord(x), '08b') for x in text_input)

list1 = [int(x) for x in list(strtobin)]
count_list1 = list1.count(0)
count_list1a = list1.count(1)
print("Liczba 0: " + str(count_list1))
print("Liczba 1: " + str(count_list1a))
print("Tekst w postaci binarnej: " + strtobin)

def compression (text):
    x = 0
    compressed_text = ""
    text_length = len(text)
    while x != text_length:
        duplicate_count = 1
        while (x<text_length-1) and (text[x] == text[x+1]):
            count = duplicate_count+1
            x = x+1
        if duplicate_count ==1:
            compressed_text += str(text[x])
        else:
            compressed_text += str(text[x]) + str(duplicate_count)
        x = x +1
    print("Skompresowany tekst: " + compressed_text)
    compressed_length = len(compressed_text)
    print("Długość tekstu po konwersji: "+str(compressed_length))
compression(text_input)