#include <stdio.h>

int binarySearch(int arr[],int n,int k){
    int ll=0,ul=n-1;
    int mid=(ll+ul)/2;
	while(ll<ul){
	    if(arr[mid]==k)
	    return mid+1;
	    else if(arr[mid]<k)
	    ll+=1;
	    else
	    ul-=1;
	}
	return -1;
}

int main() {
    int arr[10],n,k,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	scanf("%d",&k);
	printf("%d",binarySearch(arr,n,k));
    return 0;
}
