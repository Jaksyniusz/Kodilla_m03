# Kodilla_m03
3rd module tasks

### Zadanie 3.1

Zadanie: mała powtórka<br>
Zadanie 1<br>
Pamiętasz zadanie z listą zakupów?<br>
Załóżmy, że mamy do zrobienia zakupy spożywcze, potrzebujemy pójść do piekarni, w której kupujemy chleb, bułki oraz pączka. Poza tym po drodze wstąpimy też do warzywniaka, gdzie kupimy marchew, seler i rukolę.<br>
W pliku, który właśnie utworzyliśmy:<br>
<prep>
    zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
    Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <sklep> i kupuję tam <rzeczy>.
    Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).
    Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna liczba towarów, które są na listach.
</prep>
Twój program po uruchomieniu, powinien wyświetlić następujące informacje:<br>
Lista zakupów<br>
Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].<br>
Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].<br>
W sumie kupuję 6 produktów.<br>

Zadanie 2<br>
Napisz program, który:<br>
<prep>
    Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
    W następnym wierszu wyświetli te liczby podniesione do potęgi 3.
</prep>
Przesyłanie zadań<br>
Zrób zrzuty ekranu z uruchomienia Twoich programów przez VSCode wraz z ich kodem źródłowym i wyślij je swojemu Mentorowi.<br>
Wskazówka: Staraj się trzymać porządek w strukturze projektu i plików. Dobrym pomysłem będzie utrzymywanie każdego zadania jako osobnego pliku.<br>
Zestaw zrzutów ekranu przekaż Mentorowi w jeden z poniższych sposobów:<br>
<prep>
    umieść je w nowym katalogu na swoim dysku sieciowym (np. Dropbox, Google Drive, etc.), wklej poniżej link do katalogu (uzyskany za pomocą guzika "Udostępnij"),
    otwórz nowy dokument na Google Docs i przeciągnij do niego zrzuty ekranu, wklej poniżej link do tego dokumentu (uzyskany za pomocą guzika "Udostępnij"),
    zrób zdjęcie ekranu aparatem typu Polaroid i wyślij je gołębiem pocztowym.
</prep>


### Zadanie 3.5.1

Znajdź średnią zmodyfikowanej listy<br>
Twoim zadaniem jest zmodyfikowanie listy przypisanej do zmiennej numbers w taki sposób, aby każdy jej element zaokrąglić do pełnej dziesiątki. Postaraj się nie tworzyć nowej listy będącej zmodyfikowaną listą numbers, lecz zmodyfikować listę numbers.<br>
Po zaokrągleniu każdego elementu listy numbers, pozbądź się jej największego oraz najmniejszego elementu, a następnie do zmiennej mean_number przypisz średnią z ostatecznie zmodyfikowanej listy.<br>
Podsumowując:<br>
<prep>
    zaokrąglij każdy element numbers do pełnej 10 (np. 5 -> 10, 32 -> 30)
    znajdź, a następnie pozbądź się największego oraz najmniejszego elementu zmodyfikowanej listy
    policz średnią z ostatecznie zmodyfikowanej listy numbers i przypisz ją do zmiennej mean_number
</prep>


### Zadanie 3.5.2

Stwórz funkcję, która sprawdza, czy możemy zbudować most<br>
Naszym zadaniem jest zbudowanie mostu pomiędzy punktem A i punktem B.<br>
Do dyspozycji mamy płytę oraz łącznik, które mają określone długości.<br>
Płyt nie możemy dzielić na mniejsze części, ustawiamy je jedna obok drugiej. Płyty muszą być połączone ze sobą za pomocą łącznika. Łącznik stanowi połowę długości płyty.<br>
Stwórz funkcję build_bridge, która będzie zwracać wartość True, jeśli mając płytę o długości danej zmienną chunk jesteśmy w stanie zbudować most o długości danej zmienną goal.<br>
Niech funkcja build_bridge zwraca wartość False, jeśli zbudowanie mostu przy założeniu zmiennych chunk oraz goal nie jest możliwe.<br>
Na przykład:<br>
Jeśli goal to 20, a chunk to 2 - wtedy możemy użyć 7 płyt i 6 łączników. Możemy zbudować most, a funkcja powinna zwracać wartość True.<br>
Z drugiej strony, jeśli goal to 18, a chunk to 2 - wtedy NIE możemy zbudować mostu, a funkcja powinna zwracać wartość False.<br>


### Zadanie 3.5.3

