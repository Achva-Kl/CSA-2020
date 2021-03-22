import math

def load_data():
    with open('tree.txt') as f:
        data = f.read()
    with open('pairs.txt') as f:
        pairs = eval(f.read())
    decoded = [ord(i) for i in data]
    return data, pairs, decoded


def find_close_parent(parents_dict, index_pair):
    for parent, children in parents_dict.items():
        if tree_indexes[index_pair[0]] in children and tree_indexes[index_pair[1]] in children:
            return parent

    if index_pair[0] > index_pair[1]:
        for parent, children in parents_dict.items():
            if index_pair[0] in children:
                return find_close_parent(parents_dict, [parent, index_pair[1]])
    elif index_pair[1] > index_pair[0]:
        for parent, children in parents_dict.items():
            if index_pair[1] in children:
                return find_close_parent(parents_dict, [parent, index_pair[0]])


if __name__ == '__main__':
    data, pairs, decoded = load_data()
    tree_indexes = []
    for j in range(len(data)):
        tree_indexes.append(j)

    parents_dict = {}

    for i in range(int(math.floor(len(tree_indexes))/2)):
        parents_dict[tree_indexes[i]] = [tree_indexes[i*2+1], tree_indexes[i*2+2]]

    print("the flag: ")
    for pair in pairs:
        common_index = find_close_parent(parents_dict, pair)
        print(data[common_index], end="")
