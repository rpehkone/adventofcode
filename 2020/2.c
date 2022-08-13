#include "io.h"

void	part2(char** file)
{
	int x;
	int y;
	int i = 0;
	int j = 0;
	char c;
	int count = 0;

	while (file[i])
	{
		j = 0;
		x = watoi(&file[i][0]);
		while (file[i][j] != '-')
			j++;
		j++;
		y = watoi(&file[i][j]);
		while (file[i][j] != ':')
			j++;
		c = file[i][j - 1];
		j++;
		if ((file[i][j + x] == c) ^ (file[i][j + y]) == c)
			count++;
		i++;
	}
	write_int(count);
}

void	part1(char** file)
{
	int x;
	int y;
	int i = 0;
	int j = 0;
	char c;
	int count = 0;
	int zz;

	while (file[i])
	{
		j = 0;
		x = watoi(&file[i][0]);
		while (file[i][j] != '-')
			j++;
		j++;
		y = watoi(&file[i][j]);
		while (file[i][j] != ':')
			j++;
		c = file[i][j - 1];
		zz = 0;
		while (file[i][j])
		{
			if (file[i][j] == c)
				zz++;
			j++;
		}
		if (zz >= x && zz <= y)
			count++;
		i++;
	}
	write_int(count);
}

int	_start(void)
{
	wmalloc_init();

	char **file = read_textfile_2d("input/in2");

	part1(file);
	part2(file);

	asm("mov rax, 60;"
		"mov rdi, 0;"
		"syscall");
}
