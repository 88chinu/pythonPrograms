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
   // for calculation of minimum number of guesses depends
    // upon range
    while (count < total_chances) {
        count++;

        // Taking guessing number as input
        printf("Guess a number: ");
        scanf("%d", &guess);

        // Condition testing
        if (x == guess) {
            printf(
                "Congratulations you did it in %d try!\n",
                count);
            // Once guessed, loop will break
            flag = 1;
            break;
        }
        else if (x > guess) {
            printf("You guessed too small!\n");
        }
        else if (x < guess) {
            printf("You guessed too high!\n");
        }
    }
}