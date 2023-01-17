# Class
def start():
    class NPC:
        def __init__(self, name, surname, profession, race):
            self.name = name    
            self.surname = surname
            self.proffesion = profession
            self.race = race

    NPC1 = NPC("Andreous", "Penypouches", "Handlarz", "Człowiek")
    NPC2 = NPC("Iohaness", "Everguard", "Strażnik", "Człowiek")
    NPC3 = NPC("Alrik", "Svensky", "Kapitan", "Krasnolud")


    class Character:
        # Base information
        def __init__(self, name, surname, age, race, subrace, archetype, background):
            self.name = name
            self.surname = surname
            self.age = age
            self.race = race
            self.subrace = subrace
            self.archetype = archetype
            self.background = background


    Char_name = input('Wypisz imię postaci: ')
    Char_surname = input('Wypisz nazwisko postaci: ')
    Char_age = input('Podaj wiek postaci: ')
    Char_race = input('Podaj rasę postaci: ')
    Char_subrace = input('Podaj pochodzenie postaci: ')
    Char_archetype = input('Wybierz klasę postaci: ')
    Char_background = input('Podaj pod-klasę postaci: ')
    print("")
    mycharacter = Character(Char_name, Char_surname, Char_age, Char_race, Char_subrace, Char_archetype, Char_background)
    print('Informacje o postaci:')
    print('Imię: ' + mycharacter.name)
    print('Nazwisko: ' + mycharacter.surname)
    print('Wiek: ' + mycharacter.age)
    print('Rasa: ' + mycharacter.race)
    print('Pochodzenie: ' + mycharacter.subrace)
    print('Klasa: ' + mycharacter.archetype)
    print('Pod-klasa: ' + mycharacter.background)
    print("")

# Character's statistics
    def statistics():
        STR = 10
        DEX = 10
        END = 10
        INT = 10
        WIS = 10
        CHA = 10

# Race bonuses
        if mycharacter.race == 'Człowiek':
            STR = STR+1
            INT = INT+1

        elif mycharacter.race == "Krasnolud":
            END = END+2
            STR = STR+1
            CHA = CHA-1

        elif mycharacter.race == "Elf":
            DEX = DEX+2
            CHA = CHA+1
            STR = STR-1

        elif mycharacter.race == "Ork":
            STR = STR+2
            END = END+1
            INT = INT-1

        elif mycharacter.race == "Kobold":
            WIS = WIS+2
            DEX = DEX+1
            INT = INT+1
            CHA = CHA-2

# Sub-race bonuses
        if mycharacter.race == 'Człowiek':
            if mycharacter.subrace == 'Człowiek z Północy':
                STR = STR+1
                END = END+1
            elif mycharacter.subrace == 'Człowiek z Imperium':
                STR = STR+1
                CHA = CHA+1
            elif mycharacter.subrace == 'Człowiek ze Wschodu':
                INT = INT+1
                WIS = WIS+1
            else:
                print("Wybrano złe pochodzenie!")

        elif mycharacter.race == 'Krasnolud':
            if mycharacter.subrace == "Krasnolud z Twierdzy":
                END = END+1
                WIS = WIS+1
            elif mycharacter.subrace == "Krasnolud z Powierzchni":
                CHA = CHA+1
                WIS = WIS+1
            else:
                print("Wybrano złe pochodzenie!")

        elif mycharacter.race == 'Elf':
            if mycharacter.subrace == "Elf Wysokiego Rodu":
                CHA = CHA+1
                INT = INT+1
            elif mycharacter.subrace == "Leśny Elf":
                DEX = DEX+1
                WIS = WIS+1
            elif mycharacter.subrace == "Mroczny Elf":
                DEX = DEX+1
                STR = STR+1
            else:
                print("Wybrano złe pochodzenie!")

        elif mycharacter.race == 'Ork':
            if mycharacter.subrace == "Koczownik":
                DEX = DEX+1
                END = END+1
            elif mycharacter.subrace == "Członek Klanu":
                STR = STR+1
                END = END+1
            else:
                print("Wybrano złe pochodzenie!")

        elif mycharacter.race == 'Kobold':
            if mycharacter.subrace == "Kobold Kopalniany":
                DEX = DEX+1
                INT = INT+1
            elif mycharacter.subrace == "Kobold ze Smoczego Rodu":
                STR = STR+1
                CHA = CHA+1
            else:
                print("Wybrano złe pochodzenie!")

