#include <stdlib.h>   /* srand, rand */
#include <stdio.h>    /* printf */
#include <string.h>   /* strcpy */
 
int main() 
{
    const int N = 100;
    const int M = 50;
    
    // creating array of N stroks with M charachters in each
    char stroks[N][M] = { 0 }; // all elements are zero's
    
    // Filling with random data
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M-1; j++) {
            // filling j-th letter of i-th word with value from range a, b, c ... z
            stroks[i][j] = 'a' + rand() % 26;
        }
        // the last characheter of stroka stroks[i], stroks[i][M-1] will be null charachter
        // it is used to print stoka
    }
 
    for (int i = 0; i < N; i++) {
        printf("=");
    }
    printf("\n\nUnsorted string array\n\n");
    
    for (int i = 0; i < N; i++) {
        printf("%s\n", stroks[i]);
    }
    
    for (int i = 0; i < N - 1; i++) {
        for (int j = 0;  j < N - i - 1; j++) {
            // stroks[j] - is a stroka with number j
            // stroks[j][M-1] is a null charachter (termination charachter), hence
            // stroks[j][M-2] - is a last charachter of stroka with number j
            
            if (stroks[j][M-2] > stroks[j+1][M-2]) {
                // Here we changing stroki stroks[j] and stroks[j+1]
                char buff[M] = { 0 };                
                strcpy (buff, stroks[j]);
                strcpy (stroks[j], stroks[j+1]);
                strcpy (stroks[j+1], buff);
            }
        }
    }
    
    for (int i = 0; i < N; i++) {
        printf("=");
    }
    printf("\n\nHere comes sorted string array\n\n");
    
    for (int i = 0; i < N; i++) {
        printf("%s\n", stroks[i]);
    }
    
    printf("\n\nLook at the last charachters, they are sorted! yuppi!\n");
 
    return 0;
}
