#!/usr/bin/env python27

# run using `python -i .`

import gameday as gd


def round_factory(_roundNum, _roundType):

    class Round(_roundType):

        roundNum = _roundNum
        outputFile = 'output/Round{}_WashingtonRedskins.csv'.format(_roundNum)

        def __init__(self):
            super(Round, self).__init__()
            self.history = []

        def evaluate(self):
            self.log_console()
            self.write_csv()

        def log_console(self):
            print "Round", self.roundNum
            print "Winner:", self.winner
            print "Order:", self.order
            print "Result:", self.results

        def write_csv(self):
            gd.write_csv(self.outputFile, gd.nest_list(self.order))

        def vote_from_csv(self, filePath):
            voteDict = gd.read_votes(filePath)
            self.history.append(voteDict)
            self.cast_votes(voteDict)

    return Round()

round1 = round_factory(1, gd.PluralityRound)
round2 = round_factory(2, gd.CumulativeRound)
round3 = round_factory(3, gd.ApprovalRound)
round4 = round_factory(4, gd.BordaRound)
round5 = round_factory(5, gd.PlurWithElimRound)
round6 = round_factory(6, gd.PairwiseElimRound)


# round1.vote_from_csv('votes/Round 1.csv')
# round1.evaluate()
# print

# round2.vote_from_csv('votes/Round 2.csv')
# round2.evaluate()
# print

# round3.vote_from_csv('votes/Round3.csv')
# round3.evaluate()
# print

# round4.vote_from_csv('votes/Round4.csv')
# round4.evaluate()
preferenceOrders = gd.extract_order_votes(
    gd.read_votes('votes/Round4.csv'))
print "Majority Preference:", gd.majority_preference(preferenceOrders)
print

# round5.vote_from_csv('votes/Round5a.csv')
# round5.evaluate()
# print "Eliminated:", round5.eliminate()
# print

movies = gd.split_csv_rows(gd.read_csv('votes/Round4.csv'))[1]
round6.pairs = gd.pair_up(movies)
round6.vote_from_csv('votes/Round4.csv')
round6.evaluate()
preferenceOrders = gd.extract_order_votes(
    gd.read_votes('votes/Round4.csv'))

print "Pareto Dominations:", gd.determine_pareto_dominations(preferenceOrders)
print

# TODO: handle candidates with no votes, so that they appear in the
#       results (I think there's an option to set candidates in BallotBox)
