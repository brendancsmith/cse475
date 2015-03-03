#!/usr/bin/env python27

# run using `python -i .`

import gameday as gd

round1 = gd.PluralityRound()
round2 = gd.CumulativeRound()
round3 = gd.ApprovalRound()
round4 = gd.BordaRound()
round5 = gd.PlurWithElimRound()
round6 = gd.PairwiseElimRound()


def cast_votes(gdRound, filePath):
    voteDict = gd.read_votes(filePath)
    gdRound.cast_votes(voteDict)


def evaluate(gdRound):
    print "Winner:", gdRound.winner
    print "Order:", gdRound.order
    print "Result:", gdRound.results


cast_votes(round1, 'votes/round1.csv')
evaluate(round1)

# cast_votes(round1, 'votes/round1.csv')


# preferences = [gameday2.preference_from_order(vote) for vote in ordered_votes]
# round4 = gameday2.BordaRound(preferences)