# Class bonuses
        if mycharacter.archetype == 'Czempion':
            STR = STR+2
            WIS = WIS+1

        elif mycharacter.archetype == 'Łotrzyk':
            DEX = DEX+2
            CHA = CHA+1

        elif mycharacter.archetype == 'Barbarzyńca':
            STR = STR+1
            END = END+1

        elif mycharacter.archetype == 'Łowca':
            DEX = DEX+2
            WIS = WIS+1

        elif mycharacter.archetype == 'Mag':
            INT = INT+2
            CHA = CHA+1

# Sub-Class Bonuses
        if mycharacter.archetype == 'Czempion':
            if mycharacter.background == 'Rycerz Zakonny':
                WIS = WIS+1
            elif mycharacter.background == 'Paladyn':
                END = END+1
            else:
                print("Wybrano złą pod-klasę!")

        if mycharacter.archetype == 'Łotrzyk':
            if mycharacter.background == 'Szarlatan':
                CHA = CHA+1
            elif mycharacter.background == 'Przemytnik':
                DEX = DEX+1
            else:
                print("Wybrano złą pod-klasę!")

        if mycharacter.archetype == 'Barbarzyńca':
            if mycharacter.background == 'Wojownik Klanu':
                STR = STR+1
            elif mycharacter.background == 'Szaman':
                INT = INT+1
            else:
                print("Wybrano złą pod-klasę!")

        if mycharacter.archetype == 'Łowca':
            if mycharacter.background == 'Kłusownik':
                DEX = DEX+1
            elif mycharacter.background == 'Łowca Nagród':
                STR = STR+1
            else:
                print("Wybrano złą pod-klasę!")

        if mycharacter.archetype == 'Mag':
            if mycharacter.background == 'Członek Zakonu Magów':
                INT = INT+1
            elif mycharacter.background == 'Samozwańczy Mag':
                STR = STR+1
            else:
                print("Wybrano złą pod-klasę!")


