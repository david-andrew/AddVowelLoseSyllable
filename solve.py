"""
Find a word in the English language to which you can add a vowel, resulting in another word that has fewer syllables.

By “add a vowel,” I mean insert one additional letter — a vowel — somewhere in the word 
(or at the beginning or end), while keeping the ordering of all the other letters the same. 
For example, you could add a vowel to the word “TASTY” to get the word “TOASTY.” 
However, both words are two syllables, meaning this is not the solution.
"""

import pdb

ipa_diphthongs = [
    "eɪ",
    "oʊ",
    "aʊ",
    "ɪə",
    "eə",
    "ɔɪ",
    "aɪ",
    "ʊə",
]

ipa_vowels = [
    "æ",
    "ɑ",
    "ɒ",
    "ʌ",
    "ɛ",
    "ɪ",
    "i",
    "ɔ",
    "ʊ",
    "u",
    "ə",
    "ɚ",
    "ɜ",
    "ɝ",
]

latin_vowels = 'aeiou'


def download_dictionary():
    #todo: curl https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/en_US.txt > en_US.txt
    pdb.set_trace()

def count_syllables(raw_ipa):
    #split at ',' for words with multiple pronunciations
    counts = []
    for ipa in raw_ipa.split(','):
        count = 0
        for l, l_next in zip(ipa, ipa[1:] + '\0'):
            if l in ipa_vowels and l + l_next not in ipa_diphthongs:
                count += 1
        counts.append(count)

    return counts

def generate_syllable_counts():
    counts = {}
    with open('en_US.txt') as f:
        lines = f.read().strip().split('\n')
        for line in lines:
            word, raw_ipa = line.split('\t')
            counts[word] = count_syllables(raw_ipa)
            # print(f"{word} ({raw_ipa}) has {counts[word]} syllables")
    
    return counts

def any_less_than(counts0, counts1):
    """check if any values in counts1 are less than any values in counts0"""
    for v0 in counts0:
        for v1 in counts1:
            if v1 < v0:
                return True
    return False

def main():
    english = generate_syllable_counts()

    for word1, counts1 in english.items():
        for i, l in enumerate(word1):
            if l in latin_vowels and word1[:i] + word1[i+1:] in english:
                word0 = word1[:i] + word1[i+1:]
                counts0 = english[word0]
                if any_less_than(counts0, counts1):
                    print(f"found a solution: {word0} -> {word1} ({counts0} -> {counts1})")
                

if __name__ == '__main__':
    main()