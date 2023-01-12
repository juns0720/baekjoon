#include <stdio.h>

int main()
{
    int n, x;
    int answer;
    

    while (1)
    {
        scanf("%d %d", &n, &x);
        
        if (n + x == 0)
            break;
        else
            printf("%d\n", n + x);
    }


 

    return 0;
}