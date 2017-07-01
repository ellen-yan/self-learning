#include <stdio.h>

int main(int argc, char *argv[])
{
  int distance = 100;
  float power = 2.345f; // floating point
  double super_power = 56789.4532; // double: more decimal points than float
  char initial = 'X';
  char first_name[] = "Ellen";
  char last_name[] = "Yan";

  printf("You are %d miles away.\n", distance);
  printf("You have %f levels of power.\n", power);
  printf("You have %f awesome super powers.\n", super_power);
  printf("I have an initial %c.\n", initial);
  printf("");
  printf("I have a first name %s.\n", first_name);
  printf("I have a last name %s.\n", last_name);
  printf("My whole name is %s %c. %s.\n",
          first_name, initial, last_name);

  return 0;
}

/* Notes:
- char: character, written with a single-quote, then printed with %c
- char name[] declares string, (an array of characters), written with "
characters, and printed with %s
--> C makes a distinction between single-quote for char and double-quote for
char[] (strings) */
