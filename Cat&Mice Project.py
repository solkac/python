# Importy
import pygame
import random
import math

# Dane do współrzędnych
OPEN = open("Garden.txt", 'r')
Read_Line1 = OPEN.readline()
Read_Line2 = OPEN.readline()
Read_Line3 = OPEN.readline()
Read_Line4 = OPEN.readline()
INT1 = int(Read_Line1)
INT2 = int(Read_Line2)
INT3 = int(Read_Line3)
INT4 = int(Read_Line4)


# Dane Ogrodu
FPS = 30
Garden_Name = "Ogród™"
Garden_X = INT1
Garden_Y = INT2
Garden_Border = INT3
Grass_Colour = (0,153,0)
Border_Colour = (160,82,45)
Border_Size = INT4
Mice_Number = 50
Ordinery_Cats_Number = 3
Lazy_Cats_Number = 3
Kittens_Number = 4

# Dane do myszy
Normal_Mouse = dict(
    Speed_A=0,
    Speed_B=1,
    Speed_Change_A=0,
    Speed_Change_B=40,
    Acceleration_A=10,
    Acceleration_B=100,
    Turn_A=0.1 * math.pi,
    Turn_B=0.8 * math.pi,
    Turn_Speed_A=1 * math.pi,
    Turn_Speed_B=3 * math.pi,
    Time_A=0.3,
    Time_B=0.6,
    Turn_Near_Border=0.2 * math.pi,
    Colour=(192, 192, 192),
    Size=5
)
# Również dane do myszy
Near_Cat_Turn = 0.1 * math.pi
Panic_Distance = 150
Panic_Speed = 200
Turn_Panic = 5 * math.pi
Time_Panic = 0.3

# Dane do Przeciętnego Kota
Ordinery_Cat = dict(
    Speed_A=10,
    Speed_B=25,
    Speed_Change_A=0,
    Speed_Change_B=20,
    Acceleration_A=10,
    Acceleration_B=20,
    Turn_A=0 * math.pi,
    Turn_B=0.5 * math.pi,
    Turn_Speed_A=0.6 * math.pi,
    Turn_Speed_B=1 * math.pi,
    Time_A=0.5,
    Time_B=1,
    Turn_Near_Border=0.5 * math.pi,
    Colour=(0, 0, 0),
    Size=20
)

# Dane do leniwego kota
Lazy_Cat = dict(
    Speed_A=5,
    Speed_B=10,
    Speed_Change_A=0,
    Speed_Change_B=10,
    Acceleration_A=10,
    Acceleration_B=30,
    Turn_A=0 * math.pi,
    Turn_B=0.3 * math.pi,
    Turn_Speed_A=0.3 * math.pi,
    Turn_Speed_B=0.6 * math.pi,
    Time_A=0.5,
    Time_B=1,
    Turn_Near_Border=0.5 * math.pi,
    Colour=(105, 105, 105),
    Size=30
)

# Dane do kociaka
Kitten = dict(
    Speed_A=25,
    Speed_B=35,
    Speed_Change_A=0,
    Speed_Change_B=30,
    Acceleration_A=10,
    Acceleration_B=20,
    Turn_A=0 * math.pi,
    Turn_B=1 * math.pi,
    Turn_Speed_A=1 * math.pi,
    Turn_Speed_B=1.6 * math.pi,
    Time_A=0.5,
    Time_B=1,
    Turn_Near_Border=1 * math.pi,
    Colour=(128, 128, 128),
    Size=10
)

# Również dane do kociaka
Near_Mouse_Turn = 0.1 * math.pi
Kitten_Panic_Distance = 150
Kitten_Panic_Speed = 200
Kitten_Turn_Panic = 5 * math.pi
Kitten_Time_Panic = 0.3

