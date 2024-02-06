export default function handleResponseFromAPI(promise) {
 try{
    promise
    .then((response) => {
         response = {status: 200,
            body: 'success'}
            console.log('Got a response from the API')
        return response ;
    })
    .catch((error) => {
        console.log(error);
    });
 }
 catch(error){
    console.log(error);

 } 
}
