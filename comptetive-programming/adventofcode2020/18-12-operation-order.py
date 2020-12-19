
import sys
import pytest


def simple_op(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b

    raise ValueError("nope {}".format(op))


def operation_order(line):
    line = line.replace(" ", "")

    mystack = []

    val = None
    op = None

    for t in line:
        print("t={} val={} op={} mystack={}".format(t, val, op, mystack))

        if t == "(":
            mystack.append([val, op])
            val = None
            op = None
        elif t == ")":
            assert op == None
            prev_val, prev_op = mystack.pop()
            print("{} {}".format(prev_val, prev_op))

            if prev_op is None:
                val = val
            else:
                val = simple_op(prev_val, val, prev_op)
        elif t in ("+", "-", "*"):
            op = t
        else:
            new_val = int(t)
            if val is None:
                val = new_val
            else:
                val = simple_op(val, new_val, op)
                op = None

    return val


def operation_order_part2(line2):
    line = line2.replace(" ", "")
    # print(line)
    # print("------------------")

    mystack = []

    val = None
    op = None

    for t in line:
        # print("t={} val={} op={} mystack={}".format(t, val, op, mystack))

        if t == "(":
            if val is not None and op is not None:
                mystack.append([val, op])

            mystack.append([None, "("])
            val = None
            op = None
        elif t == ")":
            assert op == None

            # Unwinding up to ( -- brace is closed!
            while len(mystack) > 0:
                lhs, prev_op = mystack.pop()

                if prev_op == "(":
                    break

                if prev_op == None:
                    break

                val = simple_op(lhs, val, prev_op)

            # Unwinding all + in stack (actually at most 1 if present)
            while len(mystack) > 0:
                lhs, prev_op = mystack.pop()

                if prev_op != "+":
                    mystack.append([lhs, prev_op])
                    break

                val = simple_op(lhs, val, prev_op)
        elif t in ("*", "+"):
            op = t
        else:
            new_val = int(t)
            if val is None:
                val = new_val
            elif op == "*":

                # Unwinding all + in stack (actually at most 1 )
                while len(mystack) > 0:
                    lhs, prev_op = mystack.pop()

                    if prev_op != "+":
                        mystack.append([lhs, prev_op])
                        break

                    val = simple_op(lhs, val, prev_op)

                mystack.append([val, op])
                val = new_val
                op = None
            else:
                val = simple_op(val, new_val, op)
                op = None

    while len(mystack) > 0:
        lhs, op = mystack.pop()

        if op is None and lhs is None:
            continue

        if op == "(":
            break

        val = simple_op(lhs, val, op)

    print("{} {}".format(line2.strip(), val))

    return val


def expressions_calculator(lines):
    return sum(operation_order(line.strip()) for line in lines)


def expressions_calculator_2(lines):
    return sum(operation_order_part2(line.strip()) for line in lines)


@pytest.mark.parametrize("formula,expected", [
    ("2 * 3 + (4 * 5)", 26),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632)
]
)
def test_operation_order(formula, expected):
    assert operation_order(formula) == expected


@pytest.mark.parametrize("formula,expected", [
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("2 * 3 + (4 * 5)", 46),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
    ("(3 * (4 * 8) * 5 * 7 * 3) + 8", 10088),
    ("5 + (4 + 1) * 7 + 6", 130),
    ("(4 + 3) * 7 + 2", 63),
    ("3 + (5 + 5) + 8 * (8 * 4)", 672)
]
)
def test_operation_order_part2(formula, expected):
    assert operation_order_part2(formula) == expected


if __name__ == "__main__":
    # That's the right answer! You are one gold star closer to saving your vacation.
    # You have completed Day 18! You can [Share] this victory or [Return to Your Advent Calendar].
    # cat 18-12.txt | python 18-12-operation-order.py
    # 119224703255966
    num = expressions_calculator_2(sys.stdin)
    print("{0}".format(num))