# Klasa ogród. Zawiera dane potrzebne do stworzenia ogrodu jak i kotów i myszy
class Garden:
    # Obiekt mysz
    Mice = None
    # Obiekt kot
    Ordinery_cats = None
    # Obiekt leniwy kot
    Lazy_cats = None
    # Obiekt kociak
    Kittens = None

    def __init__(self):
        # Klatki na sekundę
        self.fps = FPS
        # Nazwa ogrodu
        self.name = Garden_Name
        # Współrzędne X ogrodu
        self.Coordinate_X = Garden_X
        # Współrzędne Y ogrodu
        self.Coordinate_Y = Garden_Y
        # Rozmiar ogrodzenia
        self.Border = Garden_Border
        # Kolor trawy
        self.Grass = Grass_Colour
        # Kolor ogrodzenia
        self.Border_Colour = Border_Colour
        # Szerokość ogrodzenia
        self.Border_Size = Border_Size
        # Liczba myszy
        self.Mice_Number = Mice_Number
        # Liczba kotów
        self.Ordinery_Cats_Number = Ordinery_Cats_Number
        self.Lazy_Cats_Number = Lazy_Cats_Number
        self.Kittens_Number = Kittens_Number

        # Dziura na myszy
        Garden.Mice = []
        # Karton na koty
        Garden.Ordinery_cats = []
        Garden.Lazy_cats = []
        Garden.Kittens = []

        # Okno programu
        self.screen = pygame.display.set_mode((self.Coordinate_X, self.Coordinate_Y))
        # Nazwa programu
        pygame.display.set_caption(self.name)
        # Zegar programu
        self.clock = pygame.time.Clock()

        # Tworzenie myszy
        self.create_mice()
        # Tworzenie kotyów
        self.create_ordinery_cats()
        self.create_lazy_cats()
        self.create_kittens()

    # Funkcja od tworzenia myszy
    def create_mice(self):
        for x in range(self.Mice_Number):
            Garden.Mice.append(Mouse())

    # Funkcja od tworzenia kotów
    def create_ordinery_cats(self):
        for x in range(self.Ordinery_Cats_Number):
            Garden.Ordinery_cats.append(Cat())

    def create_lazy_cats(self):
        for x in range(self.Lazy_Cats_Number):
            Garden.Lazy_cats.append(Lazy_Cats())

    def create_kittens(self):
        for x in range(self.Kittens_Number):
            Garden.Kittens.append(Kitty())

    # Funkcja odpowiedzialna za ruch
    def update_movement(self):
        for x in Garden.Mice:
            # Zmiana koordynatów
            x.position_update()
            if x.FPS_Number >= x.End_FPS:
                x.Turns()
        for x in Garden.Ordinery_cats:
            # Zmiana koordynatów
            x.position_update()
            if x.FPS_Number >= x.End_FPS:
                x.Turns()
        for x in Garden.Lazy_cats:
            # Zmiana koordynatów
            x.position_update()
            if x.FPS_Number >= x.End_FPS:
                x.Turns()
        for x in Garden.Kittens:
            # Zmiana koordynatów
            x.position_update()
            if x.FPS_Number >= x.End_FPS:
                x.Turns()
        self.clock.tick(FPS)

    # Funkcja od rysowania ogrodu i zwierząt
    def draw(self):
        # Wypełnia okno kolorem trawy
        self.screen.fill(self.Grass)
        # Wyznacza granice ogrodu
        pygame.draw.rect(self.screen, self.Border_Colour,
                         (self.Border, self.Border, self.Coordinate_X - 2 * self.Border,
                          self.Coordinate_Y - 2 * self.Border), self.Border_Size)
        # Rysuje myszy
        for x in Garden.Mice:
            x.draw()
        # Rysuje koty
        for x in Garden.Ordinery_cats:
            x.draw()
        for x in Garden.Lazy_cats:
            x.draw()
        for x in Garden.Kittens:
            x.draw()
        # Odświeżenie okna
        pygame.display.flip()


