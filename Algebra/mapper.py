import sys


def main():
    for incoming in sys.stdin:
        line = incoming.strip()
        elements = line.split('\t')

        if len(elements) > 1:
            key = elements[1]
            value = elements[0]

        print str(key) + '\t' + str(value)

main()
