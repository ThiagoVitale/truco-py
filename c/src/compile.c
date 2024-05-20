#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdbool.h>


#ifdef __linux__
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <dirent.h>

#define BIN_PATH "../bin/"
#define SRC_PATH "./"
#define LIB_PATH "../lib/"

void compileCode() {
    // Code for compiling on Linux
    // ...
    // Search for all .c files in the lib folder
    // Compile them and generate .o files
    // Compile the main.c file and generate the executable

    // Open the lib directory
    DIR *dir = opendir(LIB_PATH);
    if (dir == NULL) {

        perror("Failed to open lib directory");
        return;
    }

    // Count the number of .c files in the lib directory
    int count = 0;
    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == 8 && strstr(entry->d_name, ".c") != NULL) { // 8 = DT_REG
            count++;
        }
    }
    rewinddir(dir);

    // Allocate memory for the array of file paths
    char **filePaths = malloc(count * sizeof(char *));
    if (filePaths == NULL) {
        perror("Failed to allocate memory for file paths");
        closedir(dir);
        return;
    }

    // Store the paths of the .c files in the lib directory
    int index = 0;
    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == 8 && strstr(entry->d_name, ".c") != NULL) {
            char *filePath = malloc(strlen(LIB_PATH) + strlen(entry->d_name) + 1);
            if (filePath == NULL) {
                perror("Failed to allocate memory for file path");
                closedir(dir);
                free(filePaths);
                return;
            }
            strcpy(filePath, LIB_PATH);
            strcat(filePath, entry->d_name);
            filePaths[index] = filePath;
            index++;
        }
    }

    closedir(dir);

    // Use the filePaths array as needed
    for (int i = 0; i < count; i++) {
        printf("File path: %s\n", filePaths[i]);
    }
    // Free the memory allocated for the file paths
    for (int i = 0; i < count; i++) {
        free(filePaths[i]);
    }
    free(filePaths);

    // ...
}

#else
void compileCode() {
    // Code for compiling on other platforms
    // ...
}
#endif


int main(int argc, char const *argv[])
{
    compileCode();
    return 0;
}