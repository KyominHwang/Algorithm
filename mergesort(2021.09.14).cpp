#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <climits>
using namespace std;

vector<pair<int, string>> sorted;
int idx = 0;

void merge(vector<pair<int, string>>& v, int p, int q, int r){

    int left = p;
    int right = r;
    int mid = q + 1;

    while(left <= q && mid <= r){
        if(v[left].first >= v[mid].first) sorted.push_back(v[left++]);
        else sorted.push_back(v[mid++]);
    }

    for(int i = mid ; i <= r ; i++)
        sorted.push_back(v[i]);

    for(int i = left ; i <= q ; i++)
        sorted.push_back(v[i]);

    for(int i = p ; i <= r ; i++)
        v[i] = sorted[idx++];
}

void mergesort(vector<pair<int, string> >& v, int p, int r){
    if(p < r){
        int q = (p + r) / 2;
        mergesort(v, p, q);
        mergesort(v,q + 1, r);
        merge(v, p, q, r);
    }
}

int main(void) {
    int n;
    vector<pair<int, string> > v;

    cin >> n;

    for (int i=0; i<n; i++){
        int d;
        string s;
        cin >> d >> s;
        v.push_back(pair<int,string>(d,s));
    }

    // merge sort
    mergesort(v, 0, v.size()-1);

    for (int i=0; i<n; i++){
        cout << v[i].first << ' ' << v[i].second << endl;
    }

    return 0;
}