# 10-10 Common Words

# Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you'd like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer.

# You can use the 'count()' method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:

# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# >>> line.lower().count('row')

# Notice that converting the string to lowercase using 'lower()' catches all appearances of the word you're looking for, regardless of how it's formatted.

# Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'. Try counting 'the ', with a space in that string, and see how much lower your count is.

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'minions_of_the_crystal_sphere.txt'
count_common_words(filename, 'the ')

filename = 'uncle_toms_cabin.txt'
count_common_words(filename, 'the ')

