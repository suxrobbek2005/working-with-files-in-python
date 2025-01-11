from pprint import pprint

count = 0
list_l = []

while True:
    
    print("1: Maxsulot qo'shish ")
    print("2: Qushilgan maxsulotlarni kurish ")
    print("3: maxsulotingizni sonini bilish ")
    print("4: Dasturdan chiqish ")

    choise_menyu = int(input("\nMenyu tanlang  "))

    if choise_menyu == 1:

        prudact_name = input("Maxsulotingizni nomini kiriting ").title()

        with open("shopping_list.txt", 'a') as text:
            text.write(f"{prudact_name}")
            count += 1
        print(f"{prudact_name} muavaffaqiyatli qushildi ")

    if choise_menyu == 2:

        with open("shopping_list.txt", 'r+') as text:
            texts = text.read()

            if count > 0:

                for word in texts:
                    list_l = word
                    print(list_l)
                    
            else:
                print("Siz xali birorta xam maxsulot kiritmagansiz ")
    
    if choise_menyu == 3:
         print(f"Sizning maxsulotlaringiz soni = {count}")

    if choise_menyu == 4:
        print("Bizning xizmatimizni tanlaganingizdan xursandmiz sizni kutib qolamiz xudo yor bulsin ")
        break
    if choise_menyu > 4 or choise_menyu < 0:
        print("Siz mavjud bo'lmagan menyu tanladingiz iltimos yana o'rinib kuring ") 



    
