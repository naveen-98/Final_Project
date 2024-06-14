import instaloader


def get_instagram_profile_info():
    ig = instaloader.Instaloader()

    usrname = input("Enter Username: ")

    profile = instaloader.Profile.from_username(ig.context, usrname)

    print("Username: ", profile.username)
    print("Number of Posts Uploads: ", profile.mediacount)
    print(profile.username + " is having " + str(profile.followers) + ' followers.')
    print(profile.username + " is following " + str(profile.followees) + ' people')
    print("Bio: ", profile.biography)
    instaloader.Instaloader().download_profile(usrname, profile_pic_only=True)


if __name__ == "__main__":
    get_instagram_profile_info()
