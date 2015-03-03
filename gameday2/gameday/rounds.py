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


class PlurWithElimRound(PluralityRound):

    def cast_votes(self, voteDict):
        super(PlurWithElimRound, self).cast_votes(voteDict)

    def eliminate(self):
        minVoteCount = self.results[-1][0]

        eliminatedMovies = [result[1] for result in self.results
                            if result[0] == minVoteCount]

        return eliminatedMovies


class PairwiseElimRound(Round):

    pairs = None

    eliminated = []

    def cast_votes(self, voteDict):
        for teamVoteDict in voteDict.values():
            util.assert_borda_point_votes(teamVoteDict)

        votes = util.extract_order_votes(voteDict)

        while True:
            advancers = []
            for pair in self.pairs:
                advancer = util.majority_order_preference(votes,
                                                          pair[0],
                                                          pair[1])
                advancers.append(advancer)

                eliminated = []
                eliminated += [pairItem for pairItem in pair
                               if pairItem is not advancer]

                self.eliminated += reversed(eliminated)

            if len(advancers) == 1:
                print advancers
                self._winner = advancers[0]
                break

            self.pairs = util.pair_up(advancers)

    @property
    def winner(self):
        return self._winner

    @property
    def order(self):
        return [self.winner] + list(reversed(self.eliminated))

    @property
    def results(self):
        return None
