/*
 * DMPG2015B4.cpp
 *
 *  Created on: May 27, 2017
 *      Author: Rob
 */

#include<iostream>
#include<list>
#include<algorithm>
#define pb push_back
using namespace std;
int n,ans;
list<int> pos;
list<int> neg;
bool zero = false;
int main(){
	scanf("%d",&n);
	for(int i = 0; i<n; i++){
		int a;
		scanf("%d",&a);
		if(a>0){
			pos.pb(a);
		}
		else if(a<0){
			neg.pb(a);
		}
		if(a == 0){
			zero = true;
		}
	}
	neg.sort();
	ans = 1;
	for(int x: pos){
		ans *= x;
	}
	if(neg.size()%2 == 1 && (pos.size() > 0 || neg.size() > 1)){
		neg.pop_back();
	}
	for(int x: neg){
		ans*=x;
	}
	if(neg.size() == 0 && pos.size() == 0){
		ans = 0;
	}
	if(ans < 0 && zero){
		ans = 0;
	}
	printf("%d",ans);

	return 0;
}



