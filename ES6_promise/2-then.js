export default function handleResponseFromAPI(promise) {
  try {
    promise
      .then((response) => {
        console.log("Got a response from the API");
       return response = {
          status: 200,
          body: "success",
        };
      })
      .catch((error) => {
        return new error

      });
  } catch (error) {
    console.log(error);
  }
}
