from math import log

def extract_data_from_file(path):
    """Get file path and get table from file."""
    try:
        with open(path, 'r') as file:
            data = []
            for line in file:
                line = line.split(',')
                data.append(list(map(int, line)))
    except EOFError as err:
        exit(err)
    else:
        return data

def count_decision_values(data):

    decisions = dict()
    for row in data:
        decision = row[len(row)-1]
        if decision not in decisions:
            decisions[decision] = 1
        else:
            decisions[decision]+=1
    return decisions

def count_probability(counted_decisions):
    probability = dict()
    all_decisions = sum(counted_decisions.values())
    for k, v in counted_decisions.items():
        probability[k] = v/all_decisions
    return probability

def count_entrophy(probability):
    entrophy = 0
    for v in probability.values():
        entrophy += v*log(v)
    return entrophy * -1

if __name__ == "__main__":
    data = extract_data_from_file('./data.txt')
    counted = count_decision_values(data)
    print(counted)
    probability = count_probability(counted)
    print(probability)
    entrophy = count_entrophy(probability)
    print(entrophy)