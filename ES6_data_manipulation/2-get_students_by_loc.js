export default function getStudentsByLocation(studentsList, city) {
  if (Array.isArray(studentsList)) {
    return studentsList.filter((student) => student.location === city);
  }
  return [];
}
