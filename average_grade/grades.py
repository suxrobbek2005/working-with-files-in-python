while True:
    print("\n1: Talabalarning baholarini qo'shish")
    print("2: Talabalarning ismini va bahosini ko'rish")
    print("3: Talabalarning o'rtacha bahosini ko'rish")
    print("4: Dasturdan chiqish")

    
    choice_m = int(input("\nQuyidagi menyulardan birini tanlang: "))


    if choice_m == 1:
        student_name = input("Talabaning ismini kiriting: ")
        grade = int(input("Talabaning bahosini kiriting: "))


        with open("grades.txt", 'a') as grades:
            grades.write(f"{student_name}: {grade}\n")
        print(f"\n{student_name} muvaffaqiyatli qo'shildi!\n")


    elif choice_m == 2:
        try:
            with open("grades.txt", 'r') as grades_s:
                gradess = grades_s.readlines()
                
                if gradess:
                    print("\nFaylda saqlangan talabalar va baholari:")
                    for grade_student in gradess:
                        print(grade_student.strip())
                else:
                    print("\nFaylda hali hech qanday ma'lumot yo'q.")
        except FileNotFoundError:
            print("\nFayl topilmadi. Avval baholarni kiriting.")


    elif choice_m == 3:
        try:
            with open("grades.txt", 'r') as grades_s:
                gradess = grades_s.readlines()


                if gradess:
                    total = 0  
                    count = 0  

                    for grade_student in gradess:
                       
                        name, grade = grade_student.strip().split(": ")
                        total += int(grade)  
                        count += 1  

                    average = total / count
                    print(f"\nTalabalar o'rtacha bahosi: {average:.2f}")
                else:
                    print("\nFaylda hali hech qanday baho mavjud emas.")
        except FileNotFoundError:
            print("\nFayl topilmadi. Avval baholarni kiriting.")

    elif choice_m == 4:
        print("\nBizning xizmatimizni tanlaganingiz uchun rahmat! Yaxshi kun tilaymiz!")
        break

    else:
        print("\nNoto'g'ri tanlov. Iltimos, menyudan birini tanlang.")


        