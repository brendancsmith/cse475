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


#TODO: Change rows to be the preferential ordering from each round
rows = [["Movie 8", 10093], ["Movie 12", 1231], ["Movie 1", 8310], ["Movie 3", 10]]

print "Round 1"
cast_votes(round1, 'votes/round1_test.csv')
evaluate(round1)

filename = 'Round1_WashingtonRedskins.csv'
gd.write_to_file(filename, rows)

print "Round 2"
cast_votes(round2, 'votes/round2_test.csv')
evaluate(round2)

filename = 'Round2_WashingtonRedskins.csv'
gd.write_to_file(filename, rows)

print "Round 3"
cast_votes(round3, 'votes/round3_test.csv')
evaluate(round3)

filename = 'Round3_WashingtonRedskins.csv'
gd.write_to_file(filename, rows)

print "Round 4"
cast_votes(round4, 'votes/round4_test.csv')
evaluate(round4)

filename = 'Round4_WashingtonRedskins.csv'
gd.write_to_file(filename, rows)

print "Round 5"
cast_votes(round5, 'votes/round5_test.csv')
evaluate(round5)
print "Eliminated:", round5.eliminate()

filename = 'Round5_WashingtonRedskins.csv'
gd.write_to_file(filename, rows)

print "Round 6"
cast_votes(round6, 'votes/round6_test.csv')
evaluate(round6)

filename = 'Round6_WashingtonRedskins.csv'
gd.write_to_file(filename, rows)



# TODO: tie-break alphabetically
# TODO: handle candidates with no votes, so that they appear in the
#       results (I think there's an option to set candidates in BallotBox)


# preferences = [gameday2.preference_from_order(vote) for vote in ordered_votes]
# round4 = gameday2.BordaRound(preferences)