# Adding statistics by yourself

        print("Możesz wybrać jeszcze bonus do 4 różnych statystyk.")
        print('Obecne statystyki: \nSiła: ' + str(STR), '\nZręczność: ' + str(DEX), '\nWytrzymałość: ' + str(END),
              '\nInteligencja: ' + str(INT), '\nWiedza: ' + str(WIS), '\nCharyzma: ' + str(CHA))
        print("")
        wybor1 = input('Wybierz pierwszy bonus do:')
        if wybor1 == "Siła":
            STR = STR+2
        elif wybor1 == "Zręczność":
            DEX = DEX+2
        elif wybor1 == "Wytrzymałość":
            END = END+2
        elif wybor1 == "Inteligencja":
            INT = INT+2
        elif wybor1 == "Wiedza":
            WIS = WIS+2
        elif wybor1 == "Charyzma":
            CHA = CHA+2
        print("")
        wybor2 = input('Wybierz drugi bonus:')
        if wybor2 == wybor1:
            while wybor2 == wybor1:
                print("Tą statystykę można wybrać tylko raz!")
                wybor2 = input('Wybierz drugi bonus:')
            else:
                if wybor2 == "Siła":
                    STR = STR + 2
                elif wybor2 == "Zręczność":
                    DEX = DEX + 2
                elif wybor2 == "Wytrzymałość":
                    END = END + 2
                elif wybor2 == "Inteligencja":
                    INT = INT + 2
                elif wybor2 == "Wiedza":
                    WIS = WIS + 2
                elif wybor2 == "Charyzma":
                    CHA = CHA + 2
        elif wybor2 != wybor1:
            if wybor2 == "Siła":
                STR = STR + 2
            elif wybor2 == "Zręczność":
                DEX = DEX + 2
            elif wybor2 == "Wytrzymałość":
                END = END + 2
            elif wybor2 == "Inteligencja":
                INT = INT + 2
            elif wybor2 == "Wiedza":
                WIS = WIS + 2
            elif wybor2 == "Charyzma":
                CHA = CHA + 2
        print("")
        wybor3 = input('Wybierz trzeci bonus:')
        if wybor3 == wybor2:
            while wybor3 == wybor2:
                print("Tą statystykę można wybrać tylko raz!")
                wybor3 = input('Wybierz drugi bonus:')
            else:
                if wybor3 == "Siła":
                    STR = STR + 2
                elif wybor3 == "Zręczność":
                    DEX = DEX + 2
                elif wybor3 == "Wytrzymałość":
                    END = END + 2
                elif wybor3 == "Inteligencja":
                    INT = INT + 2
                elif wybor3 == "Wiedza":
                    WIS = WIS + 2
                elif wybor3 == "Charyzma":
                    CHA = CHA + 2
        elif wybor3 != wybor2:
            if wybor3 == "Siła":
                STR = STR + 2
            elif wybor3 == "Zręczność":
                DEX = DEX + 2
            elif wybor3 == "Wytrzymałość":
                END = END + 2
            elif wybor3 == "Inteligencja":
                INT = INT + 2
            elif wybor3 == "Wiedza":
                WIS = WIS + 2
            elif wybor3 == "Charyzma":
                CHA = CHA + 2
        print("")
        wybor4 = input('Wybierz czwarty bonus:')
        if wybor4 == wybor3:
            while wybor4 == wybor3:
                print("Tą statystykę można wybrać tylko raz!")
                wybor3 = input('Wybierz drugi bonus:')
            else:
                if wybor4 == "Siła":
                    STR = STR + 2
                elif wybor4 == "Zręczność":
                    DEX = DEX + 2
                elif wybor4 == "Wytrzymałość":
                    END = END + 2
                elif wybor4 == "Inteligencja":
                    INT = INT + 2
                elif wybor4 == "Wiedza":
                    WIS = WIS + 2
                elif wybor4 == "Charyzma":
                    CHA = CHA + 2
        elif wybor4 != wybor3:
            if wybor4 == "Siła":
                STR = STR + 2
            elif wybor4 == "Zręczność":
                DEX = DEX + 2
            elif wybor4 == "Wytrzymałość":
                END = END + 2
            elif wybor4 == "Inteligencja":
                INT = INT + 2
            elif wybor4 == "Wiedza":
                WIS = WIS + 2
            elif wybor4 == "Charyzma":
                CHA = CHA + 2
        print("")
        print('Obecne statystyki: \nSiła: ' + str(STR), '\nZręczność: ' + str(DEX), '\nWytrzymałość: ' + str(END),
              '\nInteligencja: ' + str(INT), '\nWiedza: ' + str(WIS), '\nCharyzma: ' + str(CHA))
        return(STR)
    statistics()
    print("")
# Equipment
    def Eq():
        Equipment = []
        if mycharacter.archetype == "Czempion":
            Equipment.append("Miecz długi")
            Equipment.append("Tarcza")
            Equipment.append("Pancerz płytowy")
            purse = 20
            print("Twój obecny ekwipunek:" + "\n-" + Equipment[0] + "\n-" + Equipment[1] + "\n-" + Equipment[2])
            print("W twojej sakiewce znajduje się: " + str(purse) + " Złotych monet")
            return Equipment


        elif mycharacter.archetype == "Łotrzyk":
            Equipment.append("Rapier")
            Equipment.append("Sztylet")
            Equipment.append("Pancerz Skórzany")
            purse = 15
            print("Twój obecny ekwipunek:" + "\n-" + Equipment[0] + "\n-" + Equipment[1] + "\n-" + Equipment[2])
            print("W twojej sakiewce znajduje się: " + str(purse) + " Złotych monet")
            return Equipment

        elif mycharacter.archetype == "Barbarzyńca":
            Equipment.append("Topór bojowy")
            Equipment.append("Topór do rzucania")
            Equipment.append("Pancerz Skórzany")
            purse = 5
            print("Twój obecny ekwipunek:" + "\n-" + Equipment[0] + "\n-" + Equipment[1] + "\n-" + Equipment[2])
            print("W twojej sakiewce znajduje się: " + str(purse) + " Złotych monet")
            return Equipment

        elif mycharacter.archetype == "Łowca":
            Equipment.append("Łuk długi")
            Equipment.append("Miecz krótki")
            Equipment.append("Pancerz z utwardzonej skóry")
            purse = 10
            print("Twój obecny ekwipunek:" + "\n-" + Equipment[0] + "\n-" + Equipment[1] + "\n-" + Equipment[2])
            print("W twojej sakiewce znajduje się: " + str(purse) + " Złotych monet")
            return Equipment

        elif mycharacter.archetype == "Mag":
            Equipment.append("Księga zaklęć")
            Equipment.append("Sztylet")
            Equipment.append("Proste szaty")
            purse = 25
            print("Twój obecny ekwipunek:" + "\n-" + Equipment[0] + "\n-" + Equipment[1] + "\n-" + Equipment[2])
            print("W twojej sakiewce znajduje się: " + str(purse) + "Złotych monet")
            return Equipment

    Eq()



