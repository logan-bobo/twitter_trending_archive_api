import tweepy
import logging

from datetime import datetime
from airflow.decorators import task, dag
from airflow.models import Variable


START_DATE = datetime(2023, 1, 29)
TWITTER_BEARER_TOKEN = Variable.get("TWITTER_BEARER_TOKEN")


# How WOEIDs work - https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends -
# Find WOEIDs https://www.woeids.com/ (Yahoo closed their API)
WOEID_MAPPING = {
    "United Kingdom": 23424975,
    # "United States of America": 23424977,
    # "Germany": 23424829,
    # "Canada": 23424775,
    # "Mexico": 23424900,
    # "Japan": 23424856,
    # "South Africa": 23424942,
    # "Australia": 23424748,
}

# Setup twitter authentication and Twitter API object
twitter_authentication = tweepy.OAuth2BearerHandler(TWITTER_BEARER_TOKEN)
twitter_api = tweepy.API(twitter_authentication)


@dag(
    dag_id="twitter_get_trends",
    schedule="@hourly",
    start_date=START_DATE,

    catchup=False
)
def twitter_get_trends():
    @task(task_id="get_trends")
    def _get_trends(execution_date=None):
        for country in WOEID_MAPPING:
            try:
                logging.info(f"Searching for - {WOEID_MAPPING[country]} - {country}")
                trends = (twitter_api.get_place_trends(id=WOEID_MAPPING[country]))
                print(trends[0]["trends"])
            except tweepy.errors.NotFound as Error:
                logging.error(f"Could not find - {WOEID_MAPPING[country]} - {country} - {Error}")
        print(execution_date)

    # This is never called and only exists to populate the task display in the airflow UI along with
    trends = _get_trends()


twitter_get_trends()
