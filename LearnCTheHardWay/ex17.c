#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define MAX_DATA 512 // constants
#define MAX_ROWS 100

struct Address {
  int id;
  int set;
  char name[MAX_DATA];
  char email[MAX_DATA];
};

struct Database {
  struct Address rows[MAX_ROWS]; // fixed memory size: less efficient but easier to store and read
};

struct Connection {
  // functions like fopen, fread, fclose, and rewind works with files. Each of
  // these functions works on a FILE struct defined by the C standard library
  FILE *file;
  struct Database *db;
};
// small program, we can make a single function that kills the program with an
// error if there's anything wrong
void die(const char *message, struct Connection *conn)
{
  // when you have an error return from a function, it will usually set an
  // "external" variable called errno to say exactly what error happened (these
  // are numbers), so we can use perror to print the error message
  if(errno) {
    perror(message);
  } else {
    printf("ERROR: %s\n", message);
  }

  if(conn) {
    if(conn->file) fclose(conn->file);
    if(conn->db) free(conn->db);
    free(conn);
  }

  exit(1);
}

void Address_print(struct Address *addr)
{
  printf("%d %s %s\n",
          addr->id, addr->name, addr->email);
}

void Database_load(struct Connection *conn)
{
  int rc = fread(conn->db, sizeof(struct Database), 1, conn->file);
  if(rc != 1) die("Failed to load database.", conn);
}

struct Connection *Database_open(const char *filename, char mode)
{
  // allocating large amount of memory with malloc
  struct Connection *conn = malloc(sizeof(struct Connection));
  if(!conn) die("Memory error", conn);

  conn->db = malloc(sizeof(struct Database));
  if(!conn->db) die("Memory error", conn);

  if(mode == 'c') {
    conn->file = fopen(filename, "w");
  } else {
    conn->file = fopen(filename, "r+");

    if(conn->file) {
      Database_load(conn);
    }
  }

  if (!conn->file) die("Failed to open the file", conn);

  return conn;
}

void Database_close(struct Connection *conn)
{
  if(conn) {
    if(conn->file) fclose(conn->file);
    if(conn->db) free(conn->db);
    free(conn);
  }
}

void Database_write(struct Connection *conn)
{
  rewind(conn->file);

  int rc = fwrite(conn->db, sizeof(struct Database), 1, conn->file);
  if(rc != 1) die("Failed to write database.", conn);

  rc = fflush(conn->file);
  if(rc == -1) die("Cannot flush database.", conn);
}

void Database_create(struct Connection *conn)
{
  int i = 0;

  for(i = 0; i < MAX_ROWS; i++) {
    // make a prototype to initialize it
    struct Address addr = {.id = i, .set = 0};
    // then just assign it
    conn->db->rows[i] = addr;
  }
}

void Database_set(struct Connection *conn, int id, const char *name, const char *email)
{
  // nested struct pointers example:
  // get the i element of rows which is in db which is in conn, then get the
  // address of it
  struct Address *addr = &conn->db->rows[id];
  if(addr->set) die("Already set, delete it first", conn);

  addr->set = 1;
  // WARNING: bug, read the "How to break it" and fix this
  char *res = strncpy(addr->name, name, MAX_DATA);
  addr->name[MAX_DATA - 1] = '\0';
  // demonstrate the strncpy bug
  if(!res) die("Name copy failed", conn);

  res = strncpy(addr->email, email, MAX_DATA);
  addr->email[MAX_DATA - 1] = '\0';
  if(!res) die("Email copy failed", conn);
}

void Database_get(struct Connection *conn, int id)
{
  struct Address *addr = &conn->db->rows[id];

  if(addr->set) {
    Address_print(addr);
  } else {
    die("ID is not set", conn);
  }
}

void Database_delete(struct Connection *conn, int id)
{
  // copying struct prototypes:
  // using temporary local address, initializing id and set fields, and copying
  // it into the rows array
  // This trick makes sure all fields except set and id are initialized to 0s
  // and is actually easier to write
  // - shouldn't be using memcpy to do these kinds of struct copying operations
  struct Address addr = {.id = id, .set = 0};
  conn->db->rows[id] = addr;
}

void Database_list(struct Connection *conn)
{
  int i = 0;
  struct Database *db = conn->db;

  for(i = 0; i < MAX_ROWS; i++) {
    struct Address *cur = &db->rows[i];

    if(cur->set) {
      Address_print(cur);
    }
  }
}

int main(int argc, char *argv[])
{
  if(argc < 3) die("USAGE: ex17 <dbfile> <action> [action params]", NULL);

  char *filename = argv[1];
  char action = argv[2][0];
  struct Connection *conn = Database_open(filename, action);
  int id = 0;

  if(argc > 3) id = atoi(argv[3]); // take string for the id and convert to int id
  if(id >= MAX_ROWS) die("There's not that many records.", conn);

  switch(action) {
    case 'c':
        Database_create(conn);
        Database_write(conn);
        break;

    case 'g':
        if(argc != 4) die("Need an id to get", conn);

        Database_get(conn, id);
        break;

    case 's':
        if(argc != 6) die("Need id, name, email to set", conn);

        Database_set(conn, id, argv[4], argv[5]);
        Database_write(conn);
        break;

    case 'd':
        if(argc != 4) die("Need id to delete", conn);

        Database_delete(conn, id);
        Database_write(conn);
        break;

    case 'l':
        Database_list(conn);
        break;
    default:
        die("Invalid action, only: c=create, g=get, s=set, d=del, l=list", conn);
  }

  Database_close(conn);

  return 0;
}

/* Notes:
Heap vs. Stack Allocation:
- heap: all the remaining memory in computer, can be accessed with the function
malloc to get more. Each time malloc is called, the US uses internal functions to
register that piece of memory to us, then returns a pointer to it. When done,
use free to return it to the OS so that it can be used by other programs.
Otherwise, will cause program to "leak" memory
- stack: special region of memory that stores temporary variables each function
creates as locals to that function. Each argument to a function is "pushed" onto
the stack and then used inside the function. This also happens with all the local
variables like char action and int id in main
- main advantage of using stack is simply that when the function exits, the C
compiler "pop" these variables off the stack to clean them up. This is simple
and prevents memory leaks if the variable is on the stack
- easiest way to keep straight heap vs. stack is that if we didn't get it from
malloc or a function that got it from malloc, then it's on the stack

Three primary problems with stacks and heaps:
1. if you get a block of memory from malloc, and have that pointer on the stack,
then when the function exits, the pointer will get popped off and lost unless we
save that somewhere
2. if you put too much data on the stack (like large structs and arrays), then
you will cause a "stack overflow" and the program will abort. In this case, use
the heap with malloc
3. if you take a pointer to something on the stack, and then pass that or return
it from your function, then the function receiving it will "segmentation fault"
because the actual data will get popped off and disappear (i.e. the something
on the stack was only on the stack because of the function)

- when a program exits the OS will clean up all the resources, but sometimes
not immediately */
