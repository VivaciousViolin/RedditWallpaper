
import praw #reddit api plugin
import wget #download things from web

#reddit api key
reddit = praw.Reddit(
    client_id="HXCeAdSuEYPXFQ",
    client_secret="	FcNIVNV5zRLGg5fnOsWMtYLN7ntjww",
    redirect_uri="http://localhost:8080",
    user_agent="public wallpaper scraper",
)

# get top post from r/wallpaper from today
top_wallpaper = reddit.subreddit('wallpaper').top(limit=1, time_filter="day")

#get picture link from r/wallpaper
for submission in top_wallpaper:
    image_url = submission.url
    if image_url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
        print(image_url)


#download the image
wget.download(image_url, 'C:/Users/Alex/Pictures/dailybackground')
