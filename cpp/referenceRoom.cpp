#include <iostream>
#include <algorithm>
using namespace std;

struct Time {
    int start = 0;
    int end = 0;
};

bool compareTime(const Time& t1, const Time& t2) {
    if (t1.end == t2.end) return t1.start < t2.start;
    return t1.end < t2.end;
}

class RefTimes {
private:
    int size;
    int totalRefNum = 0;
    Time* refList;
public:
    RefTimes(int n) : size(n) {
        refList = new Time[n];
        getRefTimes();
    }

    void getRefTimes() {
        for (int i = 0; i < size; i++) {
            Time t;
            cin >> t.start >> t.end;
            refList[i] = t;
        }
    }

    void sortRefTimes() {
        sort(refList, refList + size, compareTime);
    }

    void countCanRefTimes() {
        int prevEnd = 0;
        for (int i = 0; i < size; i++) {
            if (prevEnd <= refList[i].start) {
                totalRefNum++;
                prevEnd = refList[i].end;
            }
        }
    }

    void processing() {
        sortRefTimes();
        countCanRefTimes();
    }

    int getTotalRefNum() {
        return totalRefNum;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n; cin >> n;
    RefTimes r(n);
    r.processing();
    cout << r.getTotalRefNum();
    return 0;
}