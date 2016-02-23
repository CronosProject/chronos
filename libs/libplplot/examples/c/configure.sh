#!/bin/bash
src="src/"

for i in {1..34}
do
	if [ "$i" -le 9 ]
	then
	i='0'$i
	fi

	filename='x'$i'c.c'
	filename_out="$filename"'.out'
	command="gcc $src$filename -o builds/$filename_out `pkg-config --cflags --libs plplotd`"
	$command
done