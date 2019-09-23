STUDENT_LAST = 0
STUDENT_FIRST = 1
GRADE = 2
CLASSROOM = 3
BUS = 4
GPA = 5
TEACHER_LAST = 6
TEACHER_FIRST = 7

def get_bus(students_arr, bus_num):
    for student in students_arr:
        if int(student[BUS]) == bus_num:
            print(student[STUDENT_FIRST] + ", " + student[STUDENT_LAST] + ", " +
                  student[GRADE] + ", " + student[CLASSROOM])

def get_student(students_arr, last_name, bus = False):
    for student in students_arr:
        if(student[STUDENT_LAST] == last_name):
            if(bus == False):
                print(student[STUDENT_LAST] + ", " + student[STUDENT_FIRST] + ", " +
                      student[GRADE] + ", " + student[CLASSROOM] + ", " + student[TEACHER_FIRST] + " " + student[TEACHER_LAST])
            else:
                print(student[STUDENT_LAST] + ", " + student[STUDENT_FIRST] + ", " + student[BUS])

