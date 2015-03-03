from copy import copy
from collections import Counter

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


def extract_order_votes(voteDict):
    # assumes votes are recorded as points, with decending order
    votes = []
    for teamVoteDict in voteDict.values():
        order = sorted(teamVoteDict.keys(),
                       key=lambda k: teamVoteDict[k],
                       reverse=True)

        votes.append(order)

    return votes


def extract_preference_votes(voteDict):
    votes = []
    orders = extract_order_votes(voteDict)

    for order in orders:
        preference = preference_from_order(order)
        votes.append(preference)

    return votes


def preference_from_order(order):
    preference = {value: (index + 1) for index, value in enumerate(order)}
    return preference


def pair_up(movies):
    moviesCopy = copy(movies)

    # make safe for odd length
    # moviesCopy.append(None)

    return zip(moviesCopy[::2], moviesCopy[1::2])


def compare_order_preference(orders, movie1, movie2):
    balance = 0

    for order in orders:
        isFirstPreferred = order.index(movie1) > order.index(movie2)
        balance += 1 if isFirstPreferred else -1

    # movie1 will win ties
    return movie1 if balance >= 0 else movie2


def determine_pareto_pair_domination(orders, movie1, movie2):
    pareto1 = True
    pareto2 = True

    for order in orders:
        isFirstPreferred = order.index(movie1) > order.index(movie2)

        if isFirstPreferred:
            pareto2 = False
        else:
            pareto1 = False
    
    assert not (pareto1 and pareto2)

    if pareto1:
        return (movie1, movie2)
    elif pareto2:
        return (movie2, movie1)
    else:
        return None


def majority_preference(orders):
    topPreferences = [order[0] for order in orders]
    majorityPreference = Counter(topPreferences).most_common(1)
    return majorityPreference


def determine_pareto_dominations(orders):
    movies = sorted(orders[0])

    paretoPairs = []

    for pair in pair_up(movies):
        paretoPair = determine_pareto_pair_domination(orders, pair[0], pair[1])

        if paretoPair:
            paretoPairs.append(paretoPair)

    return paretoPairs
    

def alphabetize_results(results):
    return sorted(results, key=lambda x: (-x[0], x[1]))
