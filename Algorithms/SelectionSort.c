#include <stdio.h>

void selectionSort(int arr[],int n){
    int i,j,min,t;
    for(i=0;i<n-1;i++){
        min=i;
        for(j=i+1;j<n;j++){
            if(arr[j]<arr[min])
                min=j;
        }
        t=arr[i];
        arr[i]=arr[min];
        arr[min]=t;
    }
}

int main() {
    int arr[10],n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	selectionSort(arr,n);
	for(i=0;i<n;i++)
	printf("%d ",arr[i]);
    return 0;
}

