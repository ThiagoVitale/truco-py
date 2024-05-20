#include "base.h"

void shuffle(void* arr[], int size) {
    srand(time(NULL));
    for (int i = size - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        void* temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

void swap(void* arr[], int i, int j) {
    void* temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void shuffle_copy(void* arr[], int size, void* copy[]) {
    for (int i = 0; i < size; i++) {
        copy[i] = arr[i];
    }
    shuffle(copy, size);
}