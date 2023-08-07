# Cleaning Text Steps
# 1. Create text file and take text from it
# 2. Convert the letter into lowercase
# 3. Remove punctuation

import string
from collections import Counter
import matplotlib.pyplot as plt

text = open("read.txt", encoding="utf-8").read()
lower_case = text.lower()
# translate converts prev string to string
# str.maketrans replaces punctuation with empty strings
cleaned_text = lower_case.translate(str.maketrans("", "", string.punctuation))

# Tokenization

tokenized_words = cleaned_text.split()
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words = []
# Removing stop words greatly decreases time to analyze
for word in tokenized_words:
    if word not in stop_words:
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

# Plotting data

fig, ax1 = plt.subplots()
ax1.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()
