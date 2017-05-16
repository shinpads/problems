package javastuff;

import java.util.Scanner;

public class CCC2008S5 {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args){
		boolean[][][][] dp = new boolean[31][31][31][31];
		int[][] poss =  {{2, 1, 0, 2}, {1, 1, 1, 1}, {0, 0, 2, 1}, {0, 3, 0, 0}, {1, 0, 0, 1}};
		for(int e = 0; e<=30; e++){
			for(int f = 0; f<=30; f++){
				for(int g = 0; g<=30; g++){
					for(int h= 0; h<=30; h++){
						for(int[] m : poss){
							if (e >= m[0] && f>= m[1] && g>=m[2] && h>=m[3]){
								if(!dp[e-m[0]][f-m[1]][g-m[2]][h-m[3]]){
									dp[e][f][g][h] = true;
								}								
							}
						}
					}
				}
			}
		}
		int n = sc.nextInt();
		for(int i = 0; i <n; i++){
			int a,b,c,d;
			a = sc.nextInt(); b = sc.nextInt(); c = sc.nextInt(); d = sc.nextInt();
			if(dp[a][b][c][d]){
				System.out.println("Patrick");
			}else{
				System.out.println("Roland");
			}

					
		}
	}
}
