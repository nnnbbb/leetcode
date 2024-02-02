#include <stdio.h>
#include <stdlib.h>

void build_tree(int arr[], int tree[], int node, int start, int end) {
    if (start == end) {
        tree[node] = arr[start];
    } else {
        int mid = (start + end) / 2;
        int left_node = 2 * node + 1;
        int right_node = 2 * node + 2;
        build_tree(arr, tree, left_node, start, mid);
        build_tree(arr, tree, right_node, mid + 1, end);
        tree[node] = tree[left_node] + tree[right_node];
    }
};

void update_tree(int arr[], int tree[], int node, int start, int end, int i, int v) {
    if (start == end) {
        arr[i] = v;
        tree[node] = v;
        return;
    }
    int mid = (start + end) / 2;
    int left_node = 2 * node + 1;
    int right_node = 2 * node + 2;
    if (i >= start && i <= mid) {
        update_tree(arr, tree, left_node, start, mid, i, v);
    } else {
        update_tree(arr, tree, right_node, mid + 1, end, i, v);
    }
    tree[node] = tree[left_node] + tree[right_node];
};

int query_tree(int arr[], int tree[], int node, int start, int end, int L, int R) {
    printf("start = %d\n", start);
    printf("end = %d\n", end);
    printf("\n");
    
    if (R < start || L > end) {
        return 0;
    } else if (start == end) {
        return tree[node];
    } else if (L <= start && end <= R) {
        return tree[node];
    } else {
        int mid = (start + end) / 2;
        int left_node = 2 * node + 1;
        int right_node = 2 * node + 2;

        int left_sum = query_tree(arr, tree, left_node, start, mid, L, R);
        int right_sum = query_tree(arr, tree, right_node, mid + 1, end, L, R);
        return left_sum + right_sum;
    };
};

void _print(int arr[], int size) {
    for (size_t i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
};

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11};
    int size = 6;
    int tree[1000] = {0};

    build_tree(arr, tree, 0, 0, size - 1);

    _print(tree, 15);

    update_tree(arr, tree, 0, 0, size - 1, 4, 6);

    _print(tree, 15);

    int s = query_tree(arr, tree, 0, 0, size - 1, 2, 5);
    printf("s = %d\n", s);
};