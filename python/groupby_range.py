# from here
# https://stackoverflow.com/questions/4628333/converting-a-list-of-integers-into-range-in-python#%20converting-a-list-of-integers-into-range-in-python
# also 
# https://github.com/networktocode/netutils/blob/1c605a0c71869c37539c8e4a001c183e893f63d9/netutils/vlan.py
# also 
# https://github.com/Cray-HPE/canu/blob/0eccd1ec965535d225e8a417da183a3f364bf437/canu/generate/switch/config/config.py#L1047
#
import itertools

def ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield b[0][1], b[-1][1]

print(list(ranges([0, 1, 2, 3, 4, 7, 8, 9, 11])))
