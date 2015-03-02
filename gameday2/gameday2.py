#!/usr/bin/env python27
# encoding: utf-8

from ballotbox.ballot import BallotBox
from ballotbox.singlewinner.plurality import FirstPastPostVoting


class Round(object):

    method = None

    def __init__(self, votes):
        self.votes = votes

    @property
    def winner(self):
        bb = BallotBox(method=self.method)
        for vote in self.votes:
            bb.add_vote(vote)

        return bb.get_winner(position_count=None)


class PluralityRound(Round):

    method = FirstPastPostVoting


def preference_from_order(order):
    preference = {value: (index + 1) for index, value in enumerate(order)}
    return preference


def vote_plurality_example():
    bb = BallotBox(method=FirstPastPostVoting)
    bb.batch_votes([("alice", 4000), ("bob", 3000), ("carol", 5000)])

    preference = bb.get_winner(position_count=3)
    return preference
