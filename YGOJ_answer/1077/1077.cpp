#include <iostream>
using namespace std;
bool isSymPeak(int flag, int steps) {
    if (flag == -1 && steps == 0) return true;
    return false;
}
int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];
    int flag = 0, steps = 0, count = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] > a[i - 1]) {
            if (isSymPeak(flag, steps)) count += 1;
            if (flag == 0 || flag == -1) steps = 1;
            else steps += 1;
        } else if (a[i] == a[i - 1]) {
            if (isSymPeak(flag, steps)) count += 1;
            steps = 0;
            flag = 0;
        } else {
            steps -= 1;
            flag = -1;
        }
    }
    if (isSymPeak(flag, steps)) count += 1;
    cout << count;
    return 0;
}