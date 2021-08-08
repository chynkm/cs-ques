# solution https://www.youtube.com/watch?v=UVaGyYeH1Uw&t=344s
from collections import Counter


def steadyGene(gene):
    min_length_string = len(gene)
    occurences = Counter(gene)
    expected = len(gene) // 4

    for x in occurences:
        occurences[x] = max(0, occurences[x] - expected)

    if occurences['A'] == 0 and occurences['G'] == 0 \
            and occurences['C'] == 0 and occurences['T'] == 0:
        return 0

    found = Counter()
    tail = 0
    head = 0

    while head != len(gene):
        found[gene[head]] += 1
        if found['A'] >= occurences['A'] and \
                found['C'] >= occurences['C'] and \
                found['G'] >= occurences['G'] and \
                found['T'] >= occurences['T']:
            # this is a valid candidate
            min_length_string = min(min_length_string, head-tail+1)

            # try to shorten it
            while found[gene[tail]] > occurences[gene[tail]]:
                found[gene[tail]] -= 1
                tail += 1
                min_length_string = min(min_length_string, head-tail+1)

        head += 1

    return min_length_string


gene = "ACTGAAAG"
gene = "GAAATAAA"
print(steadyGene(gene))
