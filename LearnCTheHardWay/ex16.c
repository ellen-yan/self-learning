#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

struct Person { // similar to row of database table or a class in OOP
  char *name;
  int age;
  int height;
  int weight;
};

// function for creating a Person
struct Person *Person_create(char *name, int age, int height, int weight)
{
  struct Person *who = malloc(sizeof(struct Person)); // malloc (memory allocate) asks OS to give piece of raw memory
  assert(who != NULL); // checking to see if we have a valid piece of memory
  // initialize each field with x->y syntax
  who->name = strdup(name); // saves a copy of a string and returns a pointer to it
  who->age = age;
  who->height = height;
  who->weight = weight;

  return who;
}

void Person_destroy(struct Person *who)
{
  assert(who != NULL); // make sure input is not bad
  // use free to return the memory we got with malloc and strdup (otherwise we get "memory leak")
  free(who->name);
  free(who);
}

void Person_print(struct Person *who)
{
  printf("Name: %s\n", who->name);
  printf("\tAge: %d\n", who->age);
  printf("\tHeight: %d\n", who->height);
  printf("\tWeight: %d\n", who->weight);
}

// Extra credit
struct Persontest {
  char name[20];
  int age;
  int height;
  int weight;
};

struct Persontest Persontest_create(char name[], int age, int height, int weight) {
  struct Persontest who;
  strcpy(who.name, name);
  who.age = age;
  who.height = height;
  who.weight = weight;

  return who;
}

void Persontest_print(struct Persontest who) {
  printf("name: %s\n", who.name);
}

int main(int argc, char *argv[])
{
  // make two people structures
  struct Person *joe = Person_create(
          "Joe Alex", 32, 64, 140);

  struct Person *frank = Person_create(
          "Frank Blank", 20, 72, 180);

  // print them out and where they are in memory
  printf("Joe is at memory location %p:\n", joe);
  Person_print(joe);

  printf("Frank is at memory location %p:\n", frank);
  Person_print(frank);

  // make everyone age 20 years and print them again
  joe->age += 20;
  joe->height -= 2;
  joe->weight += 40;
  Person_print(joe);

  frank->age += 20;
  frank->weight += 20;
  Person_print(frank);
  //Person_print(NULL); // segmentation fault
  //Person_destroy(NULL);

  // destroy them both so we clean up
  Person_destroy(joe);
  Person_destroy(frank);

  // extra credit
  struct Persontest sara = Persontest_create("Sara Black", 10, 60, 130);
  Persontest_print(sara);
  return 0;
}


/* Notes:
- struct Person is a compound data type (and can be passed as a cohesive
grouping to functions)
- can use x->y syntax to access individual parts of a struct
- x.y syntax for struct that doesn't need a pointer
- need to define all the struct and functions before the main function */
