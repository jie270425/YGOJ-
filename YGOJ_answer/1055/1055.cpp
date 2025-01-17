/*#include <iostream>
#include <string>
#include <vector>
using namespace std;
string s;
int m;
vector<string> cut(string s) {
    vector<string> item;
    string part;
    for (int i = 0; i < s.size(); i++) {
        if ((s[i] == '+' || s[i] == '-') && ))
    }
}
int main() {
    cin >> m >> s;
    int i = 0;
    string mi, num;
    while (i < s.size()) {
        if ()
    }
}*/
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::string a = "-3X^-2 + 5X^3 - 10 + X^4";  // 输入的多项式
    std::string c = "";  // 用于暂存当前项
    std::vector<std::string> list1;  // 用于存储每一项
    size_t i = 0;

    // 遍历整个输入字符串
    while (i < a.length()) {
        // 如果是 '+' 或 '-' 符号，或者是第一次处理项时
        if (a[i] == '+' || a[i] == '-') {
            // 如果当前项不为空，存储它并清空
            if (c.length() != 0) {
                list1.push_back(c);
                c = "";  // 清空当前项
            }
            // 如果是负号，作为当前项的开头
            if (a[i] == '-') {
                c = "-";
            } else {
                c = "+";
            }
        } else if (a[i] == 'X') {
            // 处理 'X' 部分
            c += 'X';
            i++;  // 跳过 'X'
            if (i < a.length() && a[i] == '^') {
                // 如果后面有 '^' 符号，处理指数部分
                c += '^';
                i++;  // 跳过 '^'
                // 处理指数部分，可能是负数
                std::string exponent = "";
                if (a[i] == '-') {
                    exponent += '-';
                    i++;  // 跳过 '-'
                }
                // 收集指数数字
                while (i < a.length() && isdigit(a[i])) {
                    exponent += a[i];
                    i++;
                }
                c += exponent;  // 将指数添加到当前项
                i--;  // 因为循环会多进一位，减去多加的索引
            }
        } else if (isdigit(a[i]) || a[i] == '.') {
            // 处理数字（系数部分）
            while (i < a.length() && (isdigit(a[i]) || a[i] == '.' || a[i] == 'X')) {
                c += a[i];
                i++;
            }
            i--;  // 因为循环会多进一位，减去多加的索引
        }
        i++;
    }

    // 把最后一个项添加到列表
    if (!c.empty()) {
        list1.push_back(c);
    }

    // 输出结果
    for (const auto& term : list1) {
        std::cout << term << std::endl;
    }

    return 0;
}


