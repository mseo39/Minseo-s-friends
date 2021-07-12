# include<stdio.h>
int main(void)
{
    int a = 0;
    scanf_s("%d", &a);
    int aa[100] = { 0 };
    int sit = 0;
    int count = 0;
    for (int i = 0; i < a; i++)
    {
        scanf_s("%d", &sit);
        if (aa[sit] == 0) 
        {
            aa[sit] = 1;
        }
        else count++;
    }
    printf("%d", count);
    return 0;
}