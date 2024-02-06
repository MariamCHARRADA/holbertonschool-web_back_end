export default function handleResponseFromAPI(promise) {
  return promise
    .then((response) => {
      console.log('Got a response from the API');
      return response = {
        status: 200,
        body: 'success',
      };
    })
    .catch(() => {
      return new Error();
    });
}
