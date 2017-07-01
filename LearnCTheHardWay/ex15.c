#include <stdio.h>

int main(int argc, char *argv[])
{
  // create two arrays we care about
  int ages[] = {23, 43, 12, 89, 2};
  char *names[] = {
    "Alan", "Frank",
    "Mary", "John", "Lisa"
  };

  // safetly get the size of ages
  int count = sizeof(ages) / sizeof(int);
  int i = 0;

  // first way of using indexing
  for(i = count - 1; i >= 0; i--) {
    printf("%s has %d years alive.\n",
            names[i], ages[i]);
    printf("address of name: %p, address of age: %p\n", &names[i], &ages[i]);
  }

  printf("---\n");

  // setup the pointers to the start of the arrays
  int *cur_age = ages; // points at ages; * means value of
  char **cur_name = names;
  // note the similarity: int * points to the first element of an integer array, and
  // a string is a char *, i.e. points to the first char of an array of chars
  printf("%p\n", &cur_name);
  printf("%lu\n", sizeof(cur_name));
  // second way using pointers
  for(i = count - 1; i >= 0; i--) {
    printf("%s is %d years old.\n",
            *(cur_name+i), *(cur_age+i)); // read as value of (pointer cur_name + 1)
  }

  printf("---\n");

  // third way, pointers are just arrays
  for(i = count - 1; i >= 0; i--) {
    printf("%s is %d years old again.\n",
            cur_name[i], cur_age[i]); // accessing element of array is same for a pointer
  }

  printf("---\n");

  // fourth way with pointers in a stupid complex way
  for(cur_name = names, cur_age = ages;
          (cur_age - ages) < count;
          cur_name++, cur_age++) // calculate location based on pointer arithmetic
  {
    printf("%s lived %d years so far.\n",
            *cur_name, *cur_age); // print the value of wherever cur_name and cur_age are pointing
  }

  printf("----\n");

  // exercise making fourth one go backward
  for(cur_name = &names[count - 1], cur_age = &ages[count - 1];
          (cur_age - ages) >= 0;
          cur_name--, cur_age--) // calculate location based on pointer arithmetic
  {
    printf("%s lived %d years so far.\n",
            *cur_name, *cur_age); // print the value of wherever cur_name and cur_age are pointing
    printf("cur_name pointer: %p, cur_age pointer: %p\n", cur_name, cur_age);
  }
  return 0;
}

/* Notes:
- A pointer is simply an address pointing somewhere inside the computer's memory
with a type specifier so you get the right size of data with it
- You can also get values out with them, put new values in, and use array operations
- The purpose of a pointer is to let you manually index into blocks or memory when
an array won't do it right; in almost all other cases you actually want to use an
array, but if you have to work with a raw block of memory that's where a pointer
comes in since it gives you direct access to a block of memory so you can work
with it
- You can use either syntax for most array or pointer operations

Practical Pointer Usage:
Four primary useful things:
1. Ask the OS for a chunk of memory and use a pointer to work with it, includes
strings and structs
2. Passing large blocks of memory (like large structs) to functions with a
pointer so you don't have to pass the whole thing to them
3. Taking the address of a function so you can use it as a dynamic callback
4. Complex scanning of chunks of memory such as converting bytes off a network
socket into data structures or parsing files

- For nearly everything else, should be using arrays
- Nowadays array usage is optimized in machine code so it runs the same as using
pointers. Only use pointers as performance optimization if you have to

Pointer Lexicon:
- type *ptr: a pointer of type name ptr
- *ptr: the value of whatever ptr is pointed at
- *(ptr + i): the value of (whatever ptr is pointed at plus i)
- &thing: the address of thing
- type *ptr = &thing: a pointer of type named ptr set to the address of thing
- ptr++: increment where ptr points

- ** POINTERS ARE NOT ARRAYS: e.g. sizeof(cur_age) gets size of pointer not size
of what it points at
*/
