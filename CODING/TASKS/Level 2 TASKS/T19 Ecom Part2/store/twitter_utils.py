import tweepy
from django.conf import settings


def get_twitter_client():
    return tweepy.Client(
        consumer_key=settings.TWITTER_API_KEY,
        consumer_secret=settings.TWITTER_API_SECRET,
        access_token=settings.TWITTER_ACCESS_TOKEN,
        access_token_secret=settings.TWITTER_ACCESS_SECRET,
    )


def tweet_new_store(store_name, description):
    client = get_twitter_client()
    message = f"New Store Alert! 🏪\n\n{store_name}: {description}"
    client.create_tweet(text=message)


def tweet_new_product(store_name, product_name, description):
    client = get_twitter_client()
    message = f"New Item at {store_name}! 🛍️\n\n{product_name}: {description}"
    client.create_tweet(text=message)
