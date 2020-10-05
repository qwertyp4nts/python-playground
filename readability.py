from cs50 import get_string
import re

text = get_string("Text: ")

letters = sum(c.isalpha() for c in text)

words = text.split()
numwords = len(words)

sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)

lper100w = letters / len(words) * 100
sper100w = len(sentences) / len(words) * 100

gradeIndex = 0.0588 * lper100w - 0.296 * sper100w - 15.8
if gradeIndex < 1:
    print("Before Grade 1")
elif gradeIndex > 16:
    print("Grade 16+")
else:
    print(f"Grade {str(round(gradeIndex))}")