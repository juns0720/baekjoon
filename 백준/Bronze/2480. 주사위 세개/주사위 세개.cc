#include <stdio.h>
int main()
{
	int n, n1, n2, n3, rwd;

	scanf("%d %d %d", &n1, &n2, &n3);



	printf("%d", n1 == n2 && n2 == n3 ? 10000 + n1 * 1000 : n1 == n2 && n2 != n3 ? 1000 + n1 * 100 : n2 == n3 && n2 != n1 ? 1000 + n2 * 100 : n1 == n3 && n1 != n2 ? 1000 + n1 * 100 : n1 >= n2 && n1 >= n3 ? n1 * 100 : n2 >= n3 && n2 >= n1 ? n2 * 100 : n3 * 100);
	return 0;
} 