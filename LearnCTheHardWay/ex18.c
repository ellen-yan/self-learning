#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

/** Our old friend die from ex17. */
void die(const char *message)
{
  if(errno) {
    perror(message);
  } else {
    printf("ERROR: %s\n", message);
  }
  exit(1);
}

// a typedef creates a fake type, in this case for a function pointer
// (whatever we use as compare_cb must match this signature)
typedef int (*compare_cb)(int a, int b);
// compare_cb used later as a type in the bubble_sort and test_sorting functions

typedef int *(*sort_funct)(int *numbers, int count, compare_cb cmp);
/**
 * A classic bubble sort function that uses the
 * compare_cb to do the sorting.
 */
int *bubble_sort(int *numbers, int count, compare_cb cmp)
{
  int temp = 0;
  int i = 0;
  int j = 0;
  int *target = malloc(count * sizeof(int));

  if(!target) die("Memory error.");

  memcpy(target, numbers, count * sizeof(int));

  for(i = 0; i < count; i++) {
    for(j = 0; j < count - 1; j++) {
      if(cmp(target[j], target[j+1]) > 0) {
        temp = target[j+1];
        target[j+1] = target[j];
        target[j] = temp;
      }
    }
  }
  return target;
}

// Extra credit: coded alternative sorting method and changed testing function
// to accept a sorting function as an argument
int *merge_sort(int *numbers, int count, compare_cb cmp)
{
  int *target = malloc(count * sizeof(int));

  if(count <= 1) {
    memcpy(target, numbers, count * sizeof(int));
    if(!target) die("Memory error.");
    return target;
  }

  int count1 = count / 2;
  int count2 = count - count1;
  int *first_half;
  int *second_half;
  first_half = numbers;
  second_half = numbers + count1; // points to the same thing as numbers

  if(!first_half) die("Memory error.");
  if(!second_half) die("Memory error.");

  // Recursive call
  int *sorted_first = merge_sort(first_half, count1, cmp);
  int *sorted_second = merge_sort(second_half, count2, cmp);

  // Merge procedure
  int i = 0; // current position in first_half
  int j = 0; // current position in second_half
  int k = 0; // current position in new array
  while(i < count1 || j < count2) {
    if(i >= count1) {
      // add all the elements left in the second half
      int c = j;
      for(j = c; j < count2; j++) {
        target[k] = sorted_second[j];
        k += 1;
      }
      j = count2;
      break;
    } else if(j >= count2) {
      // second_half is empty, add all elements left in the first half
      int c = i;
      for(i = c; i < count1; i++) {
        target[k] = sorted_first[i];
        k += 1;
      }
      i = count1;
      break;
    } else {
      // neither list is empty, add one element from the two halves
      if(cmp(sorted_first[i], sorted_second[j]) < 0) {
        *(target + k) = *(sorted_first + i);
        k += 1;
        i += 1;
      } else {
        *(target + k) = *(sorted_second + j);
        k += 1;
        j += 1;
      }
    }
  }
  return target;
}

int sorted_order(int a, int b)
{
  return a - b; // < 0 if a a < b i.e. sorted
}

int reverse_order(int a, int b)
{
  return b - a;
}

int strange_order(int a, int b)
{
  if(a == 0 || b == 0) {
    return 0;
  } else {
    return a % b;
  }
}

/**
 * Used to test that we are sorting things correctly
 * by doing the sort and printing it out.
 */
void test_sorting(int *numbers, int count, compare_cb cmp, sort_funct sf)
{
  int i = 0;
  int *sorted = sf(numbers, count, cmp);

  if(!sorted) die("Failed to sort as requested.");

  printf("Sort result:\n");
  for(i = 0; i < count; i++) {
    printf("%d ", sorted[i]);
  }
  printf("\n");

  free(sorted);

  // Prints out raw assembler byte code of the function
  /*unsigned char *data = (unsigned char *)cmp;

  for(i = 0; i < 25; i++) {
    printf("%02x:", data[i]);
  }
  printf("\n");*/
}

int main(int argc, char *argv[])
{
  if(argc < 2) die("USAGE: ex18 4 3 1 5 6");

  int count = argc - 1; // number of elements to be sorted
  int i = 0;
  char **inputs = argv + 1;

  int *numbers = malloc(count * sizeof(int));
  if(!numbers) die("Memory error.");

  for(i = 0; i < count; i++) {
    numbers[i] = atoi(inputs[i]); // convert to integers
  }

  test_sorting(numbers, count, sorted_order, bubble_sort);
  test_sorting(numbers, count, reverse_order, bubble_sort);
  test_sorting(numbers, count, strange_order, bubble_sort);

  test_sorting(numbers, count, sorted_order, merge_sort);
  test_sorting(numbers, count, reverse_order, merge_sort);
  test_sorting(numbers, count, strange_order, merge_sort);

  free(numbers);

  return 0;
}
