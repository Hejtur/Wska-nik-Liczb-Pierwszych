print("Witaj w programie, który wskazuje czy podana przez Ciebie liczba jest liczbą pierwszą")
print('\n')
print('Poniżej znajduję się krótkie menu, ktore pozwala Ci się poruszać po tym programie')
print('\n')
print('Napisz 1 aby podać liczbę')
print('Napisz 2 aby zakończyć działanie programu')
while(True):
   
    wybor = input('Napisz liczbę 1 lub 2: ')
    if wybor == '1':
        liczba = int(input('Wpisz dowolną liczbę: '))
        if liczba == 1:
                     print('Jeden nie jest liczbą pierwszą, gdyż definicja liczb pierwszych zakłada, że są to liczby naturalne większe niż 1')
        elif liczba % 2 == 0 or liczba % 3 == 0 or liczba % 4 == 0 or liczba % 5 == 0 or liczba % 6 == 0 or liczba % 7 == 0 or liczba % 8 == 0 or liczba % 9 == 0 or liczba % 10 == 0:
                     print('Podana zmienna nie jest liczbą pierwszą')
        else:
                     print('Podana zmienna to liczba pierwsza!')
    elif wybor == '2':
        break    
    else:
        print('Proszę podać liczbę 1 lub 2')
