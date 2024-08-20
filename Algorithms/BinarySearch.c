#include <stdio.h>

int binarySearch(int arr[], int n, int k) {
    int ll = 0, ul = n - 1;
    while (ll <= ul) {
        int mid = (ll + ul) / 2;
        if (arr[mid] == k)
            return mid + 1;  // Return position (1-based index)
        else if (arr[mid] < k)
            ll = mid + 1;
        else
            ul = mid - 1;
    }
    return -1;  // Element not found
}

int main() {
    int arr[10], n, k, i;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    scanf("%d", &k);
    printf("%d", binarySearch(arr, n, k));
    return 0;
}
