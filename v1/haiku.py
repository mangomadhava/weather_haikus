import sys
import clipboard
from haiku_utils import *
import random


valid_patterns = ['filler adjectives nouns',
                 'adjectives nouns verbs',
                 'adverbs verbs',
                 'adjectives nouns',
                 'fillers nouns',
                 'nouns adverbs verbs'
                 ]

def compositions(n,k):
    if n < 0 or k < 0:
        return
    elif k == 0:
    # the empty sum, by convention, is zero, so only return something if
    # n is zero
        if n == 0:
            yield []
            return
        elif k == 1:
            yield [n]
            return
    else:
        for i in range(0,n+1):
            for comp in compositions(n-i,k-1):
                yield [i] + comp

def complete_line(n_syllables, context_list):
    while True:
        chosen_context = random.choice(context_list)
        chosen_pattern = random.choice(valid_patterns).split(' ')
        n = len(chosen_pattern)
        comp = list(compositions(n_syllables, n))
        # remove ones with 0 syllables
        comp = [x for x in comp if 0 not in x]
        random.shuffle(comp)
        line_text = ''
        c = 0
        for syl_pattern in comp:
            try:
                for i,syl_count in enumerate(syl_pattern):
                    if c == 3:
                        word = get_word(chosen_pattern[i], chosen_context, syl_count, last = True)
                        line_text = line_text + word + ' '
                    else:
                        word = get_word(chosen_pattern[i], chosen_context, syl_count)
                        line_text = line_text + word + ' '
            except:
                c = c + 1
                line_text = ''
                pass
            if line_text != '':
                return line_text + '\n'
    
'''
usage: 
argv are contexts
contexts are based on text files provided in pos folder

CLEAR
CLOUDY
SHOWERS
SNOW

HOT
WARM
COLD
'''
if __name__ == '__main__':
    haiku_full = ''
    contexts = []
    for name in sys.argv[1:]:
        contexts.append(name.strip().upper())
    haiku_full = complete_line(5, contexts) + complete_line(7, contexts) + complete_line(5, contexts)
    clipboard.set(haiku_full)
    print(haiku_full)