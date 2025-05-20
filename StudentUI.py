import os
import StudentClass as SC
os.chdir("StudentManagerClass")
if os.path.isdir("student_class") == False:
     os.mkdir("student_class")
os.chdir("student_class")
for class_name in ["1-1","1-2","1-3","1-4"]:
     open(f"{class_name}_class.txt","a").close()
while True:
    try:
        print("""What do you want to do?:
          1-continue
          2-exit""")
        main_choose = int(input("Enter your choise(1,2): "))
        if main_choose == 2:
            break
        elif main_choose == 1:
            print("""
                  1- 1/1
                  2-1/2
                  3-1/3
                  4-1/4""")
            classChoose = int(input("Enter your choise(1,2,3,4): "))
            cnclass = f"1-{classChoose}"
            dictClass = {
                   1:SC.Student1_1,
                   2:SC.Student1_2,
                   3:SC.Student1_3,
                   4:SC.Student1_4
            }
            student_class = dictClass.get(classChoose)
            if student_class:
                    student = student_class()
                    student.nclass = cnclass
                    print("""What would you like to do?: 
                         1-Add student
                         2-Remove student
                         3-Search for specific student
                         4-Show all students""")
                    op = int(input("Enter your choise(1,2,3): "))
                    if op == 1:
                          student.name = input("Enter the student name: ")
                          student.age = int(input("Enter the student age: "))
                          student.add()
                    elif op == 2:
                          student.name = input("Enter the student name: ")
                          print(student.remove())
                    elif op == 3:
                           student.name = input("Enter the student name: ")
                           print(student.exist())
                    elif op == 4:
                           student.see()
                    else:
                           print("invalid input,please enter a valid input")
            else:
                print("Invalid input, please enter a valid input")
        else:
            print("Invalid input please enter a correct input(1,2)")
    except ValueError:
        print("Invalid input please enter a correct input")
    finally:
        print("-------------------------------------------------------")
