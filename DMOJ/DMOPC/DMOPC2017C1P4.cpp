#include<iostream>
#include<algorithm>
using namespace std;
long long int dp[2][5001][2] = {0};
long long int gold[5001][2] = {0};-
long long int tim[5001][2] = {0};
int main(){
	int n,h;
	scanf("%d%d",&n,&h);
	for(int i = 1; i<=n; i++){
		scanf("%lld%lld%lld%lld",&gold[i][0],&tim[i][0],&gold[i][1],&tim[i][1]);
	}
	for(int npc = 1; npc<=n; npc++){
		for(int t =1 ; t<=h; t++){
			if(t >= tim[npc][0])
				dp[npc%2][t][0] = dp[npc%2][t-tim[npc][0]][1] +gold[npc][0];
			dp[npc%2][t][0] = max(dp[npc%2][t][0], dp[(npc-1)%2][t][0]);

			if(t >= tim[npc][1])
				dp[npc%2][t][1] = dp[npc%2][t-tim[npc][1]][1] + gold[npc][1];
			dp[npc%2][t][1] = max(dp[npc%2][t][1], dp[(npc-1)%2][t][0]);

		}
	}
	printf("%lld\n", dp[n%2][h][0]);		

	return 0;
}
