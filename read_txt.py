def read_file():
    infile = open("students.txt")
    arr = []
    for line in infile:
        student = line
        arr.append(student.strip().split(","))
    return arr

def main():
    students_arr = read_file()

if __name__ == "__main__":
    main()