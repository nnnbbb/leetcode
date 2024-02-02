#include <stdio.h>
#include <stdlib.h>

int compare_int(const void* a, const void* b) {
    int* pa = (int*)a;
    int* pb = (int*)b;
    int n1 = *pa;
    int n2 = *pb;
    return n2 - n1;
};
int compare_float(const void* a, const void* b) {
    // float* pa = (float*)a;
    // float* pb = (float*)b;
    float n1 = *(float*)a;
    float n2 = *(float*)b;
    if (n2 - n1 > 0) {
        return -1;
    } else {
        return 1;
    }
};
void qsort_int() {
    int arr[8] = {8, 3, 5, 4, 6, 7, 1, 2};
    qsort(arr, 8, sizeof(int), compare_int);
    for (size_t i = 0; i < 8; i++) {
        printf("%d ", arr[i]);
    }
};
void qsort_float() {
    float arr[8] = {8.1, 3.1, 5.1, 4.1, 6.1, 7.1, 1.1, 2.1};
    qsort(arr, 8, sizeof(float), compare_float);
    for (size_t i = 0; i < 8; i++) {
        printf("%.2f ", arr[i]);
    }
};
int main() {
    qsort_int();
    printf("\n");
    qsort_float();
};