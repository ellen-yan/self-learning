#include <stdio.h>

int main(int argc, char *argv[])
{
  if(argc != 2) {
    printf("ERROR: You need one argument.\n");
    // this is how you abort a program
    return 1;
  }

  int i = 0;
  for(i = 0; argv[1][i] != '\0'; i++) {
    char letter = argv[1][i];

    switch(letter) {
      case 'a':
      case 'A':
        printf("%d: 'A'\n", i);
        break;

      case 'e':
      case 'E':
        printf("%d: 'E'\n", i);
        break;

      case 'i':
      case 'I':
        printf("%d: 'I'\n", i);
        break;

      case 'o':
      case 'O':
        printf("%d: 'O'\n", i);
        break;

      case 'u':
      case 'U':
        printf("%d: 'U'\n", i);
        break;

      case 'y':
      case 'Y':
        if(i > 2) {
          // it's only sometimes Y
          printf("%d: 'Y'\n", i);
        }
        break;

      default:
        printf("%d: %c is not a vowel\n", i, letter);
        // jumped to this spot, nothing afterward, no break needed
    }
  }

  return 0;
}
/* Notes:
- a switch statement is different from an if statement because
it is really a "jump table". Instead of any boolean expressions,
you can only put expressions that result in integers and these
integers are used to calculate jumps from the top of the switch
to the part that matches the value
- compiler translates each case statement into a location in the program
 and calculates the value we're looking at (hence the position we're jumping to).
 If it's too far from any value then the value is adjusted to the default
 position
 - if there's no code after a switch statement it falls through to the next case
 - always include a default branch so that you catch any missing inputs
 - don't allow a "fall through" unless you really want it, and it's a good idea
 to add a comment //fallthrough so people know it's on purpose
 - tip: always write the case and the break before you write the code that goes
 in it */
