from textblob import TextBlob

def correct_grammar(text):
    blob = TextBlob(text)
    return str(blob.correct())

text = input("Enter your Sentence: ")
corrected_text = correct_grammar(text)
print(f"Corrected: {corrected_text}")


# Enter your Sentence: makeket
# Corrected: market
