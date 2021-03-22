import random
from string import punctuation
from collections import defaultdict 
import os


DEBUG = False

def syllables(word: str) -> int:
    word = word.strip().lower().strip(punctuation)
    syllable_count = 0
    vowels = "aeiouy"
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




def get_word(part_of_speech, context, n_syllables, last = False):
    if last == True: 
        return random.choice(word_dict[part_of_speech]['ANY'][n_syllables])
    else:
        return random.choice(word_dict[part_of_speech][context][n_syllables])
#     except:
#         if DEBUG:
#             print('not found', part_of_speech, context, n_syllables)
#         return random.choice(word_dict[part_of_speech]['ANY'][n_syllables])



word_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: [])))

for file in os.listdir("./pos"):
    if file.endswith(".txt"):
        doc = open(os.path.join("./pos", file))
        part_of_speech = file[:-4]
        for word_context in doc:
            split = word_context.split(' ')
            word, s = syllables(split[0])
            for context in split[1:]:
                context = context.strip().upper()
                if context != 'ANY':
                    word_dict[part_of_speech][context][s].append(word)
            word_dict[part_of_speech]['ANY'][s].append(word)
                
if DEBUG: 
    for i in word_dict: 
        print(i)
        for j in word_dict[i]: 
            print('\t' + j)
            for k in word_dict[i][j]: 
                print('\t\t' + str(k))
                print('\t\t\t' + str(word_dict[i][j][k]))