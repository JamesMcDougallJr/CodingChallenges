#include <stdio.h>
int atoi(char *str)
{
  char *current = str;
  int value = 0;

  while (*current == ' ')
  {
    current = str + sizeof(char);
  }
  while (*current != '\0')
  {
    current = current + sizeof(char);
  }
  return value;
}

int main(int argc, char *argv[])
{
  for (int i = 1; i < argc; i++)
  {
    printf("%d", atoi(argv[i]));
  }
  return 0;
}