#include <stdio.h>
int main()
 {
	int n,a, b, t,count;
	count = 0;
	scanf("%d", &n);
	t = n;
	while (1)
	{
		a = t / 10;
		b = t % 10;
			t = b*10+(a + b)%10;
			count++;
		if (n == t)
			break;
	}
	printf("%d", count);
	return 0;
} 