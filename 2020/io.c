#include <asm/unistd.h>
#include <unistd.h>
#include <fcntl.h>

int	watoi(const char *str)
{
	int		nbr;
	char	neg;

	// while (*str == ' ')
	// 	str++;
	neg = (*str == '-');
	if (*str == '-' || *str == '+')
		str++;
	nbr = 0;
	while (*str >= '0' && *str <= '9')
	{
		nbr = nbr * 10 + (*str - '0');
		str++;
	}
	return (neg ? -nbr : nbr);
}

int wstrlen(char *str)
{
	int i = 0;
	while (str[i])
		i++;
	return (i);
}

//write integer to console, maybe fastest possible implementation
void	write_int(long n)
{
	char neg = 0;
	if (n < 0)
	{
		neg = 1;
		n *= -1;
	}

	char out[32];

	char i = 15;
	out[i--] = '\n';
	while (n > 9)
	{
		out[i--] = n % 10 + '0';
		n /= 10;
	}
	out[i--] = n + '0';
	if (neg)
		out[i--] = '-';

	register char*	arg2 asm("rsi") = &out[i + 1];
	register int	arg3 asm("rdx") = 15 - i;
	asm("mov rax, 1;"
		"mov rdi, 1;"
		"syscall");
}

static void *heap;

void	wmalloc_init(void)
{
	heap = sbrk(0);
	// page size = 2mb = 2 ^ 21 = 2097152
	sbrk(2097152 * 4);
}

void	*wmalloc(int bytes)
{
	void *res = heap;
	heap += bytes;
	return (res);
}

static char*
read_file_to_buffer(char* filename, long *len)
{
	int fd = open(filename, O_RDONLY);
	char *res = heap;
	int ret = read(fd, res, 2097152);
	res[ret] = '\0';
	heap += ret + 1;
	*len = (long)ret;
	return (res);
}

static char **
file2d(char *file, long size)
{
	int		i;
	int		line_count;
	char	**res;

	line_count = 0;
	i = -1;
	while (++i < size)
		if (file[i] == '\n')
			line_count++;
	res = (char **)wmalloc(sizeof(char *) * (line_count + 1));
	line_count = 0;
	res[line_count] = &file[0];
	i = -1;
	while (++i < size)
	{
		if (file[i] == '\n')
		{
			file[i] = '\0';
			res[++line_count] = &file[i + 1];
		}
	}
	res[line_count] = NULL;
	return (res);
}

char **
read_textfile_2d(char *filename)
{
	long size;
	char *file = read_file_to_buffer(filename, &size);
	return file2d(file, size);
}
