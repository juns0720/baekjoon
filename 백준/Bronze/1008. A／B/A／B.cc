#define _CRT_SECURE_WARNING
#include <stdio.h>

int main()
{
    double a, b;
    scanf("%lf %lf", &a, &b);
    printf("%.10lf",a / b);


    return 0;
}