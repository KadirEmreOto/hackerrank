#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int getWays(int squares_size, int* squares, int d, int m){
    int i = 0;
    int t = 0;
    int answer = 0;
    for (i = 0; i < m; i++) t += squares[i];
    if (t == d) answer += 1;
    
    for (i = m; i < squares_size; i++){
        t += squares[i];
        t -= squares[i-m];
        if (t == d) answer++;
    }
    return answer;
}

int main() {
    int n; 
    scanf("%d",&n);
    int *s = malloc(sizeof(int) * n);
    for(int s_i = 0; s_i < n; s_i++){
       scanf("%d",&s[s_i]);
    }
    int d; 
    int m; 
    scanf("%d %d",&d,&m);
    int result = getWays(n, s, d, m);
    printf("%d\n", result);
    return 0;
}

