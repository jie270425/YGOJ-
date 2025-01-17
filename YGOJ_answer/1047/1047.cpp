#include <iostream>
#include <vector>
#include <string>

using namespace std;

string change(int n, int b) {
    string x = "";
    while (n > 0) {
        int c = n % b;
        x = to_string(c) + x;
        n = n / b;
    }
    return x;
}

bool pd(const string &a, const string &b) {
    char c = a[0], d = b[0];
    int i = 0, j = 0;
    if (c != d) {
        return false;
    }
    while (i < a.length() && j < b.length()) {
        if (a[i] == b[j]) {
            i++;
        }
        j++;
    }
    return i == a.length();
}

int main() {
    int m, n;
    cin >> m >> n;
    bool flag = true;
    for (int i = 2; i < 9; i++) {
        string m1 = change(m, i);
        string n1 = change(n, i);
        vector<int> list1(i, 0);
        vector<int> list2(i, 0);
        
        for (char k : m1) {
            list1[k - '0']++;
        }
        for (char k : n1) {
            list2[k - '0']++;
        }
        
        if (pd(m1, n1) && m1 != n1) {
            cout << i << " ";
            for (int j = 0; j < i; j++) {
                list2[j] -= list1[j];
            }
            for (int k = 0; k < list2.size(); k++) {
                if (list2[k] != 0) {
                    for (int l = 0; l < list2[k]; l++) {
                        cout << k;
                    }
                }
            }
            cout << endl;
            flag = false;
        }
    }
    if (flag) {
        cout << "404 not found" << endl;
    }
    return 0;
}
