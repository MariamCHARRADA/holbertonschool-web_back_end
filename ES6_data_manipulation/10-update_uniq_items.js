export default function updateUniqueItems(itemList) {
  if (!(itemList instanceof Map)) {
    throw new Error('Cannot process');
  }
  itemList.forEach((quantity, item) => {
    if (quantity === 1) {
      itemList.set(item, 100);
    }
  });
}
