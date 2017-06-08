/*
 * ICPC.cpp
 *
 *  Created on: Jun 7, 2017
 *      Author: Rob
 */

/*	The answer to the entire question is the minimum sum of the minimum packs of dogs and buns
 *  for all possible amount of total dogs or buns
 *
 *  I have two recursive functions (one for dogs and one for buns) which basically do the same thing:
 *  lets use the bun function as an example
 *  Let findmin(x,y) represent minimum cases of buns for x buns starting at case #y
 *  the answer to this subproblem is then the minimum of either counting case y or not counting case y
 *  ie min(findmin(x-casex,y+1)+1,findmin(x,y+1))
 *  the recurse ends once y exceeds B or x is lessthan 0
 *  if x == 0, then you know that it is possible to make y buns and return 0
 *
 *  make sure you store all answers for each recusive function up to (100*1000)(max values) and then its
 *  just a simple for loop to find the smallest sum where both of them are possible
 *
 *
 */

#include<iostream>
#include<algorithm>
using namespace std;
int h,b;
int H[101];
int B[101];
int db[101][100001];
int dh[101][100001];
//min packs required for x buns up to yth case
int minbun(int x,int y){
	if(x == 0){return 0;}
	if(y == b || x < 0){return 999;}
	if(db[y][x] != -1){return db[y][x];}
	db[y][x] = min(minbun(x,y+1),1+minbun(x-B[y],y+1));
	return db[y][x];

}
//min packs required for x dogs up to yth case
int mindog(int x,int y){
	if(x == 0){return 0;}
	if(y == h || x < 0){return 999;}
	if(dh[y][x] != -1){return dh[y][x];}
	dh[y][x] = min(mindog(x,y+1),1+mindog(x-H[y],y+1));
	return dh[y][x];

}
int main(){
	for(int x = 0; x<=100; x++){
		for(int y = 0; y<=100000; y++){
			db[x][y] = -1;
			dh[x][y] = -1;
		}
	}
	scanf("%d",&h);
	for(int i = 0; i<h; i++){
		scanf("%d",&H[i]);
	}
	scanf("%d",&b);
	for(int i = 0; i<b; i++){
		scanf("%d",&B[i]);
	}
	int dv,bv,ans;
	ans = 999999;


	for(int i = 1; i<= 100000; i++){
		dv = mindog(i,0);
		bv = minbun(i,0);
		if(dv >0 && dv <= 100 && bv >0 && bv <= 100){
			ans = min(ans,dv+bv);
		}
	}
	if(ans <= 200){
		printf("%d",ans);
	}else{
	printf("impossible");
	}


	return 0;
}


