def count_words(paragraph):
    words = paragraph.split()
    return len(words)

paragraph = "This is a sample paragraph with multiple words."
word_count = count_words(paragraph)
print("Number of words:", word_count)
