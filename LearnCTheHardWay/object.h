// "if not defined", checks if there's already a #define _object_h; if so skips this code
#ifndef _object_h
#define _object_h

typedef enum {
  NORTH, SOUTH, EAST, WEST
} Direction;

typedef struct {
  char *description;
  int (*init)(void *self);
  void (*describe)(void *self);
  void (*destroy)(void *self);
  void *(*move)(void *self, Direction direction);
  int (*attack)(void *self, int damage);
} Object;

int Object_init(void *self);
void Object_destroy(void *self);
void Object_describe(void *self);
void Object_move(void *self, Direction direction);
int Object_attack(void *self, int damage);
void *Object_new(size_t size, Object proto, char *description);

// This makes a macro, works like a template function that outputs code on right
// whenever we use the code on the left
// This is simply making a short version of the normal way we'd call Object_new
// and avoids potential errors with calling it wrong. The macro "injects" the
// parameters into the line of code on the right.
// Syntax T##Proto says to "concat Proto at the end of T"
// e.g. NEW(Room, "Hello."), would be RoomProto where T##Proto is.
#define NEW(T, N) Object_new(sizeof(T), T##Proto, N)
#define _(N) proto.N // let's us write obj->proto.blah as simply obj->_(blah)

#endif
