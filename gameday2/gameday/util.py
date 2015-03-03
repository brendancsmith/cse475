# def preference_from_order(order):
#     preference = {value: (index + 1) for index, value in enumerate(order)}
#     return preference


def extract_single_votes(voteDict):
    votes = []
    for teamVoteDict in voteDict.values():
        print teamVoteDict
        [vote] = [movie for movie in teamVoteDict
                  if teamVoteDict[movie] > 0]

        votes.append(vote)

    return votes


def extract_preference_votes(voteDict):
    pass
