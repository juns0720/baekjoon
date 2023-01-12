#include <stdio.h>
int main()
{
	int prc1, prc2, n;
	int a, b;
	prc2 = 0;
	scanf("%d", &prc1);//전체금액 
	scanf("%d", &n); // 종류
	for (int i = 0; i < n; i++)
	{
		scanf("%d %d", &a, &b);
		prc2 += a * b;
	}
	if (prc1 == prc2)
		printf("Yes");
	else
		printf("No");





	return 0;
} 