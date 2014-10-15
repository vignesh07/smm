from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import *
import time
import json
import pickle

import tweepy
import calendar
import datetime
ckey = 'rAV2mtafN5mDY2A7DwmJvQ'
csecret = 'a96tvDGKLDevbZDOTBp1CA1U5jSWeO61N0MLM3jM6G4'
atoken = '172501485-IHHymsvCrNcK5WuMygbJIxmncOl77ZK37q1JhD9o'
asecret = 'dO9c2sWqP0DIz7oozenaAhMKbrt7U6eIqxdkegoxMaRjd'

"""
class listener(StreamListener):
	def  on_data(self, data):
		try:
			#tweet = data.split(',"text":"')[1].split('","source')[0]
			#print tweet
			data_string=json.loads(data)
			#print data_string["text"]
			to_print = data_string["text"].encode('utf-8')
			print to_print
			data_loc=data_string["user"]
			data_loca=data_loc["location"].encode('utf-8')
			print data_loca
			
				
			saveFile = open('newDB.csv','a')
			saveFile.write(to_print)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException,e:
			print 'failed',str(e)
			time.sleep(5)
			
	def on_error(self,status):
		print status

"""

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api=tweepy.API(auth)
myid=172501485
idds=[]
curr=0
idds.append(myid)

check=[]


f=open('idlist_new.tsv','a')
while(len(check)<=1050):
	print "printig curr",curr
	if(idds[curr] in check):continue
	else:
		
		ids=[]
		print "printing idds of curr",curr
		
		current_cursor=""
		try:
			for page in tweepy.Cursor(api.followers_ids, user_id=idds[curr]).pages():
			#current_cursor = cursor.iterator.next_cursor
			    	cursor = tweepy.Cursor(api.followers_ids,user_id=idds[curr],cursor =  current_cursor)
			
				current_cursor = cursor.iterator.next_cursor
				#print repr(cursor)
				#print current_cursor
				ids.extend(page)
				#print page
	
			
		
		
	
		except tweepy.TweepError as e:
			print "code"
			print str(e.response.status)
		      	print "inside exception"
		      	if(e.response.status==88 or e.response.status==429):
				print "Rate limited. Checking when to try again"
				rate_info = api.rate_limit_status()['resources']
				reset_time = rate_info['followers']['/followers/ids']['reset']
				cur_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
				#wait the minimum time necessary plus a few seconds to be safe
				try_again_time = reset_time - cur_time + 5
				#Will try again in try_again_time seconds...
				print try_again_time
				time.sleep(try_again_time)
				continue
			if(e.response.status==179):
				print("Follower list is locked for ",idds[curr])
				continue
			
		for i in ids:
			
			idds.append(i)
			f.write(str(idds[curr]))
			f.write('\t')
			f.write(str(i))
			f.write('\n')
		check.append(idds[curr])		
		curr=curr+1;
		print "length is"
		print len(idds)
		



