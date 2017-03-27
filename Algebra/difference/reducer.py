import sys

# roznica zbiorow


def main():

    MAIN_SET = "A"
    current_key = None
    current_value = None

    for i, incoming in enumerate(sys.stdin):

        line = incoming.strip()
        elements = line.split('\t')

        key = elements[0]
        relation = elements[1]

        if key != current_key and MAIN_SET == current_value:
            print current_key

        current_key = elements[0]
        current_value = elements[1]


main()
