#include<iostream>
#include<algorithm>
using namespace std;
int y[100001];
int x[100001];
void docase() {
	int n;
	scanf("%i", &n);
	for (int i = 0; i < n; i++) {
		scanf("%i", &x[i]);
	}
	for (int i = 0; i < n; i++) {
		scanf("%i", &y[i]);
	}
	int i = n - 1;
	int j = n - 1;

	int ans = 0;
	while (i >= 0 && j >= 0) {

		while (y[j] < x[i]) {
			j--;
		}
		ans = max(j - i, ans);

		i--;
	}
	printf("%i", ans);

}
int main() {
	int t;
	scanf("%i", &t);
	for (int i = 0; i < t; i++) {
		docase();
	}
	return 0;
}