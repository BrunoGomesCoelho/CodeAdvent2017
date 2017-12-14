#!/bin/bash
# Basic script for creating the directories I need
# since I already have 1-5 created, we will star at 6

counter=6
while [ $counter -le 25 ]
do
	mkdir day$counter
	((counter++))
done
echo "All done"
