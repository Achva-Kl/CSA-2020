import binascii
import numpy as np
import Levenshtein


def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in xrange(size_x):
        matrix[x, 0] = x
    for y in xrange(size_y):
        matrix[0, y] = y

    for x in xrange(1, size_x):
        for y in xrange(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )
    print(matrix)
    return matrix[size_x - 1, size_y - 1]


def load_data():
    with open('first_signal.txt') as f:
        first_signal = eval(f.read())
    with open('second_signal.txt') as f:
        second_signal = eval(f.read())
    return first_signal, second_signal


def int2bin(char):
    return str(bin(int.from_bytes(char.encode(), 'big'))[2:]).zfill(8)


def find_distance_list(string, string_list):
    return list(map(lambda x: Levenshtein.distance(string, x), string_list))


def list2str(list_of_lists):
    return [''.join([str(i) for i in list_i]) for list_i in list_of_lists]


def create_distance_dict(string_list):
    all_indexes = list(range(256))
    all_indexes = [bin(i)[2:].zfill(8) for i in all_indexes]

    return {string: find_distance_list(string, list2str(string_list)) for string in all_indexes}


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    try:
        out = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    except UnicodeDecodeError:
        out = None
    return out


def yield_combos(lst):
    if lst:
        for el in lst[0]:
            for combo in yield_combos(lst[1:]):
                yield [el] + combo
    else:
        yield []


if __name__ == '__main__':

    first_signal, second_signal = load_data()
    first_signal_decoded = "Bang, zoom, straight to the moon!"

    decoded = []
    for num, character in enumerate(second_signal):
        # character = list(filter(lambda x: len(x) > 4, character))
        dist_list = create_distance_dict(character)
        mean_dist = {k: np.mean(np.array(val)) for k, val in dist_list.items()}
        bin_char = sorted(mean_dist.items(), key=lambda x: x[1])
        min_dist = list(filter(lambda x: x[1] == bin_char[0][1], bin_char))
        chars_bin = [i[0] for i in min_dist]
        chars = [text_from_bits(bits) for bits in chars_bin if text_from_bits(bits) is not None]

        decoded.append([num, None, ''.join(chars)])
        # print(''.join(chars), end=' \n')

    decoded[0][1] = 'C'
    decoded[1][1] = 'S'
    decoded[2][1] = 'A'
    decoded[3][1] = '{'

    index_ = [10, 18, 22, 28, 31, 35, 40, 44]
    for i in index_:
        decoded[i][1] = '_'
    for i, ch in enumerate(decoded):
        if len(ch[-1]) == 1:
            decoded[i][1] = ch[-1]
    decoded[20][1] = 'h'
    decoded[29][1] = 'w'
    decoded[30][1] = '3'
    decoded[32][1] = '4'
    decoded[34][1] = 'L'
    # decoded[17][1] = '4'
    decoded[24][1] = '4'
    decoded[41][1] = 'Y'
    decoded[43][1] = 't'

    decoded[46][2] = 'JLV'
    decoded[47][1] = '0TX'

    # decoded[-3][1] = 'Y'
    decoded[-2][1] = '?'
    decoded[-1][1] = '}'
    for i in decoded:
        print(i)
    decoded_to_print = decoded[36:-1]
    word = []
    for l in decoded_to_print:
        if l[1] == '_':
            break
        elif l[1] is not None:
            word.append(l[1])
        else:
            word.append(l[2])

    for permutation in yield_combos(word):
        print(''.join(permutation))

    flag = r"CSA{L1ttL3_P30pL3,_WhY_K4'Nt_w3_4LL_Ju5t_93t_4L0N9?}"
    print("flag:", flag)
