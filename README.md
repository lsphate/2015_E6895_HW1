##EECS6895 Adv. Bigdata Analytics HW 1 - Sun-Yi Lin(sl3833)##
##Prob. 2 Wikipedia Articles##
####Step 1. Download & extract Wikipedia articles####
I downloaded the latest articles from <http://dumps.wikimedia.org/enwiki/latest/>. I choose the smallest file since we only need 1,000 pages. Then I use [Wikipedia Extractor](https://github.com/bwbaugh/wikipedia-extractor) to extract the text of each articles.

![Picture 1](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/Wikipedia/Pic1%20ExtractWikiText.png =740x)

Then we need to combine all the files into one text files by keeping the moderate numbers of outputs and use the command below:

![Pictures 2](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/Wikipedia/Pic2%20CombineFiles.png =740x)

The output format of **Wikipedia Extractor** is like below:


	<doc id="10002" url="http://en.wikipedia.org/wiki?curid=10002" title="Emil Kraepelin">
	Emil Kraepelin
	
	Emil Kraepelin (15 February 1856 – 7 October 1926) was a German psychiatrist. H.J. Eysenck's "Encyclopedia of Psychology" identifies him as the founder of modern scientific psychiatry, as well as of psychopharmacology and psychiatric genetics. Kraepelin believed the chief origin of psychiatric disease to be biological and genetic malfunction. His theories dominated psychiatry at the start of the twentieth century and, despite the later psychodynamic influence of Sigmund Freud and his disciples, enjoyed a revival at century's end.
	
	Family and early life.
	Kraepelin, the son of a civil servant, was born in 1856 in Neustrelitz, in the Duchy of Mecklenburg-Strelitz in Germany. He was first introduced to biology by his brother Karl, 10 years older and, later, the director of the Zoological Museum of Hamburg.
	
	...
	
	External links.
	For biographies of Kraepelin see:
	For English translations of Kraepelin's work see:
	
	</doc>
	
Each element contains the ID, title and text of one page, all the external links and other tags will be eliminated. 

####Step 2. Do TF-IDF####
After we got we use **pyspark** to create TD-IDF of these articles.

```
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

doc = sc.textFile("PATH_OF_INPUT").map(lambda line: line.split(' '))
hashingTF = HashingTF()
tf = hashingTF.transform(doc)
idf = IDF().fit(tf)
tfidf = idf.transform(tf).collect()

print(tfidf)
```

After several minutes of computing, we'll get the result:

![Picture 3](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/Wikipedia/Pic4%20DoingTF-IDF.png =740x)

***
##Prob. 3 Tweets Regarding 5 Companies##
####Step 1. Pull the real-time tweets data####
As the request of this problem, we need to choose 5 companies to collect the real-time tweets mentions them. In order to be allowed to collect the data from Twitter, we need to create a twitter application and obtain the access token to use in the **Twitter Streaming API**.

![Picture 4](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/5Twitter/Screen%20Shot%202015-02-15%20at%204.09.32%20PM.png =740x)

