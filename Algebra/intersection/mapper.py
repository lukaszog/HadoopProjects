import sys


def main():
    for incoming in sys.stdin:
        line = incoming.strip()

        if len(line) == 0:
            continue

        elements = line.split('\t')

        if len(elements) > 1:
            key = elements[0]
            value = elements[1]

        print str(value) + '\t' + str(value)

main()
