#include <stdio.h>

int main(int argc, char *argv[])
{
  int numbers[4] = {1}; // rest of the chars are filled in with 0s
  char name[6] = {'a'}; // rest of the chars are filled in with '\0' automatically

  // first, print them out raw
  printf("numbers: %d %d %d %d\n",
          numbers[0], numbers[1],
          numbers[2], numbers[3]);

  printf("name each: %c %c %c %c %c %c\n",
          name[0], name[1], name[2],
          name[3], name[4], name[5]);

  printf("name: %s\n", name);

  // setup the numbers
  numbers[0] = 1;
  numbers[1] = 2;
  numbers[2] = 3;
  numbers[3] = 4;

  // setup the name
  name[0] = 'E';
  name[1] = 'l';
  name[2] = 'l';
  name[3] = 'e';
  name[4] = 'n';
  name[5] = '\0';

  // then print them out initialized
  printf("numbers: %d %d %d %d\n",
          numbers[0], numbers[1],
          numbers[2], numbers[3]);

  printf("name each: %c %c %c %c %c %c\n",
          name[0], name[1], name[2],
          name[3], name[4], name[5]);

  // print the name like a string
  printf("name: %s\n", name);

  // another way to use name
  char *another = "Ellen"; // should use this instead of char [] for string literals

  printf("another: %s\n", another);
  printf("another each: %c %c %c %c %c %c\n",
          another[0], another[1], another[2],
          another[3], another[4], another[5]);

  return 0;
}
