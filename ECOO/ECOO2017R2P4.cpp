/*
 * ECOO2017R2P4.cpp
 *
 *  Created on: May 28, 2017
 *      Author: Rob
 */


#include<iostream>
using namespace std;
int MOD = 1000000007;
long long int dp[2][10002];
void solve(int u){
	dp[1][1] = 1;
	for(int n = 2; n<=u; n++){
		for(int x = 1; x<=n; x++){
			if(n%2 == 1){
				if(n-1 < x){
					continue;
				}
				else{
				dp[n%2][x] = ((dp[(n-1)%2][n] - dp[(n-1)%2][x-1]) + dp[n%2][x-1])%MOD;
				if(dp[n%2][x] <0){
				  dp[n%2][x] += MOD;
				}
				}
			}
			else{
				dp[n%2][x] = (dp[(n-1)%2][x-1] + dp[n%2][x-1])%MOD;
			}
			dp[n%2][x+1] = dp[n%2][x];
		}
	}
}
int main(){

	int x;
	for(int t = 0; t<10; t++){
		scanf("%d",&x);
		solve(x);
		printf("%lld\n",dp[x%2][x]%MOD);
	}
	return 0;
}
