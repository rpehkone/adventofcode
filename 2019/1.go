package main

import (
	"strconv"
	"bufio"
	"fmt"
	"os"
)

func main(){
	file, err := os.Open("input/1in")
	if err != nil{
		return
	}

	scanner := bufio.NewScanner(file)
	var part1 int = 0
	var part2 int = 0
    for scanner.Scan(){
		n, err := strconv.Atoi(scanner.Text());
		if err != nil{
			return
		}
		var this int = 0
		this = (n / 3) - 2
		part1 = part1 + this
		for this > 0 {
			part2 = part2 + this
			this = (this / 3) - 2
		}
    }
	fmt.Printf("part1 = %d\n", part1)
	fmt.Printf("part2 = %d\n", part2)
}
