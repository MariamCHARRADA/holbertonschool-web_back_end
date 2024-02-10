export default function updateStudentGradeByCity(studentList, city, newGrades) {
    let filteredList = studentList.filter(student => student.location === city);
    filteredList.map(student => {
        newGrades.map(newGrade => {
            if (student.id === newGrade.studentId) {
                student.grade = newGrade.grade
            }
            else {
                student.grade = 'N/A';
            }
        })
    return filteredList;
    })
}