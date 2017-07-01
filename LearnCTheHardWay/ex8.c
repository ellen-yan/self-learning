#include <stdio.h>

int main(int argc, char *argv[])
{
  int areas[] = {10, 12, 13, 14, 20};
  char name[] = "Ellen";
  char full_name[] = {
    'E', 'l', 'l', 'e', 'n',
    ' ', 'X', '.', ' ',
    'Y', 'a', 'n', '\0'
  };

  // WARNING: On some systems you may have to change the
  // %ld in this code to a %u since it will use unsigned ints
  printf("The size of an int: %ld\n", sizeof(int));
  printf("The size of areas (int[]): %ld\n",
          sizeof(areas));
  printf("The number of ints in areas: %ld\n",
          sizeof(areas) / sizeof(int));
  printf("The first area is %d, the 2nd %d.\n",
          areas[0], areas[1]);

  printf("The size of a char: %ld\n", sizeof(char));
  printf("The size of name (char[]): %ld\n",
          sizeof(name));
  printf("The number of chars: %ld\n",
          sizeof(name) / sizeof(char));

  printf("The size of full_name (char[]): %ld\n",
          sizeof(full_name));
  printf("The number of chars: %ld\n",
          sizeof(full_name) / sizeof(char));

  printf("name=\"%s\" and full_name=\"%s\"\n",
          name, full_name);

  areas[0] = 100;
  printf("%d\n", areas[0]);
  areas[1] = full_name[11]; // converts char to ASCII
  printf("%d\n", areas[1]);

  return 0;
}

/* Notes:
- during array creation: compiler looks at [] and see there's no length given,
then looks at initializer {...} and figure out what to put in the array,
create a piece of memory that can hold that many items, takes the name
given and assigns it to that location
- using the syntax of assigning one character at a time in the char array is
just a more annoying way of saying the same thing
- sizeof gets the size of items in bytes */
