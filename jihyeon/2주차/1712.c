#include <stdio.h> 

int main(void)
{
    int A = 0, B = 0, C = 0, D = 0, E =0;
    scanf_s("%d %d %d", &A, &B, &C);
    D = C - B;
    E = A / D + 1;
    if (E <= 1) E = -1; 
    printf("%d", E);
    return 0;
}