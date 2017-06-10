#!/bin/bash

        echo "(1, 2, 3, 4): "
        read KATALOG
        case $KATALOG in
                "1") /bin/bash zadanie1.sh ;;
                "2") /bin/bash zadanie2.sh ;;
                "3") /bin/bash zadanie3.sh ;;
                "4") /bin/bash zadanie4.sh ;;
                *) find . -type f -name "part*" -exec echo {} \; -exec cat {} \; #cat macierze/output/mm/* ;;
        esac
