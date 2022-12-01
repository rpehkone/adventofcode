package main

import (
	"strconv"
	"fmt"
)

func part1(i int) bool {
	str := strconv.Itoa(i)
	prev := int(str[0])
	pair_found := false
	for k := 1; k < len(str); k++{
		this := int(str[k])
		if prev == this {
			pair_found = true
		}
		if this < prev {
			return false
		}
		prev = this
	}
	return pair_found
}

func part2(i int) bool {
	str := strconv.Itoa(i)
	prev := int(str[0])
	run_len := 0
	pair_found := false
	for k := 1; k < len(str); k++{
		this := int(str[k])
		if prev == this {
			run_len++
		} else {
			if run_len == 1 {
				pair_found = true
			}
			run_len = 0;
		}
		if this < prev {
			return false
		}
		prev = this
	}
	if run_len == 1 {
		pair_found = true
	}
	return pair_found
}

func main(){
	part1_res := 0
	part2_res := 0
	for i := 183564; i < 657474; i++{
		if (part1(i)) {
			part1_res++
		}
		if (part2(i)) {
			part2_res++
		}
	}
	fmt.Printf("part1: %d\n", part1_res)
	fmt.Printf("part2: %d\n", part2_res)
}
