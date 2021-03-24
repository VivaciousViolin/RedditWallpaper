
import praw #reddit api plugin
import wget #download things from web


# get top post from r/wallpaper from today
top_wallpaper = reddit.subreddit('wallpaper').top(limit=1, time_filter="day")

#get picture link from r/wallpaper
for submission in top_wallpaper:
    image_url = submission.url
    if image_url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
        print(image_url)


#download the image
wget.download(image_url, 'C:/Users/Alex/Pictures/dailybackground')