Twojemu szefowi udało się znaleźć informacje o najlepiej sprzedających się modelach samochodów w 2018 roku. Dane, które zdobył nie nadają się niestety do analizy, dlatego poprosił Cię o przetworzenie, aby można było z nich w prosty sposób wyciągać informacje.<br>
Do zmiennej models przypisano listę zawierającą najlepiej sprzedające się samochody 2018 roku uszeregowane od najlepiej sprzedającego się w formacie 'producent - model'.<br>
Do zmiennych sales2018, sales2017 oraz sales2016 przypisano liczbę sprzedanych egzemplarzy tych modeli kolejno w roku 2018, 2017 oraz 2016.<br>
Czyli - najlepiej sprzedającym się modelem samochodu w 2018 roku był: Volkswagen Golf (pierwsza pozycja na liście models). Golf w 2018 roku sprzedał się w ilości 445 754 egzemplarzy (pierwsza pozycja na liście sales2018). Wiemy też, że w 2017 roku sprzedano 483 105 modeli Golfa (pierwsza pozycja na liście sales2017), oraz że w 2016 roku sprzedano 492 952 egzemplarzy Golfa (pierwsza pozycja na liście sales2016).<br>
Niektóre samochody nie były sprzedawane przed 2018 rokiem. W takim przypadku dane o ich sprzedaży zastąpione są wartością 'NA'. Zastąp wszystkie 'NA' cyfrą 0.<br>
Na podstawie otrzymanych danych zbuduj słownik o następującej strukturze i przypisz go do zmiennej cars:<br>
<prep>
cars = {"brand": {"model1":{"sales":{"2016": 123,

                                     "2017": 456,

                                     "2018": 789}},

                  "model2":{"sales":{"2016": 987,

                                     "2017": 654,

                                     "2018": 321}}

                 },

        "brand2": ... }
</prep>
Czyli na przykładzie rzeczywistych danych powinien wyglądać on następująco:<br>
<prep>
cars = {"Opel": {"Corsa":{"sales":{"2016": 264844,

                                   "2017": 232738,

                                   "2018": 217036}},

                 "Astra":{"sales":{"2016": 253483,

                                   "2017": 217813,

                                   "2018": 160275}}

                 },

        "Dacia": ... }
</prep>
Następnie postaraj się odpowiedzieć na pytania zaprezentowane poniżej:<br>
<prep>
    Który model samochodu z listy najlepiej sprzedawał się w 2017 roku? Odpowiedź przypisz do zmiennej answer1.
    Który producent z listy sprzedał najwięcej egzemplarzy samochodów w 2018 roku? Odpowiedź przypisz do zmiennej answer2.
    Ile modeli samochodów z listy nie sprzedawało się w 2016 roku, a do sprzedaży weszło w roku 2017? Odpowiedź przypisz do zmiennej answer3.
    Który z model samochodu z listy ma najmniej sprzedanych egzemplarzy, jeśli weźmiemy pod uwagę lata 2016, 2017 oraz 2018. Odpowiedź przypisz do zmiennej answer4.
    O ile procent wzrosła sprzedaż modeli Forda w 2018 roku w stosunku do roku 2017? Odpowiedź przypisz do zmiennej answer5. Odpowiedź podaj w formacie procentowym jako string. Np. '21%'.
</prep>
UWAGA! Na potrzeby zadania potraktuj 'VW' i 'Volkswagen' jako osobnych producentów<br>


### Zadanie 3.5.4

Rzuty kostką<br>
Gramy w grę polegającą na rzucaniu typową sześcienną kostką.<br>
W każdej kolejce gracz dwukrotnie rzuca kością. Po dwukrotnym rzuceniu kością wynikiem gracza jest suma wyrzuconych oczek z rzutu numer 1 oraz rzutu numer 2.<br>
Napisz program, który do słownika dict przypisuje pary key i value, gdzie:<br>
<prep>
    key - to możliwy do uzyskania wynik w jednej kolejce (suma oczek w dwóch rzutach)
    value - to wszystkie kombinacje rzutów, które składają się na dany key
</prep>
Wszystkie możliwe kombinacje do uzyskania danego wyniku przechowuj jako zbiór, w którym każdy kolejny element to krotka, której pierwsza wartość to rezultat pierwszego rzutu, a druga wartość to rezultat drugiego rzutu.<br>
Na przykład wywołując:<br>
<prep>
dice[7]
</prep>
Wynik powinien zawierać następujące elementy:<br>
<prep>
{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)}
</prep>