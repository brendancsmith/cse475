#!/usr/bin/env python27
# encoding: utf-8

from ballotbox.ballot import BallotBox
from ballotbox.singlewinner.plurality import FirstPastPostVoting


def vote_plurality_example():
    bb = BallotBox(method=FirstPastPostVoting)
    bb.batch_votes([("alice", 4000), ("bob", 3000), ("carol", 5000)])

    preference = bb.get_winner(position_count=3)
    return preference
