export default function appendToEachArrayValue(array, appendString) {
  const appended = [];
  for (const element of array) {
    appended.push(appendString + element);
  }

  return appended;
}
