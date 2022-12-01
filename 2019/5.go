package main

import (
	"io/ioutil"
	"strconv"
	"strings"
	"math"
	"fmt"
)

func pow_int(x int, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func resolve_single_param(ip int, off int, program []int) int {
	div := pow_int(10, off + 1)
	immediate := program[ip] / div % 10;
	var val int
	if immediate == 1 {
		val = program[ip + off]
	} else {
		val = program[program[ip + off]]
	}
	return val
}

func solve(input int, program []int) int{
	var ip int = 0//instruction pointer
	output := 0

	for true {
		opcode := program[ip] % 100
		p1 := resolve_single_param(ip, 1, program)
		p2 := resolve_single_param(ip, 2, program)
		// fmt.Printf("instp = %d\n", ip)
		// fmt.Printf("values at ip = %d %d %d %d\n", program[ip], program[ip + 1], program[ip + 2], program[ip + 3])
		// fmt.Printf("opcode = %d\n", opcode)
		// fmt.Printf("params = %d %d\n\n", p1, p2)
		switch opcode {
		case 1:
			program[program[ip + 3]] = p1 + p2
			ip = ip + 4
		case 2:
			program[program[ip + 3]] = p1 * p2
			ip = ip + 4
		case 3:
			program[program[ip + 1]] = input
			ip = ip + 2
		case 4:
			output = p1
			fmt.Printf("out %d\n", output)
			ip = ip + 2
		case 5:
			if p1 != 0 {
				ip = p2
			} else {
				ip = ip + 3
			}
		case 6:
			if p1 == 0 {
				ip = p2
			} else {
				ip = ip + 3
			}
		case 7:
			if p1 < p2 {
				program[program[ip + 3]] = 1
			} else {
				program[program[ip + 3]] = 0
			}
			ip = ip + 4
		case 8:
			if p1 == p2 {
				program[program[ip + 3]] = 1
			} else {
				program[program[ip + 3]] = 0
			}
			ip = ip + 4
		case 99:
			return (output)
		default:
			fmt.Printf("Unknown opcode\n")
			return -1
		}
	}
	return -1
}

func main(){
	file, err := ioutil.ReadFile("input/5in")
	if err != nil{
		return
	}
	line := string(file)

	opcodes := strings.Split(line, ",")
	var program = make([]int, len(opcodes) + 10000)
	for i := 0; i < len(opcodes) - 1; i++ {
		n, err := strconv.Atoi(opcodes[i])
		if err != nil{
			return
		}
		program[i] = n
	}
	program_copy := make([]int, len(program))
	copy(program_copy, program)
	fmt.Printf("part1 = %d\n", solve(1, program_copy))
	copy(program_copy, program)
	fmt.Printf("part2 = %d\n", solve(5, program_copy))
}
