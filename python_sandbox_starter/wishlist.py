video_games = [
    "The Legend of Zelda",
    "Splatoon 2",
    "Super Mario"
]


def display_wishlist(display_name, wishes):
    print(display_name + ":")
    suggested_gift = wishes.pop(0)
    print("=======>", suggested_gift, "<=======")
    for wish in wishes:
        print("* " + wish)
    print()


display_wishlist("Video Games", video_games)
