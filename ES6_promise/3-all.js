import * as utilsFunctions from "./utils";

export default async function handleProfileSignup() {
    const profile = await utilsFunctions.createUser();
    const photo = await utilsFunctions.uploadPhoto();
    console.log(photo.body,profile.firstName,profile.lastName);
    return { profile, photo };
}
