#include <stdio.h>

void bubbleSort(int arr[],int n){
    int i,j;
    for(i=0;i<n-1;i++)
        for(j=0;j<n-i-1;j++)
            if(arr[j]>arr[j+1])
                {
                    int t=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=t;
                }
    
}

int main() {
    int arr[10],n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	bubbleSort(arr,n);
	for(i=0;i<n;i++)
	printf("%d ",arr[i]);
    return 0;
}

