export default function handleResponseFromAPI(promise) {
  return promise
    .then((response) => {
      response = {
        status: 200,
        body: 'success',
      };
    })
    .catch((error) => {
      error = {};
      console.log('Got a response from the API');
    });
}
