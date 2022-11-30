import tweepy
import dotenv
import os
import openai
import random

dotenv.load_dotenv(dotenv.find_dotenv())

openai.api_key=os.getenv("OpenAi_Key")

prompts=["funny programming jokes in portuguese"]

response=openai.Completion.create(
    engine="text-davinci-003",
    prompt=random.choice(prompts),
    temperature=0.4,
    max_tokens=64
)
Tweet= str(response.choices[0].text)
try:
    api = tweepy.Client(
        consumer_key=os.getenv("Consumer_key"),
        consumer_secret=os.getenv("Consumer_secret"),
        access_token=os.getenv("Access_token"),
        access_token_secret=os.getenv("Access_token_secret")
    )
except:
    print('Get Api Error')
    
try:
    tweeting=api.create_tweet(text=Tweet)
    print(tweeting)
except:
    print("error trying to tweet")