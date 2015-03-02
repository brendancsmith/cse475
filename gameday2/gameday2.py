#!/usr/bin/env python27
# encoding: utf-8

from ballotbox.ballot import BallotBox
from ballotbox.singlewinner.plurality import FirstPastPostVoting
from ballotbox.singlewinner.preferential import BordaVoting


class Round(object):

    def __init__(self, votes):
        self.votes = votes

    def cast_votes(self):
        for vote in self.votes:
            self.ballotBox.add_vote(vote)


class PluralityRound(Round):

    def __init__(self, votes):
        super(self.__class__, self).__init__(votes)

        self.ballotBox = BallotBox(method=FirstPastPostVoting)
        self.cast_votes()

    @property
    def winner(self):
        return self.ballotBox.get_winner(position_count=None)


class BordaRound(Round):

    def __init__(self, votes):
        super(self.__class__, self).__init__(votes)

        self.ballotBox = BallotBox(method=BordaVoting, mode='standard')
        self.cast_votes()

    @property
    def winner(self):
        return self.ballotBox.get_winner()


def preference_from_order(order):
    preference = {value: (index + 1) for index, value in enumerate(order)}
    return preference


def vote_plurality_example():
    bb = BallotBox(method=FirstPastPostVoting)
    bb.batch_votes([("alice", 4000), ("bob", 3000), ("carol", 5000)])

    preference = bb.get_winner(position_count=3)
    return preference
