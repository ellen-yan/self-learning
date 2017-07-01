// "header file", tells compiler we're using standard input/output functions
#include <stdio.h>

int main()
{
  int age = 10;
  int height = 72;

  printf("I am %d years old.\n", age); // variables to be replaced by format string
  printf("I am %d inches tall.\n", height);

  return 0;
}
