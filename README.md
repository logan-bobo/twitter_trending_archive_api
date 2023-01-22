# Twitter Trending Archive API
This API allows you to access trending twitter topics aggregated at the hourly, daily, weekly, monthly and yearly level, 
per region. Twitter does not currently allow this.

Core functionality:
 - Break down all trends to the regional, global or continental level.
 - Aggregate data to the hourly, daily, weekly, monthly and yearly level.

The API has two main components:
 - Web facing API that allows for the programmatic retrieval of trending data. 
 - Data retrieval and processing engine that will hourly communicate with the Twitter API to get all current trends across all countries. Transforming and writing that data to a database.

## Web API

## Data engine