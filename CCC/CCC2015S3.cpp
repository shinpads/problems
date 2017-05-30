#include<iostream>
#include<string>
using namespace std;
int j,a;
int jers[1000001];
int main(){
  scanf("%d%d\new",&j,&a);
  int ans = 0;
  int jn;
  int js;
  char je;
  for(int i =1; i<=j; i++){
    scanf("%c\n",&je);
    //printf("%c\n",je);
    if(je == 'S'){jers[i] = 0;}
    if(je == 'M'){jers[i] = 1;}
    if(je == 'L'){jers[i] = 2;}
  }
  for(int i = 0; i<a; i++){
    scanf(" %c%d",&je,&jn);
    //printf("%c %d\n",je,jn);
    if(je == 'S'){js = 0;}
    else if(je == 'M'){js = 1;}
    else{js = 2;}
    if(jers[jn] >= js){
      ans++;
      jers[jn] = -1;
    }
  }
  printf("%d",ans);
  return 0;
}
