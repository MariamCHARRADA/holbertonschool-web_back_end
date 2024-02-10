export default function createInt8TypedArray(length, position, value) {
  const ArrayBuff = new ArrayBuffer(length);
  const int8Array = new Int8Array(ArrayBuff);
  if (position >= 0 && position < length) {
    int8Array[position] = value;
  } else {
    throw new Error("Position outside range");
  }

  return new DataView(ArrayBuff);
}