# Disclaimer
print(
    'Zanim przejdziesz do tworzenia postaci proponuje zapoznać się z dostępnymi klasami, podklasami, rasami, pochodzeniem postaci oraz statystykami. (\nWybierz 1,2,3,4,5 lub 6 by przejść dajel...)')
print('')

# Menu functions
def Menu():
    print(
        'Menu wyboru: \n1.Lista klas, \n2.Lista pod-klas, \n3.Lista ras, \n4.Lista pochodzenia postaci, \n5.Dostępne statystyki, \n6.Rozpocznij przygodę')

def Classes():
    print(
        'W grze znajduję się pięć klas: '
        '\nCzempion - +2STR, +1WIS,  \nŁotrzyk - +2DEX, +1CHA,'
        '\nBarbarzyńca - +2STR, +1END, \nŁowca - +2DEX, +1WIS,'
        '\nMag - +2INT, +1CHA.'
    )

def Sub_Classes():
    print(
            'Każda z czterech klas posiada dwie podklasy: '
          '\nCzempion: \n-Rycerz Zakonny - +1WIS, \n-Błędny Rycerz - +1END,'
          '\nŁotrzyk: \n-Szarlatan - +1CHA, \n-Przemytnik - +1DEX,'
          '\nBarbarzyńca: \n-Wojownik Klanu - +1STR, \n-Szaman - +1INT,'
          '\nŁowca: \n-Kłusownik - +1DEX, \n-Łowca Nagród - +1STR,'
          '\nMag: \n-Członek Zakonu Magów - +1INT, \n-Samozwańczy Mag - +STR,'
    )

def Races():
    print('W grze znajduje się 5 ras:'
          '\nCzłowiek - +1STR, +1INT,'
          '\nKrasnolud - +2END, +1STR, -1CHA,'
          '\nElf - +2DEX, +1CHA, -1STR,'
          '\nOrk - +2STR, +1END, -1INT,'
          '\nKobold - +2WIS, +1DEX, +1INT, -2CHA '
    )

def Sub_Races():
    print('Każdej rasie przypadają po dwa pochodzenia (wyjątkiem są ludzie oraz elfy):'
          '\nCzłowiek z Północy - +1STR, +1END,'
          '\nCzłowiek z Imperium - +1CHA, +1STR,'
          '\nCzłowiek ze Wschodu - +1WIS, +1INT,'
          '\nKrasnolud z Twierdzy - +1END, +1WIS,'
          '\nKrasnolud z Powierzchni - +1CHA, +1WIS,'
          '\nElf Wysokiego Rodu - +1CHA, +1INT,'
          '\nMroczny Elf - +1DEX, +1STR,'
          '\nLeśny Elf - +1DEX, +1WIS,'
          '\nKoczownik - +1DEX, +1END,'
          '\nCzłonek Klanu - +1STR, +1END'
          '\nKobold Kopalniany - +1DEX, +1INT,'
          '\nKobold ze Smoczego Rodu - +1STR, +1CHA'
    )

def Stats():
    print(
        'W grze znajduje się 6 podstawowych statystyk: \nSiła, \nZręczność, \nWytrzymałość, \nInteligencja, \nWiedza, \nCharyzma')

Menu()
Menu_wyboru = input()
if Menu_wyboru == '1':
    Classes()
    print("")
    print('Czy chcesz wrócić do menu wyboru lub przejść dalej? \n(Wpisz "Powrót" by powrócić do menu wyboru.'
          '\nWpisz "Dwa" by przejść do listy pod-klas. \nWpisz "Trzy" by przejść do listy ras. \nWpisz "Cztery" by przejść do listy pochodzeń.'
          '\nWpisz "Pięć" by przejść do listy dostępnych statystyk. \nWpisz "Sześć" by rozpocząć przygodę (Zalecane zapoznanie się ze wszystkimi listami).")')
    powrot = input()
    if powrot == 'Powrót':
        print('Powrót do menu wyboru...')
        Menu()
    elif powrot == "Dwa":
        Sub_Classes()
    elif powrot == "Trzy":
        Races()
    elif powrot == "Cztery":
        Sub_Races()
    elif powrot == "Pięć":
        Stats()
    elif powrot == "Sześć":
        start()

