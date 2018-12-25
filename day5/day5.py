import re


def getUniqueSymbols(chain):
    unique_symbols = []
    for char in chain:
        if char.lower() not in unique_symbols:
            unique_symbols.append(char.lower())
    return unique_symbols


if __name__ == '__main__':
    input = tuple(open('./input', 'r'))[0]
    # input = 'dabAcCaCBAcCcaDA'
    unique_symbols = getUniqueSymbols(input)
    for symbol in unique_symbols:
        chain = re.sub('['+symbol.lower() + symbol.upper() + ']', '', input)
        while True:
            reactIndices = []
            index = 0

            while index < len(chain) - 1:
                currentChar = chain[index]
                nextChar = chain[index + 1]
                if currentChar != nextChar and currentChar.lower() == nextChar.lower():
                    reactIndices.append(index)
                    index += 2
                else:
                    index += 1

            if len(reactIndices) == 0:
                break
            else:
                i = 0
                newChain = chain[:reactIndices[0]]
                while i < len(reactIndices) - 1:
                    index = reactIndices[i]
                    nextIndex = reactIndices[i + 1]
                    newChain += chain[index + 2: nextIndex]
                    i += 1
                newChain += chain[reactIndices[len(reactIndices) - 1] + 2:]
                chain = newChain
                # print("New chain len = ", len(chain))
        print(symbol, len(chain))
