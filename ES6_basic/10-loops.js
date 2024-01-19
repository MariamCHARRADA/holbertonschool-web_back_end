export default function appendToEachArrayValue(array, appendString) {
  let appended = [];
  for (const element of array) {
    appended.push(appendString + element);
  }

  return appended;
}
