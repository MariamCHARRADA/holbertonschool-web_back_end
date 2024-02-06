export default function handleResponseFromAPI(promise) {
  return promise
    .then((response) => {
      response = {
        status: 200,
        body: 'success',
      };
      console.log('Got a response from the API');
      return response;
    })
    .catch(() => {
      return new Error;
    });
}
