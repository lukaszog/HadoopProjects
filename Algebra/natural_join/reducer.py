import sys

# przeciecie zbiorow

def main():
    comp_key = -1
    for incoming in sys.stdin:
        line = incoming.strip()
        elements = line.split('\t')

        key = elements[0]

        if key == comp_key:
            print str(key)

        comp_key = key
main()
