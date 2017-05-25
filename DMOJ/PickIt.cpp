/*
 * PickIt.cpp
 *
 *  Created on: May 24, 2017
 *      Author: Rob
 */

#include<iostream>
#include<algorithm>

using namespace std;
int vals[201];
int n;
int dp[201][201];
int findmax(int a, int b){
	if(b<=a){
		return 0;
	}
	if(dp[a][b]!=-1){
		return dp[a][b];
	}
	if(b-a == 2){
		return vals[a]+vals[b]+vals[a+1];
	}
	dp[a][b] = 0;
	for(int cut = a+1; cut<b; cut++){
		dp[a][b] = max(dp[a][b],findmax(a,cut)+findmax(cut,b)+vals[a]+vals[cut]+vals[b]);
	}
	//printf("%d %d %d\n",a,b,dp[a][b]);
	return dp[a][b];
}
int main(){
	scanf("%d",&n);
	while(n!= 0){
  	for(int i =0; i<n; i++){
  		scanf("%d",&vals[i]);
  	}
  	for(int x = 0; x<= 200; x++){
  		for(int y = 0; y<= 200; y++){
  			dp[x][y] = -1;
  		}
  	}
  	printf("%d\n",findmax(0,n-1));
  	scanf("%d",&n);
	}
	return 0;
}


