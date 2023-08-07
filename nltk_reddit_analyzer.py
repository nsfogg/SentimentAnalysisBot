import praw
from configparser import ConfigParser
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_headlines():
    # read configs
    config = ConfigParser()
    config.read('config.ini')

    user_agent = "Scraper 1 by /u/Ready_Asparagus8593"
    reddit = praw.Reddit(
        client_id=config["reddit"]["client_id"],
        client_secret=config["reddit"]["client_secret"],
        user_agent=user_agent
    )
    headlines = set()
    for submission in reddit.subreddit("politics").hot(limit=None):
        # print(submission.title)
        # print(submission.id)
        # print(submission.author)
        # print(submission.created_utc)
        # print(submission.score)
        # print(submission.upvote_ratio)
        # print(submission.url)
        headlines.add(submission.title)
    return headlines


# Cleaning Text Steps
# 1. Create text file and take text from it
# 2. Convert the letter into lowercase
# 3. Remove punctuation

text = ""
text_headlines = get_headlines()
length = len(text_headlines)

for headline in text_headlines:
    text = text + " " + headline

lower_case = text.lower()
# translate converts prev string to string
# str.maketrans replaces punctuation with empty strings
cleaned_text = lower_case.translate(str.maketrans("", "", string.punctuation))

# Tokenization
tokenized_words = word_tokenize(cleaned_text, "english")

final_words = []
# Removing stop words greatly decreases time to analyze
for word in tokenized_words:
    if word not in stopwords.words("english"):
        final_words.append(word)

# NLP Emotion Algorithm
# 1. Check if word in the final word list is also present in emotion.txt
# a. Open the emotion file
# b. Loop through each line and clear it
# c. Extract the word and emotion using split
# 2. If word is present -> Add emotion to emotion_list
# 3. Finally, count each emotion in emotion list

emotion_list = []
with open("emotions.txt", "r") as file:
    for line in file:
        clear_line = line.replace("\n", "").replace(",", "").replace("'", "").strip()
        word, emotion = clear_line.split(":")

        if word in final_words:
            emotion_list.append(emotion)

count = Counter(emotion_list)


def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score["neg"]
    pos = score["pos"]
    if neg > pos:
        print("Negative sentiment")
    elif pos > neg:
        print("Positive sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyze(cleaned_text)

# Plotting data

fig, ax1 = plt.subplots()
ax1.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()
