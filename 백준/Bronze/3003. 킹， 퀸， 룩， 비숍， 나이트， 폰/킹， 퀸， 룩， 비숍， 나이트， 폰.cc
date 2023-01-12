#include <stdio.h>
int main()
{
	int c[6] = { 1,1,2,2,2,8 };
	int a[6];
	int b[6];

		for (int i = 0; i < 6; i++)
			scanf("%d",&a[i]); 

		for (int i = 0; i < 6; i++)
			if (a[i] >= 0 && a[i] <= 10)
				b[i] = c[i] - a[i];
			else return 0;
		for (int i = 0; i < 6; i++)
			printf("%d ", b[i]);

	return 0;
}
