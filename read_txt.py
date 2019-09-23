from student_bus_cmd import *
def read_file():
    infile = open("students.txt")
    arr = []
    for line in infile:
        student = line
        arr.append(student.strip().split(","))
    return arr

def main():
    students_arr = read_file()
    get_bus(students_arr, 51)
    get_student(students_arr, "TOWLEY")
if __name__ == "__main__":
    main()