import instaloader

ig = instaloader.Instaloader()
profile = input("User Name: ")

ig.download_profile(profile, profile_pic_only = True)