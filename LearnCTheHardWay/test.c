#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
  int count = 5 / 2;
  printf("%d\n", count);
  int arr[5] = {1, 2, 3, 4, 5};
  int *array1 = malloc(5 * sizeof(int));

  array1 = arr;

  int *array2 = malloc(count * sizeof(int));
  memcpy(array2, (array1 + count), 3);
  printf("First element of array2: %d\n", array2[0]);

  return 0;
}
