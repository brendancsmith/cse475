import csv
from copy import deepcopy


def read_csv(filePath):
    with open(filePath, 'rbU') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


def split_csv_rows(csvRows):
    rows = deepcopy(csvRows)

    teams = rows.pop(0)[1:]
    movies = [row.pop(0) for row in rows]
    innerColumns = zip(*rows)

    return teams, movies, innerColumns


def create_vote_dict(csvRows):
    teams, movies, innerColumns = split_csv_rows(csvRows)

    voteDict = {}
    for i, team in enumerate(teams):

        def val(valStr):
            val = None
            if not len(valStr):
                val = 0
            else:
                val = int(valStr)
            return val

        votes = [val(valStr) for valStr in innerColumns[i]]
        teamVoteDict = {movie: votes[j] for j, movie in enumerate(movies)}
        voteDict[team] = teamVoteDict

    return voteDict


def read_votes(filePath):
    rows = read_csv(filePath)
    return create_vote_dict(rows)


def write_csv(filePath, rows):
    # WRITE TO A CSV FILE
    with open(filePath, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def nest_list(outList):
    return [[item] for item in outList]
