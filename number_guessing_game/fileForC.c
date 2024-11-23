#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main
{
    int lower, upper, x, guess, count = 0, flage = 0;
    int total_changes;

    printf("Enter Lower bound");
    scanf("%d",&lower);

    printf("Enter Upper bound");
    scanf("%d",&upper);

    srand(time(0));

    x = (rand() % (upper - lower + 1)) + lower;
    total_chances
        = (int)ceil(log(upper - lower + 1) / log(2));

    printf("\n\tYou've only %d chances to guess the "
           "integer!\n\n",
           total_chances);
}