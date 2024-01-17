export default function appendToEachArrayValue(array, appendString) {
  for (let element of array) {
    let element += appendString;
  }

  return array;
}
