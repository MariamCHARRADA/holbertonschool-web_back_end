export default function getIdsSum(studentsList) {
  if (Array.isArray(studentsList)) {
    return studentsList.reduce((acc, student) => acc + student.id, 0);
  }
  return 0;
}
