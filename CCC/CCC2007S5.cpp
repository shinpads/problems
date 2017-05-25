/*
 * CCC2007S5.cpp
 *
 *  Created on: May 25, 2017
 *      Author: Rob
 */

/*
 * > create svals to store sum of last w pins
 * > the answer to the subproblem for pins up to n, after k bowls is the maximum of either
 * 	   a) the answer up to pins n-1 for bowls k
 * 	   b) the sum of the last w pins plus the answer for pins up to n-w after throws k-1
 *
 */


#include<iostream>
#include<algorithm>
using namespace std;
int n,k,w,c,t;
int vals[30001] = {0};
int svals[30001] = {0};
int dp[30001][501];
int main(){
	for(int i =0; i<=30000; i++){
		dp[i][0] = 0;
	}
	scanf("%d",&t);
	for(int testcase = 0; testcase < t; testcase ++){
		//get and store input
		scanf("%d%d%d",&n,&k,&w);
		scanf("%d",&vals[0]);
		svals[0] = vals[0];
		for(int i = 1; i<w; i++){
			scanf("%d",&vals[i]);
			svals[i] = vals[i] + svals[i-1];
		}
		for(int i = w; i<n; i++){
			scanf("%d",&vals[i]);
			svals[i] =vals[i] + svals[i-1] - vals[i-w];
		}
		for(int x = 1; x<=k; x++){
			for(int y = 0; y<n; y++){
				if(y-w >= 0){
				dp[y][x] = max(dp[y-1][x],svals[y] + dp[y-w][x-1]);
				}else{
					dp[y][x] = svals[y];
				}
			}
		}
		printf("%d\n",dp[n-1][k]);
	}
	return 0;
}

