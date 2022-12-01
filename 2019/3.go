package main

import (
	"io/ioutil"
	"strconv"
	"strings"
	"fmt"
)

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func trim_left_char(s string) string {
	for i := range s {
		if i > 0 {
			return s[i:]
		}
	}
	return s[:0]
}

func move_coords(x *int, y *int, str string) {
	dir := str[0]
	var amount_str string = trim_left_char(str)
	n, err := strconv.Atoi(amount_str);
	if err != nil{
		return
	}
	if dir == 'R' {
		*x += n
	} else if dir == 'L' {
		*x -= n
	} else if dir == 'U' {
		*y -= n
	} else {
		*y += n
	}
}

func swap_min(a *int, b *int) {
    if *a > *b {
		tmp := *a
		*a = *b
		*b = tmp
    }
}

func line_len(px int, py int, x int, y int) int {
	if px == x {
		return (abs(py - y) - 1)
	}
	return (abs(px - x) - 1)
}

func do_lines_cross(l1px int, l1py int, l1x int, l1y int, l2px int, l2py int, l2x int, l2y int) (bool, int, int){
	//parallel test
	if l1px == l1x && l2px == l2x {
		return false, 0, 0
	}
	if l1py == l1y && l2py == l2y {
		return false, 0, 0
	}
	swap_min(&l1px, &l1x)
	swap_min(&l1py, &l1y)
	swap_min(&l2px, &l2x)
	swap_min(&l2py, &l2y)
	if (l1x != l1px) {
		if l2x > l1px && l2x < l1x {
			if l1y > l2py && l1y < l2y {
				return true, l1x, l2y
			}
		}
	} else {
		if l1x > l2px && l1x < l2x {
			if l2y > l1py && l2y < l1y {
				return true, l2x, l1y
			}
		}
	}
	return false, 0, 0
}

func main(){
	file, err := ioutil.ReadFile("input/3in")
	if err != nil{
		return
	}
	line := string(file)

	wires := strings.Split(line, "\n")
	wire1 := strings.Split(wires[0], ",")
	wire2 := strings.Split(wires[1], ",")

	part1 := 999999999999
	part2 := 999999999999
	thisx := 0
	thisy := 0
	prevx := 0
	prevy := 0
	w1steps := 0
	for i := 0; i < len(wire1) - 1; i++ {
		move_coords(&thisx, &thisy, wire1[i])
		w2thisx := 0
		w2thisy := 0
		w2prevx := 0
		w2prevy := 0
		w2steps := 0
		for k := 0; k < len(wire2) - 1; k++ {
			move_coords(&w2thisx, &w2thisy, wire2[k])
			crossed, cx, cy := do_lines_cross(prevx, prevy, thisx, thisy, w2prevx, w2prevy, w2thisx, w2thisy)
			if crossed {
				// fmt.Printf("%d\n", abs(cx) + abs(cy))
				fmt.Printf("%d\n", w1steps + w2steps)
				fmt.Printf("l1 %d\n", line_len(prevx, prevy, cx, cy))
				fmt.Printf("l2 %d\n", line_len(w2prevx, w2prevy, cx, cy))
				part1 = min(part1, abs(cx) + abs(cy))
				part2 = min(part2, w1steps + w2steps +
						line_len(prevx, prevy, cx, cy) +
						line_len(w2prevx, w2prevy, cx, cy))
			}
			w2steps += line_len(w2prevx, w2prevy, w2thisx, w2thisy)
			// fmt.Printf("w2step\n");
			w2prevx = w2thisx
			w2prevy = w2thisy
		}
		w1steps += line_len(prevx, prevy, thisx, thisy)
		// fmt.Printf("w1\n");
		prevx = thisx
		prevy = thisy
	}
	fmt.Printf("part1: %d\n", part1)
	fmt.Printf("part2: %d\n", part2)
}