# Klasa odpowiedzialna za koty
class Cats:
    def __init__(self, behaviour):
        # Minimalny ruch kotów
        self.Speed_A = behaviour["Speed_A"]
        # Maksymalny ruch kotów
        self.Speed_B = behaviour["Speed_B"]
        # Minimalna zmiana ruchu kotów
        self.Speed_Change_A = behaviour["Speed_Change_A"]
        # Maksymalna zmiana ruchu kotów
        self.Speed_Change_B = behaviour["Speed_Change_B"]
        # Minimalne przyspieszenie kotów
        self.Acceleration_A = behaviour["Acceleration_A"]
        # Maksymalne przyspieszenie kotów
        self.Acceleration_B = behaviour["Acceleration_B"]
        # Minimalny obrót kotów
        self.Turn_A = behaviour["Turn_A"]
        # Maksymalny obrót kotów
        self.Turn_B = behaviour["Turn_B"]
        # Minimalna prędkość obrotu kotów
        self.Turn_Speed_A = behaviour["Turn_Speed_A"]
        # Maksymalna prędkość obrotu kotów
        self.Turn_Speed_B = behaviour["Turn_Speed_B"]
        # Minimalny czas
        self.Time_A = behaviour["Time_A"]
        # Maksymalny czas
        self.Time_B = behaviour["Time_B"]
        # Zmiana kierunku przy granicy ogrodu
        self.Turn_Near_Border = behaviour["Turn_Near_Border"]
        # Kolor sierści
        self.Colour = behaviour["Colour"]
        # Rozmiar kota
        self.Size = behaviour["Size"]

        # Ogólny ruch
        self.Speed = None
        # Ruch końcowy
        self.End_Speed = None
        # Ogólne przyspieszenie
        self.Acceleration = None
        # Zmiana ruchu co klatkę
        self.Speed_Change = None
        # Kierunek ruchu
        self.Direction = None
        # Końcowy kierunek ruchu
        self.End_Direction = None
        # Ogólna prędkość obrotu
        self.Turn_Speed = None
        # Ogólny czas
        self.Time = None
        # Zmiana kierunku co klatkę
        self.Direction_per_fps = None
        # Pozycja X
        self.Position_X = None
        # Pozycja Y
        self.Position_Y = None
        # Liczba klatek
        self.FPS_Number = None
        # Końcowa liczba klatek
        self.End_FPS = None
        # Sprawdzenie czy kot przyspiesza
        self.Acceleration_Present = None
        # Sprawdzenie czy kot obraca się według wskazówek zegara
        self.Clock_Turn_Present = None

        # Początkowy stan kota
        self.state()
        # Wykonywana Tura
        self.Turns()

    # Funckja odpowiedzialna za początkowy stan kota
    def state(self):
        self.Speed = random.uniform(self.Speed_A, self.Speed_B)
        self.Direction = random.uniform(-math.pi, math.pi)
        # Współrzędne kotów
        OPEN1 = open("Cat.txt", 'r')
        Read_Line01 = OPEN1.readline()
        Read_Line02 = OPEN1.readline()
        INT01 = int(Read_Line01)
        INT02 = int(Read_Line02)
        self.Position_X = INT01
        self.Position_Y = INT02

    # Funkcja odpowiedzialna za turę. Przyda się później, jak zrobię pozostałe
    def Turns(self):
        pass

    # Funkcja od normalnej tury
    def Normal_Turn(self):
        # Zmiana ruchu
        self.End_Speed = self.Speed + random.choice([1, -1]) * random.uniform(self.Speed_Change_A, self.Speed_Change_B)
        # Maksymalny ruch jeśli ogólny ruch jest większy
        if self.End_Speed > self.Speed_B:
            self.End_Speed = self.Speed_B
        # Minimalny ruch jeśli ogólny ruch jest mniejszy
        if self.End_Speed < self.Speed_A:
            self.End_Speed = self.Speed_A
        # Zmiana kierunku ruchu
        self.End_Direction = self.Direction + random.choice([1, -1]) * random.uniform(
            self.Turn_A, self.Turn_B)
        # Zmiana przyspieszenia
        self.Acceleration = random.uniform(self.Acceleration_A, self.Acceleration_B)
        # Zmiana prędkości obrotu
        self.Turn_Speed = random.uniform(self.Turn_Speed_A, self.Turn_Speed_B)
        # Zmiana czasu
        self.Time = random.uniform(self.Time_A, self.Time_B)

    # Funkcja odpowiedzialna z wykonanie tury na granicy ogrodu
    def Near_The_Border(self):
        # Maksymalna prędkość
        self.End_Speed = self.Speed_B
        # Kierunkek do środka ogrodu
        self.End_Direction = self.To_Center(Garden_X / 2, Garden_Y / 2) + random.uniform(
            -self.Turn_Near_Border, self.Turn_Near_Border)
        # Największe przyspieszenie
        self.Acceleration = self.Acceleration_B
        # Najszybszy obrót
        self.Turn_Speed = self.Turn_Speed_B
        # Najdłuższy możliwy czas
        self.Time = self.Time_B

    # Funkcja odpowiedzialna za sprawdzanie czy kot jest na granicy
    def Present_At_The_Border(self):
        if (self.Position_X < Garden_Border or
                self.Position_X > Garden_X - Garden_Border or
                self.Position_Y < Garden_Border or
                self.Position_Y > Garden_Y - Garden_Border):
            return True
        else:
            return False

    # Funkcja odpowiedzialna za kierowanie kotem do danego punktu/centrum ogrodu
    def To_Center(self, x, y):
        return math.atan2(-self.Position_Y + y, -self.Position_X + x)

    # Funkcja zawierająca wszystkie dane kota
    def Parameters(self):
        # Kierunek pomiędzy -pi a +pi
        self.Direction = math.remainder(self.Direction, 2 * math.pi)
        self.End_Direction = math.remainder(self.End_Direction, 2 * math.pi)
        # Sprawdza czy kot przyspiesza
        if self.Speed < self.End_Speed:
            self.Acceleration_Present = True
        else:
            self.Acceleration_Present = False
        # Sprawdza czy kot porusza się według wskazówek zegara
        if math.remainder(self.Direction - self.End_Direction, 2 * math.pi) < 0:
            self.Clock_Turn_Present = True
        else:
            self.Clock_Turn_Present = False
        self.Speed_Change = self.Acceleration / FPS
        self.Direction_per_fps = self.Turn_Speed / FPS
        self.End_FPS = self.Time * FPS
        # Reset liczby klatek
        self.FPS_Number = 0

    # Funkcja odpowiedzialna za aktualizacje pozycji i koordynatów
    def position_update(self):
        # Przyspieszenie kota dopóki nie osiągnie odpowiedniego ruchu
        if self.Acceleration_Present and self.Speed < self.End_Speed:
            self.Speed += self.Speed_Change
        # Spowolnienie kota dopóki nie osiągnie odpowiedniego ruchu
        elif not self.Acceleration_Present and self.Speed > self.End_Speed:
            self.Speed -= self.Speed_Change
        # Obroacanie kota według wskazówek zegara tak długo aż nie osiągnie odpowiedniego obrotu. (Sam zaczynam się przez tą ilośc warunków gubić)
        if self.Clock_Turn_Present:
            if self.End_Direction > 0 and self.Direction < self.End_Direction:
                self.Direction += self.Direction_per_fps
            elif self.End_Direction < 0 and self.Direction < self.End_Direction + math.pi * (
                    abs(self.Direction) + self.Direction) / abs(self.Direction):
                self.Direction += self.Direction_per_fps
        # Obracanie kota w przeciwnym kierunku tak długo aż nie osiągnie odpowiedniego obrotu (To samo co wyżej ale na odwrót)
        else:
            if self.End_Direction < 0 and self.Direction > self.End_Direction:
                self.Direction -= self.Direction_per_fps
            elif self.End_Direction > 0 and self.Direction > self.End_Direction - math.pi * (
                    abs(self.Direction) - self.Direction) / abs(self.Direction):
                self.Direction -= self.Direction_per_fps
        # Aktualizacja X
        self.Position_X += math.cos(self.Direction) * self.Speed / FPS
        # Aktualizacja Y
        self.Position_Y += math.sin(self.Direction) * self.Speed / FPS
        # Zwiększenie liczby klatek na sekundę
        self.FPS_Number += 1

    # Rysowanie kota
    def draw(self):
        pygame.draw.circle(garden.screen, self.Colour, (round(self.Position_X),
                                                              round(self.Position_Y)), self.Size, 0)

