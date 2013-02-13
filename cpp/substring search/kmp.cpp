#include <iostream>
#include <string.h>

using std::cout;

#define prs(str, N) { for (int k = 0; k < N; k++) cout << k << "-" << str[k] << " "; }

#define prss(str, N) for(int k = 0; k < N; k++) { cout << " "; } \
    cout << str << " - i=" << i << " j="<< j << " > sh=" << shift[j] << std::endl;

const int N = 1000;

int kmp_search (char* str, char* substr) {
    cout << str << std::endl;
    int str_l = strlen(str);
    int substr_l = strlen(substr);

    if (substr_l == 1) {
        int i = 0;
        while (str[i] != substr[0]) { i++; }
        return i;
    }

    int shift[N];
    shift[0] = 0;

    for (int i = 1; i < substr_l; i++) {
        if (substr[i] == substr[shift[i - 1]]) shift[i] = shift[i - 1] + 1;
        else shift[i] = 0;
    }

    //prs(shift, substr_l);

    for (int i = 0, j = 0; i < str_l - substr_l + 1;) {

        for (; j < substr_l; j++) {
            if (str[i + j] != substr[j]) {
                prss(substr, i);

                if (j == 0) { j++; }//if first letter

                i += j - shift[j-1];
                j = shift[j-1];
                break;
            }
        }
        if (j == substr_l) return i;
    }
    return -1;
}

int main () {
    cout << kmp_search ("abcbbabaababac", "abac") << std::endl;
    cout << kmp_search ("abcbbabaababac", "ab") << std::endl;
    cout << kmp_search ("abcbbabaababac", "a") << std::endl;
    cout << kmp_search ("abcbbabaababak", "k") << std::endl;
    cout << kmp_search ("aababac", "abab") << std::endl;
    //cout << kmp_search ("abcbbabaababac", "abab") << std::endl;
}
