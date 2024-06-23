import re

def compare_strings(string1, string2):
    # Convert both strings to lowercase and remove leading and trailing blanks
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()

    # Define a regular expression pattern to remove punctuation
    # The \W character class matches any non-alphanumeric character, equivalent to [^a-zA-Z0-9_]
    # Adding the underscore (_) and the hyphen (-) to this class, we exclude them from removal
    pattern = r"[^\w\s]"
    
    # Remove all non-alphanumeric characters (and underscores and hyphens)
    string1 = re.sub(pattern, "", string1)
    string2 = re.sub(pattern, "", string2)

    # Debugging code to see the processed strings
    print(f"Processed string1: {string1}")
    print(f"Processed string2: {string2}")

    # Compare the processed strings
    return string1 == string2

# Test cases
print(compare_strings("Have a Great Day!", "Have a great day?"))  # True
print(compare_strings("It's raining again.", "its raining, again"))  # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three."))  # False
print(compare_strings("They found some body.", "They found somebody."))  # False
