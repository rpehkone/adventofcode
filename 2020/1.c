#include "io.h"

void	part1(char** file)
{
	int	x;
	int	y;
	int	intx;
	int	inty;

	x = 0;
	while (file[x])
	{
		y = 0;
		intx = watoi(file[x]);
		while (file[y])
		{
			inty = watoi(file[y]);
			if (intx + inty == 2020)
			{
				write_int(intx * inty);
				return;
			}
			y++;
		}
		x++;
	}
}

void	part2(char** file)
{
	int	x;
	int	y;
	int	z;
	int	intx;
	int	inty;
	int	intz;

	x = 0;
	while (file[x])
	{
		y = 0;
		intx = watoi(file[x]);
		while (file[y])
		{
			z = 0;
			inty = watoi(file[y]);
			while (file[z])
			{
				intz = watoi(file[z]);
				if (intx + inty + intz == 2020)
				{
					write_int(intx * inty * intz);
					return;
				}
				z++;
			}
			y++;
		}
		x++;
	}
}

int	_start(void)
{
	wmalloc_init();

	char **file = read_textfile_2d("input/in1");

	part1(file);
	part2(file);

	asm("mov rax, 60;"
		"mov rdi, 0;"
		"syscall");
}
