#!/usr/bin/env python

import sys

def solve_problem():
    pass

    return 1

def add_to_hash(hash, val):
    if val not in hash:
        hash[val] = 1
    else:
        hash[val] += 1

def debug(s):
    if False:
        print(s)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def process_cases():
    num_cases = int(next(sys.stdin))

    for case_number in range(1, num_cases + 1):
        debug("-----------")
    	debug("Case #{0}".format(case_number))
        debug("-----------")
        nums_in_case = int(next(sys.stdin))
        #print(nums_in_case)

    	line = next(sys.stdin)
    	numbers = map(int, line.split(' '))

        debug(numbers)
        num_hash = {}

        for n in numbers:
            if n in num_hash:
                num_hash[n] += 1
            else:
                num_hash[n] = 1

        total_triplets = 0

        nums = num_hash.keys()

        last = nums[-1]

        #print("last: {}".format(last))
        for i_a_x in range(0, len(nums)):
            for i_a_y in range(i_a_x, len(nums)):
                debug("----")

                a_x = nums[i_a_x]
                a_y = nums[i_a_y]
                a_z = a_x * a_y

                if a_z not in num_hash:
                    continue

                debug("{0} * {1} = {2}".format(a_x, a_y, a_z))
                debug("Match!")

                res_hash = {}
                add_to_hash(res_hash, a_x)
                add_to_hash(res_hash, a_y)
                add_to_hash(res_hash, a_z)

                break_it = False

                possible_results = 1

                debug("res_hash: {}".format(res_hash))
                for k,v in res_hash.items():
                    curr = num_hash[k] - res_hash[k]

                    debug("curr={} k={} v={} num_hash[k]={}".format(curr, k, v, num_hash[k]))
                    if curr < 0:
                        break_it = True
                        break
                    elif curr == 0:
                        pass
                    else:
                        #selections = factorial(num_hash[k])/factorial(res_hash[k])
                        # OR ==
                        selections = 1
                        for i in range(res_hash[k], num_hash[k]):
                            selections *= (i + 1)

                        debug("selection: num={} times = {}".format(k, selections))
                        possible_results = possible_results * selections

                if break_it:
                    #print("Break!")
                    continue

                total_triplets += possible_results

        #print(num_hash)
    	print("Case #{0}: {1}".format(case_number, total_triplets))

def test_problem():
    assert solve_problem() == 1

if __name__ == '__main__':
    process_cases()
