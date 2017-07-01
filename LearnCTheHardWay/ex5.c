#include <stdio.h>

/* This is a multiline comment. */
int main(int argc, char *argv[])
{
  int distance = 100; // variable declaration and assignment at the same time

  // this is also a comment
  printf("You are %d miles away.\n", distance);

  return 0; // gives OS the exit value (return code)
}

/* Notes:
- The main function is the one run by operating system.
- The function needs to return an int and take two parameters; an int for the
argument count and an array of char* strings for the arguments
- All statements (except for logic) end in a ; character*/
