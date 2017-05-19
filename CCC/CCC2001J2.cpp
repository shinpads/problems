/*
 * CCC2001J2.cpp
 *
 *  Created on: May 19, 2017
 *      Author: Rob
 */




#include<iostream>
#include<cmath>
using namespace std;
int main(){
	int  n,x, m;
	n = 1;
	scanf("%i%i",&x,&m);
	while(n<=m){
		if(n*x % m == 1){
			break;
		}
		n++;
	}
	if(n < m){
		printf("%i",n);
	}else{
		printf("No such integer exists.");
	}
	return 0;
}
