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
        st_marks.append([90,80,90,97,60])

    students_marks = np.array(st_marks);
    students_names = np.array(st_names);
    return students_names,students_marks;

def averageGrade(students_marks):
    marks_avg = [];
    for i in students_marks:
        average = np.mean(i);
        marks_avg.append(float(average))
    return marks_avg;

def classAverage(students_marks):
    class_avg = np.sum(students_marks) / students_marks.size;
    return class_avg;

def applyGrades(students_marks):
    marks_grades = []
    for marks in students_marks:
        grade = [];
        for j in marks:
            if j >= 90:
                grade.append('A+')
            elif j >= 80:
                grade.append('A')
            elif j >= 70:
                grade.append('B')
            elif j >= 60:
                grade.append('C')
            elif j >= 50:
                grade.append('D')
            else:
                 grade.append('F')
        marks_grades.append(grade)
    return np.array(marks_grades);
    
def getGradeDistribution(students_marks):
    print(students_marks)
    above_90 = np.count_nonzero(students_marks >= 90);
    between_89_80 = np.count_nonzero((students_marks <= 89) & (students_marks >= 80));
    between_79_70 = np.count_nonzero((students_marks <= 79) & (students_marks >= 70));
    between_69_60 = np.count_nonzero((students_marks <= 69) & (students_marks >= 60));
    return np.array([above_90,between_89_80,between_79_70,between_69_60])

if __name__ == '__main__':
    print('-----------------------')
    print('  --- Report card ---')
    print('-----------------------')
    students_names,students_marks= getStudentsData();  
    marks_avg  = averageGrade(students_marks);
    print(marks_avg)
    class_avg = classAverage(students_marks)
    print(class_avg)
    marks_grades = applyGrades(students_marks);
    print(marks_grades)
    marks_deistribut = getGradeDistribution(students_marks)
    print(marks_deistribut)
    