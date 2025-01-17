#include <iostream>
using namespace std;
int jdz(int n) {
    if (n >= 0) return n;
    else return -n;
}
int main() {
    int n1, n2, delta, maxdelta = 0, y = 1900;
    cin >> n1 >> n2;
    delta = jdz(n1 - n2);
    for (int i = 2; i < 100; i++) {
        n1 = n2;
        cin >> n2;
        delta = jdz(n1 - n2);
        if (delta >= maxdelta) {
            maxdelta = delta;
            y = 1900 + i;
        }
    }
    cout << y - 1 << ' ' << y;
}
