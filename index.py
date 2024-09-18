import numpy as np
import json

def getStudentsData():
    num_student = int(input("[+] Enter the number of students to input: "));
    st_marks = [];
    st_names = [];
    for i in range(num_student):
        name = input("Enter a student name: ");
        st_names.append(name);
        print(f"Enter moumi each sub marks: ")
        bengali = int(input("Bengali: "));
        english = int(input("English: "));
        math = int(input("Math: "));
        biology = int(input("Biology: "));
        physics = int(input("Physics: "));
        chemistry = int(input("Chemistry: "))
        st_marks.append([bengali,english,math,biology,physics,chemistry])

    students_marks = np.array(st_marks);
    students_names = np.array(st_names);
    return students_names,students_marks;

def averageGrade(students_marks):
    marks_avg = [];
    for i in students_marks:
        average = np.mean(i);
        marks_avg.append(float(round(average,2)))
    return marks_avg;

def classAverage(students_marks):
    class_avg = np.sum(students_marks) / students_marks.size;
    return round(class_avg,2);

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
    above_90 = np.count_nonzero(students_marks >= 90);
    between_89_80 = np.count_nonzero((students_marks <= 89) & (students_marks >= 80));
    between_79_70 = np.count_nonzero((students_marks <= 79) & (students_marks >= 70));
    between_69_60 = np.count_nonzero((students_marks <= 69) & (students_marks >= 60));
    return np.array([above_90,between_89_80,between_79_70,between_69_60])

def getTopperStudent(students_marks):
    marks_sum = np.sum(students_marks,axis=1) # sum of each row
    top_marks = np.max(marks_sum);
    topper_index = np.where(marks_sum==top_marks);
    return topper_index[0];

if __name__ == '__main__':
    studentReport= {};
    print('--------------------------------')
    print('  --- Generate Report Card ---')
    print('-------------------------------')
    students_names,students_marks= getStudentsData();  
    marks_avg  = averageGrade(students_marks);
    class_avg = classAverage(students_marks)
    marks_grades = applyGrades(students_marks);
    marks_deistribut = getGradeDistribution(students_marks);
    topper_index = getTopperStudent(students_marks);
    for i in range(len(students_marks)):
        studentReport.update({
            "classAvg":float(class_avg),
            "classTopers":{
                "ids":list(map(lambda i: int(i),topper_index)),
                "names":list(map(lambda i: str(students_names[i]),topper_index))
            },
            "marksDistribute":{
                "above_90":marks_deistribut[0].tolist(),
                "between_89_80":marks_deistribut[1].tolist(),
                "between_79_70":marks_deistribut[2].tolist(),
                "between_69_60":marks_deistribut[3].tolist(),
            },
            f"student {i+1}":{
                "id":i,
                "name":str(students_names[i]),
                "marks":students_marks[i].tolist(),
                "marks_avg":float(marks_avg[i]),
                "marks_grades":marks_grades[i].tolist(),
            }
        })
    with open('studentList.json','w') as file:
        json.dump(studentReport,file,indent=4);

    print("Data has been written to studentList.json 😊🚀")