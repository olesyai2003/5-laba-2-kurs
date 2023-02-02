#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == "__main__":
    with open('txt.txt', 'r', encoding='utf-8-sig') as fileptr:
        sentence = fileptr.readlines()
    if len(sentence) < 10:
        print("Недостаточно строк", file=sys.stderr)

    else:
        print("Последние 10 строк", str(sentence[-10::]))