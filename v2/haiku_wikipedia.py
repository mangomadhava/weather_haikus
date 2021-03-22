import random
from string import punctuation
from collections import defaultdict 
import os
import wikipedia 
import sys
import clipboard

def syllables(word: str) -> int:
    word = word.strip().lower().strip(punctuation)
    syllable_count = 0
    vowels = "aeiouy"
    if len(word) == 0:
        return '', 0
    if word[0] in vowels:
        syllable_count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllable_count += 1
    if word.endswith("e"):
        syllable_count -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
    return word, syllable_count

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def find_phrase(syl, wiki_page):
    possible_phrases = []
    for i,word in enumerate(wiki_page):
        so_far = 0
        partial_phrase = ''
        c = 0
        while True:
            if (i + c) >= len(wiki_page):
                break
            current_word = wiki_page[i + c]
            if hasNumbers(current_word):
                break
                
            w, s = syllables(current_word)
            if s != 0:                
                so_far = so_far + s
                partial_phrase = partial_phrase + w + ' '

            if so_far == syl:
                possible_phrases.append(partial_phrase)
                break
                
            if so_far > syl:
                break
            c = c + 1
    return random.choice(possible_phrases)
    


def complete_line(syl, contexts, pages):
    context = random.choice(contexts)
    page = pages[context]
    wiki_page = wikipedia.page(page)
    wiki_page = wiki_page.content.split()
    l = len(wiki_page)
    wiki_page = wiki_page[:int(l/8)]
    print(wiki_page)
    phrase = find_phrase(syl, wiki_page)
    return phrase + '\n'


if __name__ == '__main__':
    haiku_full = ''
    contexts = []
    for name in sys.argv[1:]:
        contexts.append(name.strip().upper())
    pages = {}
    print(contexts)
    for line in open('context_dict.txt'):
        s = line.split()
        pages[s[0]] = s[1:]
    haiku_full = complete_line(5, contexts, pages) + complete_line(7, contexts, pages) + complete_line(5, contexts, pages)
    clipboard.set(haiku_full)
    print(haiku_full)


