#!/usr/bin/env python27
# encoding: utf-8

from ballotbox.ballot import BallotBox
from ballotbox.singlewinner.plurality import FirstPastPostVoting
from ballotbox.singlewinner.preferential import BordaVoting


class Round(object):

    def __init__(self):
        super(self.__class__, self).__init__()

    def cast_votes(self, votes):
        for vote in votes:
            self.ballotBox.add_vote(vote)

    @property
    def winner(self):
        return [winner[1] for winner in self.ballotBox.get_winner()]


class PluralityRound(Round):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.ballotBox = BallotBox(method=FirstPastPostVoting)

    @property
    def results(self):
        return self.ballotBox.get_winner(position_count=None)

    @property
    def order(self):
        return [result[1] for result in self.results]


class CumulativeRound(Round):

    pass


class ApprovalRound(Round):

    pass


class BordaRound(Round):

    def __init__(self, votes):
        super(self.__class__, self).__init__()

        self.ballotBox = BallotBox(method=BordaVoting, mode='standard')

    @property
    def results(self):
        return self.ballotBox.method.get_counts(self.ballotBox)

    @property
    def order(self):
        return [result[1] for result in self.results]


class PlurWithElimRound(Round):

    pass


class PairwiseElimRound(Round):

    pass





def preference_from_order(order):
    preference = {value: (index + 1) for index, value in enumerate(order)}
    return preference


def vote_plurality_example():
    bb = BallotBox(method=FirstPastPostVoting)
    bb.batch_votes([("alice", 4000), ("bob", 3000), ("carol", 5000)])

    preference = bb.get_winner(position_count=3)
    return preference
