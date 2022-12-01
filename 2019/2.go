package main

import (
	"io/ioutil"
	"strconv"
	"strings"
	"fmt"
)

func solve(a int, b int, program []int) int{
	program[1] = a
	program[2] = b

	var ip int = 0//instruction pointer
	for program[ip] != 99 {
		if program[ip] == 1{
			program[program[ip + 3]] = program[program[ip + 1]] + program[program[ip + 2]]
		} else if program[ip] == 2{
			program[program[ip + 3]] = program[program[ip + 1]] * program[program[ip + 2]]
		} else{
			fmt.Printf("Unknown opcode\n")
			return -1
		}
		ip = ip + 4
	}
	return (program[0])
}

func main(){
	file, err := ioutil.ReadFile("input/2in")
	if err != nil{
		return
	}
	line := string(file)

	opcodes := strings.Split(line, ",")
	var program = make([]int, len(opcodes))
	for i := 0; i < len(opcodes) - 1; i++ {
		n, err := strconv.Atoi(opcodes[i])
		if err != nil{
			return
		}
		program[i] = n
	}
	program_copy := make([]int, len(program))
	copy(program_copy, program)
	fmt.Printf("part1 = %d\n", solve(12, 2, program_copy))
	for x := 1; x < 100; x++{
		for y := 1; y < 100; y++{
			copy(program_copy, program)
			if 19690720 == solve(x, y, program_copy){
				fmt.Printf("part2 = %d\n", 100 * x + y)
				return
			}
		}
	}
}
