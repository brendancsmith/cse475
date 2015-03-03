from ballotbox.ballot import BallotBox
from ballotbox.singlewinner.plurality import FirstPastPostVoting
from ballotbox.singlewinner.preferential import BordaVoting

import util


class Round(object):

    @property
    def winner(self):
        return [winner[1] for winner in self.ballotBox.get_winner()]


class PluralityRound(Round):

    def __init__(self):
        super(PluralityRound, self).__init__()
        self.ballotBox = BallotBox(method=FirstPastPostVoting)

    @property
    def results(self):
        return self.ballotBox.get_winner(position_count=None)

    @property
    def order(self):
        return [result[1] for result in self.results]

    def cast_votes(self, voteDict):
        for teamVoteDict in voteDict.values():
            util.assert_single_vote(teamVoteDict)

        votes = util.extract_individual_votes(voteDict)

        for vote in votes:
            self.ballotBox.add_vote(vote)


class CumulativeRound(PluralityRound):

    def cast_votes(self, voteDict):
        # TODO: assert number of votes is == k

        votes = util.extract_individual_votes(voteDict)

        for vote in votes:
            self.ballotBox.add_vote(vote)


class ApprovalRound(PluralityRound):

    def cast_votes(self, voteDict):
        for teamVoteDict in voteDict.values():
            util.assert_approval_vote(teamVoteDict)

        votes = util.extract_individual_votes(voteDict)

        for vote in votes:
            self.ballotBox.add_vote(vote)


class BordaRound(Round):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.ballotBox = BallotBox(method=BordaVoting, mode='standard')

    @property
    def results(self):
        return self.ballotBox.method.get_counts(self.ballotBox)

    @property
    def order(self):
        return [result[1] for result in self.results]

    def cast_votes(self, voteDict):
        for teamVoteDict in voteDict.values():
            util.assert_borda_point_votes(teamVoteDict)

        votes = util.extract_preference_votes(voteDict)

        for vote in votes:
            self.ballotBox.add_vote(vote)


class PlurWithElimRound(Round):

    pass


class PairwiseElimRound(Round):

    pass
