if __name__ == '__main__':
    ids = tuple(open('./d2_input', 'r'))

    for id1 in ids:
        for id2 in ids:
            difs = 0
            for idx in range(len(id1) - 1):
                if id1[idx] != id2[idx]:
                    difs += 1
            if difs == 1:
                print(id1, id2, difs)
                break


    # double = 0
    # triple = 0
    #
    # for id1 in ids:
    #     chars = defaultdict(int)
    #     for char in id1:
    #         chars[char] += 1
    #     doubles = {k: v for k, v in chars.items() if v == 2}
    #     triples = {k: v for k, v in chars.items() if v == 3}
    #     # print(doubles, doubles.__len__(), triples, triples.__len__())
    #     if doubles.__len__() > 0:
    #         double += 1
    #     if triples.__len__() > 0:
    #         triple += 1
    #     # print("double = " + str(double), ", triple = " + str(triple))
    # print(double, triple)
    # checksum = double * triple
    # print(checksum)
