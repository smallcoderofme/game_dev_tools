#!/bin/sh

# Author : Sun Shuai
# Copyright (c) Tutorialsyiibai.com
# Script follows here

$date
pwd
ls

echo "What is your name?"
read PERSON
echo "Hello, $PERSON"

# readyonly NAME
## cancel variables 
# unset NAME 

# $字符表示进程ID号，或PID，在当前shell：
echo $$, $0

read NEXT