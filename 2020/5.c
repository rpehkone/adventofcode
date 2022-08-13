#include "io.h"

int get_seat(char *str)
{
	int change = 128;
	int x = 0;
	int res = 0;
	while (x < 7)
	{
		change /= 2;
		if (str[x] == 'B')
			res += change;
		x++;
	}
	int change2 = 8;
	res *= 8;
	while (x < 10)
	{
		change2 /= 2;
		if (str[x] == 'R')
			res += change2;
		x++;
	}
	return (res);
}


void	part1(char** file)
{
	int i = 0;

	int res = 0;
	while (file[i])
	{
		int seat = get_seat(file[i]);
		if (seat > res)
			res = seat;
		i++;
	}
	write_int(res);
}

void	part2(char** file)
{
	int this = 100;

	int i = 0;
	while (file[i])
	{
		int seat = get_seat(file[i]);
		i++;
		if (seat == this)
		{
			i = 0;
			this++;
		}
	}
	write_int(this);
}

int	_start(void)
{
	wmalloc_init();

	char **file = read_textfile_2d("input/in5");

	part1(file);
	part2(file);

	asm("mov rax, 60;"
		"mov rdi, 0;"
		"syscall");
}
