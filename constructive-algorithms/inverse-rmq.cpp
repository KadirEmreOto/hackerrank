#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>

#define fi first
#define se second
#define sz(a) ((int)a.size())

using namespace std;

int n, result[(1<<20) + 10], lg[(1<<20) + 10];
map<int, int> fre;
set<int> s[1000000],cnt;

int main(int argc, char const *argv[]) {
    cin >> n;

    for (int i=0, k; i < 2*n-1; i++){
        scanf("%d", &k);
        fre[k]++;
    }

    for( map<int,int>::iterator it=fre.begin() ; it!=fre.end() ; it++ )
        s[it->se].insert(it->fi);

    for (int i=0; i<=18; i++)
        for (int k=1<<i; k < 1<<(i+1); k++)
            lg[k] = i+1;

    if( sz(s[lg[n]]) != 1 ){
        cout << "NO" << endl;
        return 0;
    }

    result[0] = *s[lg[n]].begin();

    for (int i=1; i < 2 * n; i++){
        if (i & 1) {
            result[i] = result[i>>1];
            for (int j=i; j <= 2*n; j<<=1)
                result[j] = result[i>>1];

            continue;
        }

        int pl=lg[n] - lg[i] + 1;
        set<int>::iterator it=s[pl].upper_bound(result[(i>>1)-1]);
        if ( it!=s[pl].end() ) {result[i] = *it; s[pl].erase(it); }
        else{
            cout << "NO" << endl;
            return 0;
        }
    }

    for (int i=0; i<n; i++){
        if (cnt.find(result[2*n-i-1]) == cnt.end())
            cnt.insert(result[2*n-i-1]);
        else{
            cout << "NO" << endl;
            return 0;
        }
    }

    cout << "YES" << endl;
    for (int i=0; i < 2*n-1; i++)
        printf("%d ", result[i]);
    cout << endl;

    return 0;
}

