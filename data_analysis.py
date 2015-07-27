import json,re, pandas as pd, matplotlib.pyplot as plt
tweets_data_path = 'Give the PATH to the file in which text is stored'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
tweets['johncena'] = tweets['text'].apply(lambda tweet: word_in_text('johncena', tweet))
tweets['undertaker'] = tweets['text'].apply(lambda tweet: word_in_text('undertaker', tweet))
tweets['randyorton'] = tweets['text'].apply(lambda tweet: word_in_text('randyorton', tweet))
print tweets['johncena'].value_counts()[True]
print tweets['undertaker'].value_counts()[True]
print tweets['randyorton'].value_counts()[True]
wrestlers = ['johncena','undertaker', 'randyorton']
tweets_by_wrestlers = [tweets['johncena'].value_counts()[True], tweets['undertaker'].value_counts()[True], tweets['randyorton'].value_counts()[True]]

x_pos = list(range(len(wrestlers)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_wrestlers, width, alpha=1, color='b')

ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: johncena vs. undertaker vs. randyorton (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(wrestlers)
plt.grid()
