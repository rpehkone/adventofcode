#include "io.h"

int	solve(char** file, int dx, int dy)
{
	int x = 0;
	int y = 0;
	int x2 = 0;
	int count = 0;
	int len = wstrlen(file[0]);

	while (file[y])
	{
		if (file[y][x % len] == '#')
			count++;
		x += dx;
		y += dy;
	}
	return (count);
}

void	part1(char** file)
{
	write_int(solve(file, 3, 1));
}

void	part2(char** file)
{
	long res;
	res  = solve(file, 1, 1);
	res *= solve(file, 3, 1);
	res *= solve(file, 5, 1);
	res *= solve(file, 7, 1);
	res *= solve(file, 1, 2);
	write_int(res);
}

int	_start(void)
{
	wmalloc_init();

	char **file = read_textfile_2d("input/in3");

	part1(file);
	part2(file);

	asm("mov rax, 60;"
		"mov rdi, 0;"
		"syscall");
}
