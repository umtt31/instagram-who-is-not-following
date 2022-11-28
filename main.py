import instaloader

L = instaloader.Instaloader()

username = "YOUR USERNAME"
password = "YOUR PASSWORD"

L.login(username, password)
profile = instaloader.Profile.from_username(L.context, username)

followers = []
following = []
notFollowing = []

for username in profile.get_followers():
    followers.append(username.username)
for username in profile.get_followees():
    following.append(username.username)

for a in following:
    if followers.count(a) == 0:
        notFollowing.append(a)
    # if followers.index(a) == val:
    #     notFollowing.append(a)


for x in notFollowing:
    print(x)