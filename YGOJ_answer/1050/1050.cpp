#include <iostream>
#include <string>
using namespace std;
int main() {
    int n, t, d;
    cin >> n;
    wstring tg = L"子丑寅卯辰巳午未申酉戌亥", dz = L"甲乙丙丁戊己庚辛壬癸", nian = L"鼠牛虎兔龙蛇马羊猴鸡狗猪";
    for (int i = n; i < n + 12; i++) {
        t = (i - 4) % 12;
        d = (i - 4) % 10;
        //cout << t << ' ' << d << endl;
        wcout << i << L' ' << dz[d] << tg[t] << L' ' << nian[t] << L"年" << endl;
    }
    return 0;
    //cout << tg << endl << dz << endl << nian;
}