# Klasa odpowiedzialna za koty
class Mice:
    def __init__(self, behaviour):
        # Minimalny ruch myszy
        self.Speed_A = behaviour["Speed_A"]
        # Maksymalny ruch myszy
        self.Speed_B = behaviour["Speed_B"]
        # Minimalna zmiana ruchu myszy
        self.Speed_Change_A = behaviour["Speed_Change_A"]
        # Maksymalna zmiana ruchu myszy
        self.Speed_Change_B = behaviour["Speed_Change_B"]
        # Minimalne przyspieszenie myszy
        self.Acceleration_A = behaviour["Acceleration_A"]
        # Maksymalne przyspieszenie myszy
        self.Acceleration_B = behaviour["Acceleration_B"]
        # Minimalny obrót myszy
        self.Turn_A = behaviour["Turn_A"]
        # Maksymalny obrót myszy
        self.Turn_B = behaviour["Turn_B"]
        # Minimalna prędkość obrotu myszy
        self.Turn_Speed_A = behaviour["Turn_Speed_A"]
        # Maksymalna prędkość obrotu myszy
        self.Turn_Speed_B = behaviour["Turn_Speed_B"]
        # Minimalny czas
        self.Time_A = behaviour["Time_A"]
        # Maksymalny czas
        self.Time_B = behaviour["Time_B"]
        # Zmiana kierunku przy granicy ogrodu
        self.Turn_Near_Border = behaviour["Turn_Near_Border"]
        # Kolor sierści
        self.Colour = behaviour["Colour"]
        # Rozmiar myszy
        self.Size = behaviour["Size"]

        # Ogólny ruch
        self.Speed = None
        # Ruch końcowy
        self.End_Speed = None
        # Ogólne przyspieszenie
        self.Acceleration = None
        # Zmiana ruchu co klatkę
        self.Speed_Change = None
        # Kierunek ruchu
        self.Direction = None
        # Końcowy kierunek ruchu
        self.End_Direction = None
        # Ogólna prędkość obrotu
        self.Turn_Speed = None
        # Ogólny czas
        self.Time = None
        # Zmiana kierunku co klatkę
        self.Direction_per_fps = None
        # Pozycja X
        self.Position_X = None
        # Pozycja Y
        self.Position_Y = None
        # Liczba klatek
        self.FPS_Number = None
        # Końcowa liczba klatek
        self.End_FPS = None
        # Sprawdzenie czy kot przyspiesza
        self.Acceleration_Present = None
        # Sprawdzenie czy kot obraca się według wskazówek zegara
        self.Clock_Turn_Present = None

        # Początkowy stan myszy
        self.state()
        # Wykonywana Tura
        self.Turns()

    # Funckja odpowiedzialna za początkowy stan myszy
    def state(self):
        self.Speed = random.uniform(self.Speed_A, self.Speed_B)
        self.Direction = random.uniform(-math.pi, math.pi)
        # Współrzędne myszy
        OPEN2 = open("Mice.txt", 'r')
        Read_Line001 = OPEN2.readline()
        Read_Line002 = OPEN2.readline()
        INT001 = int(Read_Line001)
        INT002 = int(Read_Line002)
        self.Position_X = INT001
        self.Position_Y = INT002

    # Funkcja odpowiedzialna za turę. Przyda się później, jak zrobię pozostałe
    def Turns(self):
        pass

    # Funkcja od normalnej tury
    def Normal_Turn(self):
        # Zmiana ruchu
        self.End_Speed = self.Speed + random.choice([1, -1]) * random.uniform(self.Speed_Change_A, self.Speed_Change_B)
        # Maksymalny ruch jeśli ogólny ruch jest większy
        if self.End_Speed > self.Speed_B:
            self.End_Speed = self.Speed_B
        # Minimalny ruch jeśli ogólny ruch jest mniejszy
        if self.End_Speed < self.Speed_A:
            self.End_Speed = self.Speed_A
        # Zmiana kierunku ruchu
        self.End_Direction = self.Direction + random.choice([1, -1]) * random.uniform(
            self.Turn_A, self.Turn_B)
        # Zmiana przyspieszenia
        self.Acceleration = random.uniform(self.Acceleration_A, self.Acceleration_B)
        # Zmiana prędkości obrotu
        self.Turn_Speed = random.uniform(self.Turn_Speed_A, self.Turn_Speed_B)
        # Zmiana czasu
        self.Time = random.uniform(self.Time_A, self.Time_B)

    # Funkcja odpowiedzialna z wykonanie tury na granicy ogrodu
    def Near_The_Border(self):
        # Maksymalna prędkość
        self.End_Speed = self.Speed_B
        # Kierunkek do środka ogrodu
        self.End_Direction = self.To_Center(Garden_X / 2, Garden_Y / 2) + random.uniform(
            -self.Turn_Near_Border, self.Turn_Near_Border)
        # Największe przyspieszenie
        self.Acceleration = self.Acceleration_B
        # Najszybszy obrót
        self.Turn_Speed = self.Turn_Speed_B
        # Najdłuższy możliwy czas
        self.Time = self.Time_B

    # Funkcja odpowiedzialna za sprawdzanie czy kot jest na granicy
    def Present_At_The_Border(self):
        if (self.Position_X < Garden_Border or
                self.Position_X > Garden_X - Garden_Border or
                self.Position_Y < Garden_Border or
                self.Position_Y > Garden_Y - Garden_Border):
            return True
        else:
            return False

    # Funkcja odpowiedzialna za kierowanie myszami do danego punktu/centrum ogrodu
    def To_Center(self, x, y):
        return math.atan2(-self.Position_Y + y, -self.Position_X + x)

    # Funkcja zawierająca wszystkie dane myszy
    def Parameters(self):
        # Kierunek pomiędzy -pi a +pi
        self.Direction = math.remainder(self.Direction, 2 * math.pi)
        self.End_Direction = math.remainder(self.End_Direction, 2 * math.pi)
        # Sprawdza czy mysz przyspiesza
        if self.Speed < self.End_Speed:
            self.Acceleration_Present = True
        else:
            self.Acceleration_Present = False
        # Sprawdza czy mysz porusza się według wskazówek zegara
        if math.remainder(self.Direction - self.End_Direction, 2 * math.pi) < 0:
            self.Clock_Turn_Present = True
        else:
            self.Clock_Turn_Present = False
        self.Speed_Change = self.Acceleration / FPS
        self.Direction_per_fps = self.Turn_Speed / FPS
        self.End_FPS = self.Time * FPS
        # Reset liczby klatek
        self.FPS_Number = 0

    # Funkcja odpowiedzialna za aktualizacje pozycji i koordynatów
    def position_update(self):
        # Przyspieszenie kota dopóki nie osiągnie odpowiedniego ruchu
        if self.Acceleration_Present and self.Speed < self.End_Speed:
            self.Speed += self.Speed_Change
        # Spowolnienie kota dopóki nie osiągnie odpowiedniego ruchu
        elif not self.Acceleration_Present and self.Speed > self.End_Speed:
            self.Speed -= self.Speed_Change
        # Obroacanie kota według wskazówek zegara tak długo aż nie osiągnie odpowiedniego obrotu. (Sam zaczynam się przez tą ilośc warunków gubić)
        if self.Clock_Turn_Present:
            if self.End_Direction > 0 and self.Direction < self.End_Direction:
                self.Direction += self.Direction_per_fps
            elif self.End_Direction < 0 and self.Direction < self.End_Direction + math.pi * (
                    abs(self.Direction) + self.Direction) / abs(self.Direction):
                self.Direction += self.Direction_per_fps
        # Obracanie kota w przeciwnym kierunku tak długo aż nie osiągnie odpowiedniego obrotu (To samo co wyżej ale na odwrót)
        else:
            if self.End_Direction < 0 and self.Direction > self.End_Direction:
                self.Direction -= self.Direction_per_fps
            elif self.End_Direction > 0 and self.Direction > self.End_Direction - math.pi * (
                    abs(self.Direction) - self.Direction) / abs(self.Direction):
                self.Direction -= self.Direction_per_fps
        # Aktualizacja X
        self.Position_X += math.cos(self.Direction) * self.Speed / FPS
        # Aktualizacja Y
        self.Position_Y += math.sin(self.Direction) * self.Speed / FPS
        # Zwiększenie liczby klatek na sekundę
        self.FPS_Number += 1

    # Rysowanie myszy
    def draw(self):
        pygame.draw.circle(garden.screen, self.Colour, (round(self.Position_X),
                                                              round(self.Position_Y)), self.Size, 0)

