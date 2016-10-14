#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char const *argv[]) {
    int n, k, a[25];

    scanf("%d%d", &n, &k);
    for (int i=0; i < n; i++) scanf("%d", a+i);

    int pos=k%n;
    int E = 99;
    if(*(a+pos)) E -= 2;

    while (pos != 0) {
        pos = (pos + k) % n;
        if (*(a+pos)) E -= 2;
        E--;
    }

    printf("%d\n", E);

    return 0;
}


