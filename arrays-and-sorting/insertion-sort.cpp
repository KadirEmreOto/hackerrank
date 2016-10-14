#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

#define fi first
#define se second

using namespace std;

typedef pair<int,int> ii;

void update(int index, int pos, int low, int high, int* seg){
    if (low <= index && index <= high){ // # total overlap
        seg[pos] += 1;

        if (low == high) return;

        int mid = (low + high) / 2;
        if (index <= mid) update(index, 2*pos+1, low, mid, seg);
        else update(index, 2*pos+2, mid+1, high, seg);
    }
}

int query(int qlow, int qhigh, int pos, int low, int high, int *seg){
    if (qlow <= low && high <= qhigh) return seg[pos]; // Total overlap
    else if (high < qlow || qhigh < low) return 0; // no overlap

    int mid = (low + high) / 2;
    int left  = query(qlow, qhigh, 2*pos+1, low, mid, seg);
    int right = query(qlow, qhigh, 2*pos+2, mid+1, high, seg);

    return left + right;
}

int main(int argc, char const *argv[])
{
    int T, N, nu;
    ii ar[100001];
    int seg[4 * 100000];
    scanf("%d", &T);

    for (int t = 0; t < T; ++t)
    {
        scanf("%d", &N);
        
        for (int i = 0; i < N; ++i){
            scanf("%d", &ar[i].fi);
            ar[i].se=i;
        }

        sort(ar, ar+N);
        reverse(ar, ar+N);

        memset(seg, 0, sizeof(seg));
        
        long long int ans = 0;

        for (int i=0; i < N; i++){
            ans += query(0, ar[i].se - 1, 0, 0, N-1, seg);
            update(ar[i].se, 0, 0, N-1, seg);
        }
        printf("%lld\n", ans);

    }

    return 0;
}