# Klasa Ordinery Cat odpowiedzialna za wykonywanie operacji z klasy Cats
class Cat(Cats):
    def __init__(self):
        # Specyficzne dane dla kota
        Cats.__init__(self, Ordinery_Cat)

    # Wykonywanie odpowiednich tur
    def Turns(self):
        # Poruszanie się ku środkowi planszy jeśli kot znajduje się przy granicy
        if self.Present_At_The_Border():
            self.Near_The_Border()
        else:
            # Wykonanie normalnej tury jeśli nie znajduje się na granicy
            self.Normal_Turn()
        # Aktualizacja parametrów po wykonaniu tury
        self.Parameters()

class Lazy_Cats(Cats):
    def __init__(self):
        # Specyficzne dane dla kota
        Cats.__init__(self, Lazy_Cat)

    # Wykonywanie odpowiednich tur
    def Turns(self):
        # Poruszanie się ku środkowi planszy jeśli kot znajduje się przy granicy
        if self.Present_At_The_Border():
            self.Near_The_Border()
        else:
            # Wykonanie normalnej tury jeśli nie znajduje się na granicy
            self.Normal_Turn()
        # Aktualizacja parametrów po wykonaniu tury
        self.Parameters()


class Kitty(Cats):
    def __init__(self):
        # Specyficzne dane dla kota
        Cats.__init__(self, Kitten)

    # Wykonywanie odpowiednich tur
    def Turns(self):
        # Poruszanie się ku środkowi planszy jeśli kot znajduje się przy granicy
        if self.Present_At_The_Border():
            self.Near_The_Border()
        else:
            # Wykonanie normalnej tury jeśli nie znajduje się na granicy
            self.Normal_Turn()
        # Aktualizacja parametrów po wykonaniu tury
        self.Parameters()

