import sys


def main():
    for incoming in sys.stdin:
        line = incoming.strip()
        elements = line.split('\t')

        if len(elements) > 1:
            key = elements[0]
            value = elements[1]

        print str(key) + '\t' + str(value)

main()
