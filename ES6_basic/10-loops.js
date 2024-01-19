export default function appendToEachArrayValue(array, appendString) {
  let appended = [];
  for (const element of array) {
    array.push(appendString + element);
  }

  return appended;
}
