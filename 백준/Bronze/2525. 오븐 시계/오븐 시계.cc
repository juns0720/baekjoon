#include <stdio.h>
int main()
{

	int hour, min ,time;
	scanf("%d %d", &hour, &min);
	scanf("%d", &time);


			hour = hour+(min + time) / 60;
			min =(min + time) % 60;
			if (hour >= 24)
				hour = hour - 24;

	printf("%d %d\n", hour, min);
	return 0;
}