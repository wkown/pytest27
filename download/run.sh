#!/bin/bash
for((integer = 1; integer <= 100; integer++))
do
    python down-pic-index.py -u http://www.i1024larmo.cn/img/*.jpg -e 130
done