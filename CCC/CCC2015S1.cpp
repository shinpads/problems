#include<iostream>
#include<list>
using namespace std;
list<int> nums;
int n, total, c;
int main(){
  scanf("%d",&n);
  for(int i = 0; i<n; i++){
    scanf("%d",&c);
    if(c== 0){
      total-= nums.front();
      nums.pop_front();
    }else{
      nums.push_front(c);
      total+=c;
    }
  }
  printf("%d",total);
  return 0;
