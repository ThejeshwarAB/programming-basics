#include <stdio.h>

int linearSearch(int arr[],int n,int k){
	for(int i=0;i<n;i++)
		if(arr[i]==k)
			return i+1;
	return -1;
}

int main() {
    int arr[10],n,k,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	scanf("%d",&k);
	printf("%d",linearSearch(arr,n,k));
    return 0;
}
