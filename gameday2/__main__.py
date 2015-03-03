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


print "Round 1"
cast_votes(round1, 'votes/round1_test.csv')
evaluate(round1)

print "Round 2"
cast_votes(round2, 'votes/round2_test.csv')
evaluate(round2)

print "Round 3"
cast_votes(round3, 'votes/round3_test.csv')
evaluate(round3)

print "Round 4"
cast_votes(round4, 'votes/round4_test.csv')
evaluate(round4)

# TODO: tie-break alphabetically
# TODO: handle candidates with no votes, so that they appear in the
#       results (I think there's an option to set candidates in BallotBox)


# preferences = [gameday2.preference_from_order(vote) for vote in ordered_votes]
# round4 = gameday2.BordaRound(preferences)
