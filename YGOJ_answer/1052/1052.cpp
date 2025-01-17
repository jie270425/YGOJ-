#include <iostream>
using namespace std;
int data[1000000 + 10];
int main() {
    int n = 0, num, i = 0;
    while (cin >> num) {
        data[n++] = num;
    }
    while (i < n) {
        if (data[i] == 0) {
            if (i + 1 < n && data[i + 1] == 0) {
                cout << 0 << ' ';
                i += 2;
            } else if (i + 2 < n) {
                int repeat_count = data[i + 1];
                int value = data[i + 2];
                for (int j = 0; j < repeat_count; j++) {
                    cout << value << ' ';
                }
                i += 3;
            }
        } else {
            cout << data[i] << ' ';
            i++;
        }
    }
    return 0;
}
