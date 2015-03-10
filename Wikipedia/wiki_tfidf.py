from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
doc = sc.textFile("/Users/lsphate/Desktop/Wikipedia/1000articles.txt").map(lambda line: line.split(' '))
hashingTF = HashingTF()
tf = hashingTF.transform(doc)
idf = IDF().fit(tf)
tfidf = idf.transform(tf).collect()
print(tfidf)