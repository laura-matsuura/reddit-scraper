# !/usr/bin/python
import praw
import csv

keywords = 'keywords.csv'
file = open(keywords, 'r')
# print file.read()
reader = csv.reader(file)
keywords_list = []

#loop through csv
for keyword_query in file:
    keywords_list.append(keyword_query)

print(keywords_list)

user_agent = ("test")
r = praw.Reddit(user_agent = user_agent)

# open a file for writing
csv_out = open('output.csv','wb')

#create csv writer object
mywriter = csv.writer(csv_out)

#looping through keywords_list to print out title, text, score
for query in keywords_list:
    results = r.search(query, subreddit=None,sort=None, syntax=None,period=None,limit=1)
    for result in results:
        mywriter.writerow([result.title])
        print(result.title)
        print(result.selftext)
        print(result.score)


csv_out.close()