# Klasa Mouse odpowiedzialna za wykonywanie operacji z klasy Mice
class Mouse(Mice):
    def __init__(self):
        # Specyficzne dane dla myszy
        Mice.__init__(self, Normal_Mouse)
        # Obrót w pobliżu kota
        self.Near_Cat_Turn = Near_Cat_Turn
        # Dystans od którego mysz zaczyna uciekać
        self.Panic_Distance = Panic_Distance
        # Przyspieszenie ruchu w trakcie paniki
        self.Panic_Speed = Panic_Speed
        # Szybszy obórt w trakcie paniki
        self.Turn_Panic = Turn_Panic
        # Czas trwania paniki
        self.Time_Panic = Time_Panic

        # Sprawdzenie obecności kota
        self.Cats_Presence = None

    # Funkcja odpowiedzialna za sprawdzanie obecności kota
    def near_cat(self):
        for x in Garden.Ordinery_cats and Garden.Lazy_cats and Garden.Kittens:
            if math.sqrt((self.Position_X - x.Position_X) ** 2 +
                         (self.Position_Y - x.Position_Y) ** 2) < self.Panic_Distance:
                return x
        return False

    # Wykonywanie odpowiednich tur
    def Turns(self):
        self.Cats_Presence = self.near_cat()
        if self.Cats_Presence is not False:
            self.Turn_Near_Cat()
        elif self.Present_At_The_Border():
            self.Near_The_Border()
        else:
            self.Normal_Turn()
        self.Parameters()

    # Tura w pobliżu cota
    def Turn_Near_Cat(self):
        # Zwykły ruch na ruch w trakcie paniki
        self.End_Speed = self.Panic_Speed
        # Ruch w kierunku przeciwnym do kota
        self.End_Direction = math.remainder(self.To_Center(self.Cats_Presence.Position_X,
                                     self.Cats_Presence.Position_Y) + math.pi, 2 * math.pi) + random.uniform(
                                    -self.Near_Cat_Turn, self.Near_Cat_Turn)
        # Maksymalne przyspiesznie
        self.Acceleration = self.Acceleration_B
        # Zwykły obrót na obrót w trakcie paniki
        self.Turn_Speed = self.Turn_Panic
        # Zwykły czas na czas trwania paniki
        self.Time = self.Time_Panic



if __name__ == "__main__":
    # Inicjalizacja programu
    pygame.init()
    garden = Garden()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        garden.update_movement()
        garden.draw()