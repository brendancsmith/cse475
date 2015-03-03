import csv


def read_csv(filePath):
    with open(filePath, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


def create_vote_dict(csvRows):
    teams = csvRows.pop(0)[1:]
    movies = [csvRow.pop(0) for csvRow in csvRows]

    columns = zip(*csvRows)

    voteDict = {}
    for i, team in enumerate(teams):
        votes = [int(valStr) for valStr in columns[i]]
        teamVoteDict = {movie: votes[j] for j, movie in enumerate(movies)}
        voteDict[team] = teamVoteDict

    return voteDict


def read_votes(filePath):
    rows = read_csv(filePath)
    return create_vote_dict(rows)

def write_to_file(filename, rows):
    # WRITE TO A CSV FILE
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
