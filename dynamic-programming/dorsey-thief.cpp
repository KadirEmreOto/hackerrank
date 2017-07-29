#include <stdio.h>

long long int dp[10000];
int N, X, v, a;

int main() {
    
    scanf("%d%d", &N, &X);
    
    for (int j = 0; j < N; j++){
        scanf("%d%d", &v, &a);
            
        for (int i = X - a; 0 < i; i--)
            if (dp[i] > 0 && dp[i + a] < dp[i] + v)
                dp[i + a] = dp[i] + v;
        
        if (a <= X && dp[a] < v)
            dp[a] = v;
    }
    
    if (dp[X] != 0)
        printf("%lld\n", dp[X]);
    else
        printf("Got caught!\n");
    
    return 0;
}

