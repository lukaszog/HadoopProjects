import sys


def main():

    order_id, user_id, date, customer_id, customer_name, customer_lastname, customer_city\
        = "", "", "", "", "", "", ""

    for incoming in sys.stdin:
        line = incoming.strip()

        if len(line) == 0:
            continue

        elements = line.split('\t')

        # only orders
        if len(elements) == 4:
            order_id = elements[1]
            user_id = elements[2]
            date = elements[3]
        else:
            # now user data
            customer_id = elements[1]
            customer_name = elements[2]
            customer_lastname = elements[3]
            customer_city = elements[4]

        print customer_city


main()
