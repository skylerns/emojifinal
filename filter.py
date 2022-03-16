import os
import csv
import re
import pandas

from pandas import *

tweets = pandas.read_csv('hunnidscrape.csv', encoding = 'utf-8')

column = tweets.content
content = column.tolist()

print('Initial Sample:',len(content))


#First filter removes duplicates
content = list(dict.fromkeys(content))
print('First Filter (Removed duplicates):',len(content))

#Second filter - Removes tweets without text (tweets only containing emojis).
holder = []

for i in content:
  if bool(re.search(r"[a-zA-Z]", i)) == True:
    holder.append(i)

print('Second Filter (Removed non-text tweets):',len(content))

#Third Filter - Removes reply tweets (tweets that begin with the @ symbol). In our final team project, we found that these tweets are often context dependent. This makes them difficult to human annotate (without reading the whole thread), let alone filter by code.

  
for i in content:
  if bool(re.search(r"^@", i)) == True:
    holder.remove(i)

  

print('Third Filter (Removed replies):', len(holder))

#Fourth Filter - First filter to categorize tweets into 'fact' or 'opinion' groups.

#OPINIONSBELOW
#OPINIONSBELOW
#OPINIONSBELOW
#OPINIONSBELOW
#OPINIONSBELOW

holder2 = holder
opinions = []
facts = []

#this is looking for the phrase "keep it 100", which, from my personal experience, is often used to mark opinions.
for i in holder2:
  if bool(re.search(r"(?i)keep it", i)) == True:
    opinions.append(i)
    holder2.remove(i)

#"I think" is usually a good indicator of an opinion
for i in holder2:
  if bool(re.search(r"(?i)i think", i)) == True:
    opinions.append(i)
    holder2.remove(i)

#This is a group of words (non-adjectives) that I associate with opinions. 
for i in holder2:
  if bool(re.search(r"(?i)(me|my|opinion|agree|feel)", i)) == True:
    opinions.append(i)
    holder2.remove(i)

#List of subjective adjectives that would usually be associated with opinions
for i in holder2:
  if bool(re.search(r"(?i)(cool|special|funny|nice|good|great|silly|stupid|)", i)) == True:
    opinions.append(i)
    holder2.remove(i)
print("Opinions:",len(opinions))


#FACTSBELOW
#FACTSBELOW
#FACTSBELOW
#FACTSBELOW
#FACTSBELOW
#FACTSBELOW


for i in holder2:
  if bool(re.search(r"(?i)i know", i)) == True:
    facts.append(i)
    holder2.remove(i)

for i in holder2:
  if bool(re.search(r"(?i)research|factual|fact|understand|learn|know|comprehend|ignorant|actually|truth|reality|true|for sale", i)) == True:
    facts.append(i)
    holder2.remove(i)
print("Facts:",len(facts))


#Write to .csv files below
#factsfile
factsfile = open('facts.csv', 'a', newline='\n')

with factsfile:
  
  write = csv.writer(factsfile)
  write.writerow(facts)

#opinionsfile
opinionsfile = open('opinions.csv', 'a', newline='\n')

with opinionsfile:
  
  write = csv.writer(opinionsfile)
  write.writerow(opinions)

#unmarkedtweets
unmarkedfile = open('unmarked.csv', 'a', newline='\n')

with unmarkedfile:
  
  write = csv.writer(unmarkedfile)
  write.writerow(holder2)




