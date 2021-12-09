#include <stdio.h>
#include <stdlib.h>
#define SIZE 2000
int main(){
  // Read input from file
  FILE *fp = fopen("input.txt","r");
  char buffer[8];
  int nums[SIZE];
  int index = 0;
  while (fgets(buffer, 8, fp)){
    nums[index] = atoi(buffer);
    index++;
  }
  fclose(fp);
  
  // Part 1
  int counter = 0;
  for (int i = 1; i < SIZE; i++){
    if (nums[i-1] < nums[i])
      counter ++;
  }
  printf("Part 1: %i\n", counter);

  // Part 2
  counter = 0;
  for (int i = 3; i < SIZE; i++){
    int a = nums[i-3],b= nums[i-2],c = nums[i-1],d=  nums[i];
    if (a+b+c < b+c+d){
      counter ++;
    }
  }
  printf("Part 2: %i\n", counter);
  return 0;
}
