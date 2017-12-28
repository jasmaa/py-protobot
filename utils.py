import random
import json

def strip2alpha(text, alphabet):
    return "".join(c for c in text if c in alphabet)

def generate_id(alphabet):
    strf = ''
    for i in range(20):
        strf += alphabet[random.randint(0, len(alphabet)-1)]

    return strf

def extract_json(text):
    json_text = ''
    for i in range(len(text)):
        try:
            json.loads(text[i:])
        except:
            continue

        return json.loads(text[i:])

def union_dict(src, add):
    return dict(list(src.items()) + list(add.items()))

def cumsum(li, rate):
    cs = 0
    for num in li:
        cs += round(num*rate)
    return cs
