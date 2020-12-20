import sys
import copy
import pytest
import random

# sys.setrecursionlimit(1000)


class ImposterLineError(Exception):
    pass


class Rule:

    @staticmethod
    def from_line(line):
        # print(line)
        num, rule = line.split(":", 1)

        num = int(num)
        rule = rule.strip()

        letter = None
        variants = None

        if rule.startswith('"'):
            assert len(rule) == 3
            letter = rule[1]

            return LetterRule(num, letter)
        elif "|" in rule:
            variants = [
                [int(v) for v in var.strip().split(" ")]
                for var in rule.split("|")
            ]
        else:
            variants = [[int(v) for v in rule.strip().split(" ")]]

        return VariantRule(num, variants)


class LetterRule(Rule):
    def __init__(self, num, letter):
        self.num = num
        self.letter = letter

    def __repr__(self):
        return "LetterRule(num={}, letter={})".format(self.num,
                                                      self.letter)

    def matches(self, message, rules, last_matches=None):
        print("Matched LetterRule message={} letter={}".format(message, self.letter))
        is_matches = message.startswith(self.letter)

        # second retval is number of letters
        return is_matches, message[1:], [[message[:1]]]


class VariantRule(Rule):

    def __init__(self, num, variants):
        self.num = num
        self.variants = variants

    def __repr__(self):
        return "VariantRule(num={},variants={})".format(self.num,
                                                        self.variants)

    def matches_variant(self, message, variant, rules, last_matches=None):
        # CREATOR! I COULD BE STATIC.
        #          -- your tiny func
        if not last_matches:
            last_matches = []

        curr_message = message

        prev_match = last_matches[-1:]

        print("-- prev_match/variant/num = {}/{}/{}".format(prev_match, variant, self.num))

        if prev_match and self.num in prev_match[0] and self.num in variant:
            print("return0")
            return False, "", []

        print("-- matches_variant last_matches={} /// {}".format(last_matches, last_matches[-1:]))

        left_variant, right_variant = variant, []

        try:
            idx = variant.index(self.num)
            left_variant, right_variant = variant[:idx], variant[idx + 1:]

            assert right_variant.count(self.num) == 0, "Multiple rec not allowed! {}".format(variant)
        except:
            pass

        print("{}/{}".format(left_variant, right_variant))

        new_matches_full = []

        if variant == [self.num]:
            return False, "", []

        for v in left_variant:
            if not curr_message:
                print("return1 - empty message v={}".format(v))
                return False, "", []

            is_matches, curr_message, new_matches = rules[v].matches(curr_message, rules, last_matches + [left_variant])

            print("res1 {}/{}/{}".format(is_matches, curr_message, new_matches))

            if not is_matches:
                print("return1 v={} Not matching to curr={}".format(v, curr_message))
                return False, "", []

            new_matches_full.extend(new_matches)

        curr_message = curr_message[::-1]

        for v in right_variant[::-1]:
            if not curr_message:
                print("return2")
                return False, "", []

            is_matches, curr_message, new_matches = rules[v].matches(curr_message, rules, last_matches + [right_variant])

            print("res2 {}/{}/{}".format(is_matches, curr_message, new_matches))

            if not is_matches:
                print("return2")
                return False, "", []

            new_matches_full.extend(new_matches)

        # new_matches_full.remove(self.num)

        return True, curr_message[::-1], last_matches + new_matches_full

    def matches(self, message, rules, last_matches=None):
        if not last_matches:
            last_matches = []

        # Simple circuit breaker
        if message == "" and [self.num] in self.variants:
            return True, message, last_matches

        should_repeat_rule = False

        rnd0 = int(random.random() * 1000)

        print("{} message={}".format(rnd0, message))

        for variant in self.variants:
            should_repeat_rule = should_repeat_rule or (self.num in variant)

            rnd = int(random.random() * 1000)

            print("{}/{} Prematch variant={} last_matches={}".format(rnd0, rnd, variant, last_matches))

            is_matches, remaining_part, new_matches = self.matches_variant(message, variant,
                                                                           rules, last_matches)

            # print("{} is_matches={} var={} {}".format(rnd, is_matches, remaining_part, new_matches))
            print("res0 {}/{}/{}".format(is_matches, remaining_part, new_matches))

            if is_matches:
                print("{}/{} Matched! remaining_part={} {}".format(rnd0, rnd, remaining_part, new_matches))
                if remaining_part and should_repeat_rule:
                    print("{}/{} Repeating rule {}".format(rnd0, rnd, self))
                    return self.matches(remaining_part, rules, last_matches + new_matches)

                return is_matches, remaining_part, last_matches + new_matches

        print("{} False".format(rnd0))

        return False, "", []


def monster_messages(data):
    data_it = iter(data)

    rules = {}

    for line in data_it:
        line = line.strip()

        if not line:
            break

        rule = Rule.from_line(line)

        rules[rule.num] = rule
    # print(rules)

    main_rule = rules[0]

    matches = 0

    for line in data_it:
        line = line.strip()

        is_matches, remaining_part, new_matches = main_rule.matches(line, rules)

        print("{}/{}".format(is_matches, remaining_part))

        if is_matches and not remaining_part:
            matches += 1

    return matches


BASE_TEST = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".splitlines()

MY_TEST = """0: 1 2 | 2 1
1: "a"
2: "b"

ab
ba
aa
bb""".splitlines()

MY_TEST2 = """0: 2 2
2: 3 3 | 4
3: "a"
4: "b"

aab""".splitlines()

CYCLE_TEST = """0: 0 | 1
1: "a"

aaa""".splitlines()

SIMPLE_REPEAT = """0: 1 1 | 2
1: "a"
2: "c"

aa""".splitlines()

CYCLE_TEST_2 = """0: 0 2 | 1
1: "a"
2: "b"

ab""".splitlines()

CYCLE_TEST_3 = """0: 0 2 | 1
1: "a"
2: "b"

ab""".splitlines()


@pytest.mark.parametrize("data,expected", [
    pytest.param(BASE_TEST, 2, id="base"),
    pytest.param(MY_TEST, 2, id="my"),
    pytest.param(MY_TEST2, 1, id="my2"),
    pytest.param(CYCLE_TEST, 1, id="cycle"),
    pytest.param(CYCLE_TEST_2, 1, id="cycle2"),
    pytest.param(CYCLE_TEST_3, 1, id="cycle3"),
    pytest.param(SIMPLE_REPEAT, 1, id="simple_repeat")

]
)
def test_monster_messages(data, expected):
    print("\n".join(data))
    assert monster_messages(data) == expected


if __name__ == "__main__":
    # 190
    # That's the right answer! You are one gold star closer to saving your vacation. [Continue to Part Two]
    num = monster_messages(sys.stdin)
    print("{0}".format(num))
