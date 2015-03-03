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


#TODO: Change rows to be the preferential ordering from each round
rows = [["Movie 8", 10093], ["Movie 12", 1231], ["Movie 1", 8310], ["Movie 3", 10]]

print "Round 1"
cast_votes(round1, 'votes/round1_test.csv')
evaluate(round1)
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(1), rows)

print "Round 2"
cast_votes(round2, 'votes/round2_test.csv')
evaluate(round2)
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(2), rows)

print "Round 3"
cast_votes(round3, 'votes/round3_test.csv')
evaluate(round3)
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(3), rows)

print "Round 4"
cast_votes(round4, 'votes/round4_test.csv')
evaluate(round4)

filename = 'Round4_WashingtonRedskins.csv'
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(4), rows)

print "Round 5"
cast_votes(round5, 'votes/round5_test.csv')
evaluate(round5)
print "Eliminated:", round5.eliminate()

gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(5), rows)

print "Round 6"
movies = gd.split_csv_rows(gd.read_csv('votes/round4_test.csv'))[1]
round6.pairs = gd.pair_up(movies)
cast_votes(round6, 'votes/round4_test.csv')
evaluate(round6)
gd.write_csv(OUTPUT_FILEPATH_FORMAT.format(6), rows)



# TODO: tie-break alphabetically
# TODO: handle candidates with no votes, so that they appear in the
#       results (I think there's an option to set candidates in BallotBox)


# preferences = [gameday2.preference_from_order(vote) for vote in ordered_votes]
# round4 = gameday2.BordaRound(preferences)
