#!/bin/bash

status=$(nmcli con show --active | grep -i CNET)

if [[ -z "$status" ]]; then
    nmcli c up CNET
else
    nmcli c down CNET
fi
