#!/usr/bin/env python27

import gameday2

votes = ['A', 'B', 'C', 'D']

round1 = gameday2.PluralityRound(votes)

print round1.winner
