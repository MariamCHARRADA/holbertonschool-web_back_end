export default function getListStudentIds(studentsList) {
  if (Array.isArray(studentsList)) {
    return studentsList.map((student) => student.id);
  }
  return [];
}
