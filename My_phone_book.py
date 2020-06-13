
phonelist = []
isdiriving = True
while isdiriving:
    print("1.Add record\n2.Delete record\n3.Update Record\n4.Read record\n5.List Records\n6.Quit")
    istek = int(input('Please select your process (1-6) : '))
    if istek == 1:
        person = []
        
        print("\n" * 10)
        print('=' * 20 + 'Add Record' + '=' * 20)
        print("\n" * 1)
        
        name = input('Please enter name : ')
        person.append(name.lower())
        
        surname = input('Please enter surname : ')
        person.append(surname.lower())
        
        phoneNumber = input('Please enter your number : ')
        person.append(phoneNumber)
        phonelist.append(person)
        
        print('Record Added')
        print(phonelist)
        print("\n" * 2)

    elif istek == 2:
        print("\n" * 10)
        print('=' * 20 + ' Delete Record ' + '=' * 20)
        print("\n" * 1)
        name = input('Please enter name : ')
        surname = input('Please enter surname : ')
        for indeks, isim in enumerate(phonelist):
            if isim[0] == name.lower() and isim[
                1] == surname.lower():  # phonelist den isim ve o isme aid index i çıkaracak
                del (phonelist[indeks])
        print("\n" * 3)
        print('Record deleted')
        print("\n" * 2)

    elif istek == 3:
        print("\n" * 10)
        print('=' * 20 + ' Update Record ' + '=' * 20)
        print("\n" * 1)
        
        name = input('Please enter name : ')
        surname = input('Please enter surname : ')
        
        for indeks, isim in enumerate(phonelist):  # phonelist den isim ve o isme aid index i çıkaracak
            if isim[0].lower() == name.lower() and isim[1].lower() == surname.lower():  # Büyük küçük harf e karşı hassasiyeti ortadan kaldırır
                
                new_name = input('Please enter new name : ')
                new_surname = input('Please enter new surname : ')
                new_phone = input('Please enter new phone number : ')
                
                isim[0] = new_name  # Yeni isim atanıyor
                isim[1] = new_surname  # Yeni soyisim atanıyor
                isim[2] = new_phone    #Yeni telefon numarası atıyor
                break
        print("\n" * 1)
        print('Account has been updated')
        print("\n" * 2)

    elif istek == 4:
        print("\n" * 10)
        print('=' * 20 + ' Read Record ' + '=' * 20)
        print("\n" * 1)
        name = input('Please enter name : ')
        surname = input('Please enter surname : ')
        print("\n" * 1)
        for indeks, isim in enumerate(phonelist):  # phonelist den isim ve o isme aid index i çıkaracak
            if isim[0].lower() == name.lower() and isim[1].lower() == surname.lower():  # Büyük küçük harf e karşı hassasiyeti ortadan kaldırır.
                print("Name        : " + isim[0])
                print("Surname     : " + isim[1])
                print("Phone Number: " + isim[2])
        print("\n" * 3)
        print('There is no any record named {} {}'.format(name, surname))
        print("\n" * 2)
    elif istek == 5:
        print("\n" * 10)
        print('=' * 20 + ' List Records ' + '=' * 20)
        print("\n" * 1)
        for indeks, isim in enumerate(phonelist):
            print('Recording ' + str(indeks+1))
            print('_'*20)
            print("\n" * 1)
            print('Name         :' + isim[0])
            print('Surname      :' + isim[1])
            print('Phone Number :' + isim[2])
            print("\n" * 2)
    elif istek == 6:
        print('Thank you! See you again....')
        print("\n" * 2)
        isdiriving = False