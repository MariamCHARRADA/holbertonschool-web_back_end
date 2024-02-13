export default function updateUniqueItems(itemList) {
  try {
    itemList.forEach((quantity, item) => {
      if (quantity === 1) {
        itemList.set(item, 100);
      }
    });
  } catch (error) {
    console.error('Cannot process');
  }
}
