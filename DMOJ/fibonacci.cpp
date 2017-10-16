#include<iostream>
#define MOD 1000000007
using namespace std;


void mulMatrix(unsigned long long int m[2][2], unsigned long long int n[2][2]){
	unsigned long long int a,b,c,d;
	a = (m[0][0] * n[0][0])%MOD + (m[0][1]*n[1][0])%MOD; 
	b = (m[0][0] * n[0][1])%MOD + (m[0][1]*n[1][1])%MOD; 
	c = (m[1][0] * n[0][0])%MOD + (m[1][1]*n[0][1])%MOD; 
	d = (m[1][0] * n[0][1])%MOD + (m[1][1]*n[1][1])%MOD; 
	m[0][0] = a%MOD;
	m[0][1] = b%MOD;
	m[1][0] = c%MOD;
	m[1][1] = d%MOD;
}


int main(){
	unsigned long long int n;
	unsigned long long int result[2][2] = {{1,0},{0,1}};
	unsigned long long int fibo[2][2] = {{1,1},{1,0}};
	scanf("%llu",&n);
	while(n > 0){
		if(n%2 == 1){
			mulMatrix(result,fibo);
		}
		n = n/2;
		mulMatrix(fibo,fibo);
	}
	printf("%llu\n",result[1][0]%MOD);
	return 0;
}