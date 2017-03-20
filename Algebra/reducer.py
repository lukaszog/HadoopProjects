import sys


def main():
    for incoming in sys.stdin:
        line = incoming.strip()
        elements = line.split('\t')

        key = elements[1]
        value = elements[0]

        print str(key) + str(value)

main()