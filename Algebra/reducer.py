import sys

# przeciecie zbiorow

def main():
    comp_key = -1
    comp_value = -1
    for incoming in sys.stdin:
        line = incoming.strip()
        elements = line.split('\t')

        key = elements[0]
        value = elements[1]

        if key == comp_key and not value == comp_value:
            print str(key) + str(value)

        comp_key = key
        comp_value = value


main()