# define _CRT_SECURE_NO_WARNINGS
# include<stdio.h>
int main(void)
{
    char s1[80];
    int i = 0;
    scanf("%s", s1);
    while (1) {
        if (s1[i] != 'X' && s1[i] != 'O')
            break;
        printf("%c\n", s1[i]);
        i++;
    }
    return 0;
}