import fileinput

# from pprint import pprint
import re


def get_match(words):

    max_w = max(words)

    print(sorted(words))

    trie = {}

    trie_ = trie

    for parts in max_w.split("*")

    for l in max_w:
        max_w
        base = trie.setdefault(l, {})
        trie_.setdefault(l, base)

        trie_ = trie_[l]

    print(trie)

    # print(max_w)
    # print(trie)

    # for w in words:
    #     # print("word: " + w)
    #     if w == max_w:
    #         continue

    #     trie_ = trie

    #     for l in w:
    #         if l == "*":
    #             continue
    #         elif l in trie_:
    #             trie_ = trie_[l]
    #         else:
    #             # print("{} {}".format(l, w))
    #             return "*"

    return max_w.replace('*', '')


def main():
    finput = fileinput.input()
    cases = int(next(finput))

    for case_no in range(1, cases+1):
        N = int(next(finput).strip())

        words = set(next(finput).strip() for _ in range(N))

        match = get_match(words)

        print('Case #{}: {}'.format(case_no, match))


if __name__ == '__main__':
    main()
