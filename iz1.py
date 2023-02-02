#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open('text.txt', 'r', encoding='utf-8-sig') as fileptr:
        sentence = fileptr.readlines()
        reverse_sentence = list(reversed(sentence))
        print(reverse_sentence)