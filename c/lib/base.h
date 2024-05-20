#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void shuffle(void* arr[], int size);
void swap(void* arr[], int i, int j);
void shuffle_copy(void* arr[], int size, void* copy[]);