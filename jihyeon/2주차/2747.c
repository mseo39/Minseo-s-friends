#include <stdio.h> 

int main(void)
{
    int a= 0, b = 1, c = 0, n = 0;
    scanf_s("%d", &n);
    if (n == 0) printf("0");
    else if (n == 1) printf("1");
    else
    {
        for (int i = 1; i < n; i++)
        {
            c = a + b;
            a = b;
            b = c;
        }
        printf("%d", c);
    }
    return 0;
}