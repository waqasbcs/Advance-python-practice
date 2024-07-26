from textblob import TextBlob

text = input("Enter a sentence: ")
blob = TextBlob(text)

print("Original Text: ", text)
print("Sentiment: ", blob.sentiment)

# output

# Enter a sentence: i love python 
# Original Text:  i love python
# Sentiment:  Sentiment(polarity=0.5, subjectivity=0.6)