import os
import pandas
import emoji


tweet_count = 1000
hunemoji = emoji.emojize(':hundred_points:')
keywords = [hunemoji]

start_date = "2021-01-22"
end_date = "2021-01-24"


for phrase in keywords:
  search_string = '\"' + phrase + '\"'
  os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'> hunnidscrape.json".format(tweet_count, start_date, search_string, end_date))


  tweets_dataframe = pandas.read_json('hunnidscrape.json', lines=True)
  
  if len(tweets_dataframe) == 0 :
    print("Tweet Count of ", search_string, " : 0")
  else:
    tweets_dataframe.to_csv('hunnidscrape.csv', sep=',', index=False, columns=['date', 'content', 'id', 'url'])
  print("Tweet Count of ", search_string, " : ", str(len(tweets_dataframe)))