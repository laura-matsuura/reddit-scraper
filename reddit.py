# !/usr/bin/python
import praw
import csv

keywords = 'keywords.csv'
file = open(keywords, 'r')
# print file.read()
reader = csv.reader(file)
keywords_list = []

# how do i loop through a csv??
for keyword_query in file:
    keywords_list.append(keyword_query)

print(keywords_list)

user_agent = ("test")

r = praw.Reddit(user_agent = user_agent)

for query in keywords_list:
    results =r.search(query, subreddit=None,sort=None, syntax=None,period=None,limit=5)
    for result in results:
        print(result.title)
        print(result.selftext)
        print(result.score)
