import  {uploadPhoto}  from './utils';
import  { createUser }  from './utils';


export default function handleProfileSignup() {
   Promise.all([uploadPhoto(), createUser()]).then((results) => {
    const [photo, user] = results;
    console.log(photo.body, user.firstName, user.lastName);
  })
  .catch((error) => {
    console.log('Signup system offline');
  });
}
