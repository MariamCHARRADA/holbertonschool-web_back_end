export default function updateUniqueItems(itemList) {
  itemList.forEach((quantity, item) => {
    if (quantity === 1) {
      itemList.set(item, 100);
    }
  });
}
