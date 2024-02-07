import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(
  firstName,
  lastName,
  fileName
) {
  const user = [{
    status: 'fulfilled',
    value: await signUpUser(firstName, lastName).catch((error) =>
      error.toString()
    ),
  }];
  const photo = [{
    status: 'fulfilled',
    value: await uploadPhoto(fileName).catch((error) => error.toString()),
  }];
  return [user, photo];
}
