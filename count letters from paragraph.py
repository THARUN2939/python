import string
def count_letters(paragraph):
    count = 0
    for char in paragraph:
        if char.isalpha():
            count += 1
    return count

paragraph = "This is Tharun ."
letter_count = count_letters(paragraph)
print("Number of letters:", letter_count)