import sys
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from lxml import html
import requests
import tweepy


def create_tweet():
    response = requests.get('https://www.worldometers.info/coronavirus/')
    doc = html.fromstring(response.content)
    total, deaths, recovered = doc.xpath('//div[@class="maincounter-number"]/span/text()')
    tweet = (
        f"Coronavirus Latest Updates\n"
        f"Total cases: {total}\n"
        f"Recovered: {recovered}\n"
        f"Deaths: {deaths}\n"
        f"Source: https://www.worldometers.info/coronavirus/\n\n"
        f"#coronavirus #covid19 #covid19updates"
    )
    return tweet


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('Authentication Successful')
    except:
        print('Error while authenticating API')
        sys.exit(1)

    tweet = create_tweet()
    print(tweet)
    api.update_status(tweet)
    print('Tweet successful')
