#!/usr/bin/env python

import cytoolz.curried as cc
import itertools as it
from pprint import pprint as pp
import operator as op
import sys

answer = cc.pipe(
    sys.stdin.read()
    , str.split
    , cc.map(int)
    , lambda x: it.accumulate(x, op.add)
    , cc.last
)

print(answer)
