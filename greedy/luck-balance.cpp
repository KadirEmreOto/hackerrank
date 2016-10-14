#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> im;
vector<int> un;

int main(){
    int N, K, l, t;
    scanf("%d%d", &N, &K);

    for (int i=0; i<N; i++){
        scanf("%d%d", &l, &t);

        if (t) im.push_back(l);
        else un.push_back(l);
    }

    sort(im.begin(), im.end());
    int answer = 0;

    for (vector<int>::iterator it=un.begin(); it!=un.end(); ++it)
        answer += *it;

    int c = 0;
    for (vector<int>::iterator it=im.end()-1; it!=im.begin()-1; --it){
        if (c < K) answer += *it;
        else answer -= *it;
        c++;
    }

    printf("%d\n", answer);
}


