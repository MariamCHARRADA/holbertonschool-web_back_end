export default function appendToEachArrayValue(array, appendString) {
  const appended_array = [];
  for (const element of array) {
    array.push(appendString + element);
  }

  return appended_array;
}
