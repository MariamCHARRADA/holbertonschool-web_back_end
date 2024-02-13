export default function cleanSet(set, startString) {
  let cleaned = '';
  set.forEach((element) => {
    if (element.startsWith(startString) && typeof startString === 'string') {
      cleaned += element.slice(startString.length) + '-';
    }
  });
  cleaned = cleaned.slice(0, -1);
  return cleaned;
}
