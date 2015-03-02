#!/usr/bin/env python27

import gameday2

singular_votes = ['A', 'B', 'C', 'D']
round1 = gameday2.PluralityRound(singular_votes)
print round1.winner


ordered_votes = [
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D']
]
preferences = [gameday2.preference_from_order(vote) for vote in ordered_votes]
round4 = gameday2.BordaRound(preferences)
print round4.winner
