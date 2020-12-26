#include <stdio.h>

void insertionSort(int arr[],int n){
    int i,j,t;
    for(int i=1;i<n;i++){
        t=arr[i];
        for(j=i-1;j>=0 && arr[j]>t;j--)
            arr[j+1]=arr[j];
        arr[j+1]=t;
    }
}

int main() {
    int arr[10],n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	insertionSort(arr,n);
	for(i=0;i<n;i++)
	printf("%d ",arr[i]);
    return 0;
}

