from pprint import pprint

count = 0

while True:

    print("Telifon raqamlar bilan ishalash ")
    print("1: Telifon raqam qushish ")
    print("2: Telifon raqamlarni kurish ")
    print("3: Foydalanuchilar sonini kurish ")
    print("4: Dasturdan chiqish ")

    choise = int(input("Menyu tanlang "))

    if choise == 1:

        name = input("Ismingizni kiriting ")
        contact_u = int(input("Telifon raqamingizni kiriting "))

        with open("contact.txt", 'w') as text:
            text.write(f"{name}, {contact_u}")
            count += 1
            print(f"{name} ning telifon raqami muaffaqiyatli qushildi")
    
    if choise == 3:

        print(f"Ayni vaqtda dasturimida {count} foydalanuchining raqami saqlanmoqda ")
    
    if choise == 2:

        while True:

            with open("contact.txt", 'r') as text:
                contacts = text.readline()

                if contacts:
                    pprint("Saqlangan kontaktalar \n")
                        
                    if count >= 1:
                            
                         print(contacts.strip())
                         break

                    else:
                        print("Sizda hali birorta ham raqam saqlanmagan ")
    
    if choise == 4:
        print("Xizmatimizdan foydalanganingiz uchun tashakur sizni kutib qolamiz ")
        break

    if choise > 4 or choise < 0:
        print("\nSiz bizda mavjud bo'lmagan menyuni tanladingiz \n")
    



        
