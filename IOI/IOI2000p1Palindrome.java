package javastuff;
import java.util.*;
import java.lang.Math;
public class IOI2000p1Palindrome {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args){
		int n = sc.nextInt();sc.nextLine();
		String word = sc.nextLine();
		int[][] dp = new int[2][n+1];

		for(int x = 1; x <= n; x++){
			for(int y = 1; y <=n; y++){
				if(word.charAt(x-1) == word.charAt(n-y)){
					dp[x%2][y] = dp[(x-1)%2][y] + 1;					
				}
				else{
					dp[x%2][y] = Math.max(dp[x%2][y-1], dp[(x-1)%2][y]);
				}
			}
		}
		System.out.println(n-dp[n%2][n]);
	}
}
