#include <stdio.h>
#include <ctype.h>
#include <string.h>

// forward declarations: tells C we will use these functions later
// without actually having to define them
int can_print_it(char ch);
void print_letters(char arg[]);

void print_arguments(int argc, char *argv[]) // *argv[] an array of string literals
{
  int i = 0;

  for(i = 0; i < argc; i++) {
    print_letters(argv[i]);
  }
}

void print_letters(char arg[]) // arg[] an array of characters ie. a string
{
  int i = 0;

  for(i = 0; i < strlen(arg); i++) { // originally: condition was arg[i] != '\0'
    char ch = arg[i];

    if(can_print_it(ch)) {
      printf("'%c' == %d", ch, ch);
    }
  }

  printf("\n");
}

int can_print_it(char ch)
{
  return isalpha(ch) || isblank(ch); // also: isdigit
}

int main(int argc, char *argv[])
{
  print_arguments(argc, argv);
  return 0;
}
