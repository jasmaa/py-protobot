""" Utils """

import random
import json

""" Strips string of non-alphabet characters """
def strip2alpha(text, alphabet):
    return "".join(c for c in text if c in alphabet)

""" Generates a 20 character id """
def generate_id(alphabet):
    strf = ''
    for i in range(20):
        strf += alphabet[random.randint(0, len(alphabet)-1)]

    return strf

""" Tries to extract json from string """
def extract_json(text):
    json_text = ''
    for i in range(len(text)):
        try:
            json.loads(text[i:])
        except:
            continue

        return json.loads(text[i:])

""" Unions two dictionaries """
def union_dict(src, add):
    return dict(list(src.items()) + list(add.items()))

""" Cumulative sum with multiplier """
def cumsum(li, rate):
    cs = 0
    for num in li:
        cs += round(num*rate)
    return cs
