export default function cleanSet(set, startString) {
  let cleaned = '';
  if(typeof(startString) === 'string'){
    set.forEach((element) => {
        if (element.startsWith(startString)) {
          cleaned += element.slice(startString.length) + '-';
        }
      });
      cleaned = cleaned.slice(0, -1);
  }

  return cleaned;
}
