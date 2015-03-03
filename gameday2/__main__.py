#!/usr/bin/env python27

# run using `python -i .`

import gameday as gd

OUTPUT_FILEPATH_FORMAT = 'output/Round{}_WashingtonRedskins.csv'

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

def nest_list(order):
    return [[candidate] for candidate in order]

print "Round 1"
cast_votes(round1, 'votes/round1_test.csv')
evaluate(round1)
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(1), nest_list(round1.order))

print "Round 2"
cast_votes(round2, 'votes/round2_test.csv')
evaluate(round2)
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(2), nest_list(round2.order))

print "Round 3"
cast_votes(round3, 'votes/round3_test.csv')
evaluate(round3)
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(3), nest_list(round3.order))

print "Round 4"
cast_votes(round4, 'votes/round4_test.csv')
evaluate(round4)

filename = 'Round4_WashingtonRedskins.csv'
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(4), nest_list(round4.order))

print "Round 5"
cast_votes(round5, 'votes/round5_test.csv')
evaluate(round5)
print "Eliminated:", round5.eliminate()

gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(5), nest_list(round5.order))

print "Round 6"
movies = gd.split_csv_rows(gd.read_csv('votes/round4_test.csv'))[1]
round6.pairs = gd.pair_up(movies)
cast_votes(round6, 'votes/round4_test.csv')
evaluate(round6)
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(6), nest_list(round6.order))

# TODO: handle candidates with no votes, so that they appear in the
#       results (I think there's an option to set candidates in BallotBox)
