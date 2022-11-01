from dotenv import load_dotenv
import os
from instabot import Bot
from scripts.getapod import get_apod
import random



def create_caption():
    with open('results/caption.txt', 'r') as f:
        caption_info = f.readlines()

    emojis = random.choice(['🔭','🪐','☄️','🛸','👽','🛰','🚀','👩‍🚀'])
    title = caption_info[0][:-2] + random.choice(emojis)
    credit = caption_info[1]

    with open('assets/hashtags.txt', 'r') as f:
        hashtag_list = f.read().split()
    
    hashtags = []
    for i in range(20):
        curhashtag = random.choice(hashtag_list)
        while curhashtag in hashtags:
            curhashtag = random.choice(hashtag_list)
        hashtags.append(f'{curhashtag} ')

    return f"{title} \n{credit} \n@nasa @nasawebb {''.join(hashtags)}"


def post_photo(title):
    print('\n'*20)
    print(title)

    if (input('Post? (y/n) ') != 'y'):
        return
    if (input('Confirm? (y/n) ') != 'y'):
        return

    bot = Bot()
    bot.login(username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
    bot.upload_photo("results/apod.jpg", caption=caption)



get_apod()
caption = create_caption()

# post_photo(caption)