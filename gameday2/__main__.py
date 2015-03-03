#!/usr/bin/env python27

from gameday2 import *

round1 = PluralityRound()
round2 = CumulativeRound()
round3 = ApprovalRound()
round4 = BordaRound()
round5 = PlurWithElimRound()
round6 = PairwiseElimRound()


def evaluate(gameRound):
    print gameRound.results


singular_votes = ['A', 'B', 'B', 'C', 'B' 'D']
round1 = gameday2.PluralityRound(singular_votes)
print round1.winner
print round1.order
print round1.results


ordered_votes = [
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D']
]
preferences = [gameday2.preference_from_order(vote) for vote in ordered_votes]
round4 = gameday2.BordaRound(preferences)
print round4.winner
print round4.order
print round4.results
