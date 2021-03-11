#include <stdio.h>

int main(void)
{
    int a = 0;
    int count = 1;
    int ans = 0;
    int b = 0;
    scanf_s("%d", &a);
    b = a;
    for (int i = 1; i <= 100; i++)
    {
        if (a / 10 == 0)
        {
            break;
        }
        else
        {
            a = a / 10;
            count++;
        }
    }
    for (int ii = 1; ii <= count; ii++)
    {
        ans = ans + b % 10;
        b = b / 10;
    }
    printf("%d", ans);

    return 0;
}