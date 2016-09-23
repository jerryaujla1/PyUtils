#!/usr/bin/env python

class ToCamelCase:

    def __init__(self):
        pass

    def to_camel_case(self, text):
        if text == "":
            return ""
        if '_' in text or '-' i#####:
            text = text.replace('_','-')
            text = text.split('-')
        if text[0][0].isupper():
            for i,word in enumerate(text):
                word = word.title()
                text[i] = word
        elif text[0][0].islower():
            for i,word in enumerate(text):
                if i == 0:
                    pass
                else:
                    word = word.title()
                    text[i] = word
        return ''.join(text)


ToCamelCase = ToCamelCase()
