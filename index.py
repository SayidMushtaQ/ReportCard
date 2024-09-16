import numpy as np


def getStudentsData():
    num_student = 2  #int(input("[+] Enter the number of students to input: "));
    st_marks = [];
    st_names = [];
    for i in range(num_student):
        # name = input("Enter a student name: ");
        st_names.append(f'moumi {i}');
        print(f"Enter moumi each sub marks: ")
        # bengali = int(input("Bengali: "));
        # english = int(input("English: "));
        # math = int(input("Math: "));
        # biology = int(input("Biology: "));
        # physics = int(input("Physics: "));
        # chemistry = int(input("Chemistry: "))
        st_marks.append([70,66,90,97,90])

    students_marks = np.array(st_marks);
    students_names = np.array(st_names);
    return students_names,students_marks;


if __name__ == '__main__':
    print('-----------------------')
    print('  --- Report card ---')
    print('-----------------------')
    students_names,students_marks= getStudentsData();  
    print(students_names,students_marks)
    