elif Menu_wyboru == '2':
    Sub_Classes()
    print("")
    print('Czy chcesz wrócić do menu wyboru lub przejść dalej? \n(Wpisz "Powrót" by powrócić do menu wyboru.'
          '\nWpisz "Jeden" by przejść do listy klas. \nWpisz "Trzy" by przejść do listy ras. \nWpisz "Cztery" by przejść do listy pochodzeń.'
          '\nWpisz "Pięć" by przejść do listy dostępnych statystyk. \nWpisz "Sześć" by rozpocząć przygodę (Zalecane zapoznanie się ze wszystkimi listami).")')
    powrot = input()
    if powrot == 'Powrót':
        print('Powrót do menu wyboru...')
        Menu()
    elif powrot == "Jeden":
        Classes()
    elif powrot == "Trzy":
        Races()
    elif powrot == "Cztery":
        Sub_Races()
    elif powrot == "Pięć":
        Stats()
    elif powrot == "Sześć":
        start()

elif Menu_wyboru == '3':
    Races()
    print("")
    print('Czy chcesz wrócić do menu wyboru lub przejść dalej? \n(Wpisz "Powrót" by powrócić do menu wyboru.'
          '\nWpisz "Jeden" by przejść do listy klas. \nWpisz "Dwa" by przejść do listy pod-klas. \nWpisz "Cztery" by przejść do listy pochodzeń.'
          '\nWpisz "Pięć" by przejść do listy dostępnych statystyk. \nWpisz "Sześć" by rozpocząć przygodę (Zalecane zapoznanie się ze wszystkimi listami).")')
    powrot = input()
    if powrot == 'Powrót':
        print('Powrót do menu wyboru...')
        Menu()
    elif powrot == "Jeden":
        Classes()
    elif powrot == "Dwa":
        Sub_Classes()
    elif powrot == "Cztery":
        Sub_Races()
    elif powrot == "Pięć":
        Stats()
    elif powrot == "Sześć":
        start()

elif Menu_wyboru == '4':
    Sub_Races()
    print("")
    print('Czy chcesz wrócić do menu wyboru lub przejść dalej? \n(Wpisz "Powrót" by powrócić do menu wyboru.'
          '\nWpisz "Jeden" by przejść do listy klas. \nWpisz "Dwa" by przejść do listy pod-klas. \nWpisz "Trzy" by przejść do listy ras.'
          '\nWpisz "Pięć" by przejść do listy dostępnych statystyk. \nWpisz "Sześć" by rozpocząć przygodę (Zalecane zapoznanie się ze wszystkimi listami).")')
    powrot = input()
    if powrot == 'Powrót':
        print('Powrót do menu wyboru...')
        Menu()
    elif powrot == "Jeden":
        Classes()
    elif powrot == "Dwa":
        Sub_Classes()
    elif powrot == "Trzy":
        Races()
    elif powrot == "Pięć":
        Stats()
    elif powrot == "Sześć":
        start()

elif Menu_wyboru == '5':
    Stats()
    print("")
    print('Czy chcesz wrócić do menu wyboru lub przejść dalej? \n(Wpisz "Powrót" by powrócić do menu wyboru.'
          '\nWpisz "Jeden" by przejść do listy pod-klas. \nWpisz "Dwa" by przejść do listy pod-klas. \nWpisz "Trzy" by przejść do listy ras. \nWpisz "Cztery" by przejść do listy pochodzeń.'
          '\nWpisz "Sześć" by rozpocząć przygodę (Zalecane zapoznanie się ze wszystkimi listami).")')
    powrot = input()
    if powrot == 'Powrót':
        print('Powrót do menu wyboru...')
        Menu()
    elif powrot == "Jeden":
        Classes()
    elif powrot == "Dwa":
        Sub_Classes()
    elif powrot == "Trzy":
        Races()
    elif powrot == "Cztery":
        Sub_Races()
    elif powrot == "Sześć":
        start()

elif Menu_wyboru == '6':
    print('Przenoszenie do kreatora postaci...')
    start()
