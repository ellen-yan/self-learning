/* Extra credit exercise for chapter 17:
   Creating a stack data structure */

#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

// Stack operations:
// push, pop, peek, isempty

#define MAX_DATA 512
#define MAX_NUM_ELEMENTS 10 // max size of stack

struct Stack {
  char *stack_array[MAX_NUM_ELEMENTS];
};

void die(char *message, struct Stack *s)
{
  if(errno) {
    perror(message);
  } else {
    printf("ERROR: %s\n", message);
  }
  free(s);
  exit(1);
}

struct Stack *create_stack (char *element)
{
  struct Stack *s = malloc(sizeof(struct Stack) * MAX_DATA);
  if(!s) die("Memory error.", NULL);
  assert (s != NULL);
  s->stack_array[0] = strdup(element);
  //printf("%d\n", s->stack_array[1] == NULL); This evaluates to true
  printf("Created New Stack.\n");
  return s;
}

void print_stack(struct Stack *s)
{
  assert (s != NULL);
  printf("Current Stack:\n");

  int i = 0;
  for(i = 0; s->stack_array[i] != NULL & i < sizeof(s->stack_array)/sizeof(s->stack_array[0]); i++) {
    printf("element number %d: %s\n", i + 1, s->stack_array[i]);
  }
}

struct Stack *push (struct Stack *s, char *element)
{
  assert (s != NULL);
  int i = 0;
  int j = 0;
  for (i = 0; s->stack_array[i] != NULL && i < MAX_NUM_ELEMENTS; i++) {
    j = i;
  }
  if (i == MAX_NUM_ELEMENTS) {
    die ("Stack full, could not add the last element", s);
  } else {
    s->stack_array[j + 1] = element;
    printf("Push successful for element %d.\n", j + 2);
  }
  return s;
}

char *pop(struct Stack *s)
{
  assert(s != NULL);
  if(s->stack_array[0] == NULL) {
    die ("No items left on stack, pop failed.", s);
  }
  char *element;

  int i = 0;
  for (i = 0; s->stack_array[i] != NULL && i < MAX_NUM_ELEMENTS; i++) {
  }

  element = s->stack_array[i - 1];
  s->stack_array[i - 1] = NULL;

  printf("Pop successful.\n");
  return element;
}

char *peek(struct Stack *s)
{
  assert(s != NULL);
  char *element = NULL;
  int i = 0;
  for (i = 0; s->stack_array[i] != NULL && i < MAX_NUM_ELEMENTS; i++) {
  }
  if(i == 0) {
    element = NULL;
  } else {
    element = s->stack_array[i - 1];
  }

  return element;
}

int isempty(struct Stack *s)
{
  assert(s != NULL);
  return s->stack_array[0] == NULL;
}

int main(int argc, char *argv[])
{
  if (argc < 2) {
    die ("No entry.", NULL);
  }
  struct Stack *s = create_stack(argv[1]);
  int i = 2;
  for(i = 2; i < argc; i++) {
    s = push(s, argv[i]);
  }
  print_stack(s);
  printf("Peek: %s\n", peek(s));
  pop(s);
  printf("Is empty: %d\n", isempty(s));
  print_stack(s);
  return 0;
}
