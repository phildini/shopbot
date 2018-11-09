import os
import random
import pytz
import datetime
from mastodon import Mastodon


DAYS = {
    0: [
        "#movie Monday! What'd everybody watch over the weekend?",
        "Mondays we often talk #movie. What should we see while it's still in theaters or streaming?",
    ],
    1: [
        "It's #tv Tuesday! Binge any good seasons on Netflix lately?",
        "Tuesdays we often talk #tv -- what good shows have we been missing?",
    ],
    2: [
        "It's #wip / #writing Wednesday. What's everyone working on?",
        "Mid-week #wip / #writing Wednesday. Show off and talk about your in-progress creations!",
    ],
    3: [
        "It's #thankful Thursday! What's gone well for you this week?",
        "Prompt: What are you #thankful for this Thursday?",
    ],
    4: [
        "Friday is for #fanfic -- who's shipping what this week?",
        "It's Follow Friday (#ff) -- who's toots are the tops?",
    ],
    6: [
        "It's #scifi Sunday! What's got you thinking out of this world?",
        "Sunday #scifi -- what worlds are we exploring today?",
    ],
}


def toot():
    access_token = os.getenv('ACCESS_TOKEN')
    visibility = os.getenv('VISIBILITY', 'direct')
    client = Mastodon(
        access_token=access_token,
        api_base_url='https://wandering.shop',
    )
    today = datetime.datetime.today().weekday()
    toot = f'{random.choice(DAYS[today])}\n\ncc @phildini',
    client.status_post(
        status=toot,
        visibility=visibility,
    )


if __name__ == '__main__':
    toot()