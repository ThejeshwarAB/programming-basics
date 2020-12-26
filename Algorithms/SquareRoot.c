#include <stdio.h>
#include <math.h>

int main() {
    double n,x,root;
    scanf("%lf",&n);
    x=n;
    while(1){
        root=0.5*(x+(n/x));
        if((n-(root*root))>=0)
            break;
        else
            x=root;
    }
    printf("%.3lf",root);
    return 0;
}