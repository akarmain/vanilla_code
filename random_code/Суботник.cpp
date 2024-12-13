#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n, r, c, a;
	int ans = 0;
	cin >> r >> c;
	n = r * c;

	vector<int> arr(n);
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}

	sort(arr.begin(), arr.end());

	for (int i = 0; i < n; i += c)
	{
		a = arr[i + c - 1] - arr[i];
		if (a > ans)
			ans = a;
	}
	cout << ans << endl;
	return 0;
}
