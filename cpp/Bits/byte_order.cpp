#include <stdio.h>

#define BIG_ENDIAN "big"
#define LITTLE_ENDIAN "little"

char* byteorder() {
    int x = 1;
    char* pointer = (char*) &x; // Address of the 1st byte
    return (*pointer > 0) ? LITTLE_ENDIAN : BIG_ENDIAN;
}

void main() {
    printf("%s\n", byteorder());
}