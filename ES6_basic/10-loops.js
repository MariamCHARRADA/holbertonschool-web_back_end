export default function appendToEachArrayValue(array, appendString) {
  const appended = [];
  for (const element of array) {
    array.push(appendString + element);
  }

  return appended;
}
