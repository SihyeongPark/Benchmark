#!/bin/sh

DATE=`date +%Y%m%d-%H%M%S`

PYTHON=`ps -ef|grep python3|grep -v grep | wc -l`
BASH=`ps -ef|grep bash|grep -v grep | wc -l`

if [ $BASH -gt 0 ]
then
	echo "$DATE: YES"
else
	echo "$DATE: NO"
fi
