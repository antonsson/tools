#!/bin/sh

norm="$(printf '\033[0m')"
red="$(printf '\033[31m')"
yellow="$(printf '\033[33m')"

sed -e "s/^.* E .*$/${red}&${norm}/g" -e "s/^.* W .*$/${yellow}&${norm}/g"

