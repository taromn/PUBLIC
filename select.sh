#!/bin/bash

function advancedMenu() {

    ADVSEL=$(whiptail --title "Menu" --fb --menu "Select options" 15 60 4 \
    "1" "Option 1st" \
    "2" "Option 2nd" \
    "3" "Option 3rd" 3>&1 1>&2 2>&3)

    case $ADVSEL in

    1)
      echo "Options 1"
      whiptail --title "Options 1" --msgbox "you choose options 1" 8 45
      ;;

    esac

}

advancedMenu

# one line
# whiptail --title "Menu" --fb --menu "Select options" 15 60 4 "1" "Options" "2" "Options" "3" "Options" 3>&1 1>&2 2>&3

# https://manpages.debian.org/testing/whiptail/whiptail.1.en.html
