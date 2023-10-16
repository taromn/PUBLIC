#include <stdio.h>

void compare_two(int sub_array[]);

int main(void)
{
  int nums[10] = {0, 3, 5, 1, 6, 8, 7, 9, 2, 4};
  compare_two(nums);

  printf("the output is:\n");

  for(int m=0;m<=9;m++){
    printf("%d\n",m);
  }
  return 0;
}

void compare_two(int sub_array[])
{
  int tmp; 
  for(int r=1;r<=9;r++){
    for(int j=1;j<=10-r;j++){
      if (sub_array[10-j] < sub_array[10-j-1]){
        tmp = sub_array[10-j-1];
        sub_array[10-j-1] = sub_array[10-j];
        sub_array[10-j] = tmp;
      }
    }
  }
}

/*
  r= 1 (round)
  i= 10 (num of elements)
  j= 1 ~ 9 (cursor)

  r = 2
  i = 10
  j = 1 ~ 8

  r = 3
  i = 10
  j = 1 ~ 7


  r = 9
  i = 10
  j = 1 ~ 1
*/
