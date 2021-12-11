#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define SIZE 1000

int part1(char *direction, int *nums)
{
    int horizontal = 0;
    int depth = 0;
    for (int i = 0; i < SIZE; i++)
    {
        char d = direction[i];
        int n = nums[i];
        if (d == 'd')
            depth += n;
        else if (d == 'u')
            depth -= n;
        else if (d == 'f')
            horizontal += n;
    }
    return depth * horizontal;
}

int part2(char *direction, int *nums)
{
    int aim = 0;
    int horizontal = 0;
    int depth = 0;

    for (int i = 0; i < SIZE; i++)
    {
        char d = direction[i];
        int n = nums[i];
        if (d == 'd')
            aim += n;
        else if (d == 'u')
            aim -= n;
        else if (d == 'f')
        {
            horizontal += n;
            depth += aim * n;
        }
    }
    return horizontal * depth;
}

int main()
{

    // Read input from file
    FILE *fp = fopen("input.txt", "r");
    char buffer[16];
    char direction[SIZE];
    int nums[SIZE];
    int index = 0;
    while (fgets(buffer, 16, fp))
    {
        direction[index] = buffer[0];
        for (int i = 1; i < 16; i++)
        {
            if (isspace(buffer[i]))
            {
                nums[index] = buffer[i + 1] - '0';
                break;
            }
        }
        index++;
    }
    fclose(fp);

    printf("Part 1: %i\n", part1(direction, nums));
    printf("Part 2: %i\n", part2(direction, nums));

    return 0;
}
