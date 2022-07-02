#!/usr/bin/python3
if __name__ == "__main__"
    import calculator_1 as calculate
    import sys

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: >/100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        c = calculate.add(a, b)
    elif sys.argv[2] == '-':
        c = calculate.sub(a, b)
    elif sys.argv[2] == '*':
        c = calculate.mul(a, b)
    elif sys.argv[2] == '/':
        c = calculate.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, c))
    sys.exit(0)