And also we need the third-party library called [Tweepy](http://www.tweepy.org/) to pull down the tweets. I followed the instruction form [here](http://adilmoujahid.com/posts/2014/07/twitter-analytics/), and wrote the Python application to get the tweets.

```
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_SECRET"
consumer_key = "YOUR_KEY"
consumer_secret = "YOUR_SECRET"

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status
        
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['KEYWORD'])
```

Where I replace the **KEYWORD** by the names of the 5 companies' name I choose: **BMW**, **Burberry**, **Heineken**, **Nikon** and **Tumblr**, then start these applications to grab the data.

![Picture 5](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/5Twitter/Pic1%20PullingData.png =740x)

The tweets pulled down are in these format:

	{"created_at":"Thu Feb 12 21:23:02 +0000 2015","id":565984447057895424,"id_str":"565984447057895424","text":"RT @PdeTannhauser: Hoy hace 8 a\u00f1os, en St Moritz, @NickHeidfeld se lo pasaba pipa con su BMW Sauber F1.07 CC @VirutasF1 http:\/\/t.co\/CDLQu1e\u2026",
	
	...
	
	"lang":"es","timestamp_ms":"1423776182318"}
	
####Step 2. Do TF-IDF####
Similar to the former problem, I use **pyspark** to create TF-IDF for each file.

```
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

doc = sc.textFile("INPUT TWITTER DATA").map(lambda line: line.split(' '))
hashingTF = HashingTF()
hashingTF.indexOf("COMPANY NAME")
tf = hashingTF.transform(doc)
idf = IDF().fit(tf)
tfidf = idf.transform(tf).collect()

print(tfidf)
```
And following are the results of each company:

![Picture 6](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/5Twitter/Pic3%20BMW_TFIDF.png =740x)
![Picture 7](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/5Twitter/Pic4%20Burberry_TFIDF.png =740x)
![Picture 8](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/5Twitter/Pic5%20Heineken_TFIDF.png =740x)
![Picture 9](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/5Twitter/Pic6%20Nikon_TFIDF.png =740x)
![Picture 10](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/5Twitter/Pic7%20Tumblr_TFIDF.png =740x)

***
##Prob. 4 The Stock Prices of 5 Companies##
####Step 1. Pull the real-time stock prices####
We need the [yahoo-finance](https://pypi.python.org/pypi/yahoo-finance) library to get the shared data of stocks from Yahoo Finance. I downloaded, installed the library, and wrote a Python application to get the data.

```
import time
from yahoo_finance import Share

price = Share('COMPANY CODE')
print price.get_open() + " at open"
print price.get_price() + " at " + price.get_trade_datetime()
for x in range(0, 28):
	time.sleep(60)
	price = Share('COMPANY CODE')
	print price.get_price() + " at " + price.get_trade_datetime()

print "Data pulling completed."
```

My choises of 5 companies are **Amazon**, **HP**, **IBM**, **Microsof**t and **Yahoo**. The datas I pulled down and outputed were in thi format:

	{'Sector': 'Services', 'end': '2015-02-17', 'CompanyName': None, 'symbol': 'AMZN', 'start': '1997-05-16', 'FullTimeEmployees': '154100', 'Industry': 'Catalog & Mail Order Houses'}
	378.10 at open
	375.2698 at 2015-02-17 18:01:00 UTC+0000
	375.12 at 2015-02-17 18:01:00 UTC+0000
	375.01 at 2015-02-17 18:03:00 UTC+0000
	375.01 at 2015-02-17 18:03:00 UTC+0000
	375.29 at 2015-02-17 18:05:00 UTC+0000
	375.25 at 2015-02-17 18:06:00 UTC+0000
	375.355 at 2015-02-17 18:07:00 UTC+0000
	375.19 at 2015-02-17 18:08:00 UTC+0000
	375.11 at 2015-02-17 18:09:00 UTC+0000
	375.05 at 2015-02-17 18:10:00 UTC+0000	
	374.90 at 2015-02-17 18:11:00 UTC+0000
	374.792 at 2015-02-17 18:12:00 UTC+0000
	374.58 at 2015-02-17 18:13:00 UTC+0000
	374.65 at 2015-02-17 18:14:00 UTC+0000
	375.33 at 2015-02-17 18:14:00 UTC+0000
	375.29 at 2015-02-17 18:16:00 UTC+0000
	375.14 at 2015-02-17 18:17:00 UTC+0000
	375.245 at 2015-02-17 18:18:00 UTC+0000
	375.54 at 2015-02-17 18:19:00 UTC+0000
	375.18 at 2015-02-17 18:20:00 UTC+0000
	375.18 at 2015-02-17 18:20:00 UTC+0000
	375.475 at 2015-02-17 18:22:00 UTC+0000
	375.68 at 2015-02-17 18:23:00 UTC+0000
	375.524 at 2015-02-17 18:24:00 UTC+0000
	375.36 at 2015-02-17 18:25:00 UTC+0000
	375.14 at 2015-02-17 18:26:00 UTC+0000
	375.248 at 2015-02-17 18:27:00 UTC+0000
	375.3852 at 2015-02-17 18:28:00 UTC+0000
	375.16 at 2015-02-17 18:28:00 UTC+0000
	Data pulling completed.

####Step 2. Use filter to find outliers####
I wrote an application to extract the data points that are 2 standard deviations away against the mean of the prices. The data that imported has been pre-processed to left the price numbers only:

```
import math

def stof(x):
    try:
        return float(x[0])
    except (ValueError, TypeError):
        return 0.0

price = sc.textFile("PRICE_DATA_NAME").map(lambda line: line.split(' '))
pricen = price.map(stof)
stats = pricen.stats()
stddev = stats.stdev()
mean = stats.mean()
outliers = pricen.filter(lambda x: math.fabs(x - mean) > 2 * stddev)
print outliers.collect()
```

![Picture 11](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/YFinance/Pic1%20PullData.png =740x)

And we can get the results of the outliers:


![Picture 12](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/YFinance/Pic2%20Amazon.png =650x)

![Picture 13](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/YFinance/Pic3%20HP.png =650x)

![Picture 14](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/YFinance/Pic4%20IBM.png =650x)

![Picture 15](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/YFinance/Pic5%20Microsoft.png =650x)

![Picture 16](file:///Volumes/JetDrive/Columbia/2015%20Spring/Adv%20Big%20Data%20Analytics/HW1/YFinance/Pic6%20Yahoo.png =650x)
