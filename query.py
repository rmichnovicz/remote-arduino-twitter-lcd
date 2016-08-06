import tweepy
import serial
current_tweet = 0
ser = serial.Serial('/dev/ttyACM0')
auth = tweepy.OAuthHandler("mRHxJLNd3HkLv1nZwDDXG86ft", "WdaYRME3j94uB7fWv4PbXeMgqF2HwNjgrh0uaY8UJ7d9zQ5tQy")
auth.set_access_token("126431754-2trZWVcvY1YieZfykhCR0WV3chU45kJ1b23lkg01", "kgGO7psjBmfr9LD5UKOfKGTqEUxrMEcmes4DGNTzs5CmL")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
query = raw_input("Enter a search query: ")
searched_tweets = api.search(q=query, count=100)

ser.write((searched_tweets[current_tweet].user.name + ": " + searched_tweets[current_tweet].text).encode('utf8'))

while True:
	s = ser.read()
	if s == "N":
		if current_tweet < 100: current_tweet += 1
		ser.write((searched_tweets[current_tweet].user.name + ": " + searched_tweets[current_tweet].text).encode('utf8'))

	if s == "P":
		if current_tweet > 1: current_tweet -= 1
		ser.write((searched_tweets[current_tweet].user.name + ": " + searched_tweets[current_tweet].text).encode('utf8'))
		

