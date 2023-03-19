"""
Convert string to camel case:
https://www.codewars.com/kata/517abf86da9663f1d2000003/python

"""


def to_camel_case(text):
    text = text.replace("_", " ").replace("-", " ").split()
    if len(text) > 0:
        upper_words = [i.title() for i in text[1:]]
        return text[0] + "".join(upper_words)
    else:
        return ""
