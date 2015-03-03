def assert_single_vote(teamVoteDict):
    voteSum = sum(teamVoteDict.values())
    assert 0 <= voteSum <= 1


def assert_approval_vote(teamVoteDict):
    for value in teamVoteDict.values():
        assert 0 <= value <= 1


def assert_borda_point_votes(teamVoteDict):
    numCandidates = len(teamVoteDict)

    orderedVotes = sorted(teamVoteDict.values())

    for i in range(numCandidates):
        assert orderedVotes[i] == i


def extract_individual_votes(voteDict):
    votes = []
    for teamVoteDict in voteDict.values():
        for movie, voteCount in teamVoteDict.items():
            votes += [movie] * voteCount

    return votes


def extract_preference_votes(voteDict):
    # assumes votes are recorded as points, with decending order
    votes = []
    for teamVoteDict in voteDict.values():
        order = sorted(teamVoteDict.keys(),
                       key=lambda k: teamVoteDict[k],
                       reverse=True)

        preference = preference_from_order(order)
        votes.append(preference)

    return votes


def preference_from_order(order):
    preference = {value: (index + 1) for index, value in enumerate(order)}
    return preference
