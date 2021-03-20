#include <stdio.h> 

int main(void)
{
    int N = 0;
    scanf_s("%d", &N);
    for (int i = 1; i <= N; i++)
    {
        for (int ii = 1; ii <= i; ii++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}