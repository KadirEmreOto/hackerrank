
#include <iostream>
#include <cstring>

int n;
int a[1300];

const int mod = 1000000007;
long long int dipo[1300][1300];
long long int perm[1300][1300];

long long int Solve(int p, int l){
    if (dipo[p][l] != -1) return dipo[p][l];

    if (p == n+1){
        dipo[p][l] = 1;
        return 1;
    }

    if (p == 1)
        dipo[p][l] = Solve(p+1, 1);
    else
        dipo[p][l] = (Solve(p+1, 1)*l) % mod;

    for (int i=1; i < l; i++){
        if (p + i > n || a[p+i] < a[p+i-1]) break;

        else if (p == 1){
            dipo[p][l] += Solve(p+i+1, i+1);
            if (dipo[p][l] > mod)
                dipo[p][l] -= mod;
        }
        else{
            dipo[p][l] += Solve(p+i+1, i+1) * perm[l][i+1];
            if (dipo[p][l] > mod)
                dipo[p][l] %= mod;
        }
    }
    return dipo[p][l];
  }


int main(int argc, char const *argv[]) {
    memset(dipo, -1, sizeof dipo);

    scanf("%d", &n);
    for (int i=0; i < n; i++)
        scanf("%d", &a[i+1]);

    for (int i=1; i < n+1; i++){
        perm[i][1] = i;
        for (int j=2; j < i+1; j++)
            perm[i][j] = (perm[i][j-1] * (i-j+1)) % mod;
    }
    printf("%lld\n", Solve(1, n));

    return 0;
}


