#include <stdio.h>

int main()
{
    int a, b, c, d, e;
    scanf("%d %d", &a, &b);
    c = a * (b%10);
    d = a * (((b % 100)-(b%10))/10);
    e = a * ((b - (((b % 100) - (b % 10))+b%10))/100);
    printf("%d\n", c);
    printf("%d\n", d);
    printf("%d\n", e);
    printf("%d\n", c + 10 * d + 100 * e);
   

    

    return 0;
}