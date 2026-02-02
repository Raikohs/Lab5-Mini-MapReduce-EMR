#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = line.strip().lower()
    words = re.findall(r'\b\w+\b', line)
    for word in words:
        if word:
            print(f"{word}\t1")
