import java.util.*;
public class P2LOL {
	static Scanner sc = new Scanner(System.in);
	public static void main(String[] args){
		int n = sc.nextInt();
		int minx = -1000;
		int maxx = 1000;
		int miny = -1000;
		int maxy = 1000;
		for(int i = 0; i < n; i++){
			int a = sc.nextInt();
			int b = sc.nextInt();
			minx = Math.max(minx,a);
			maxx = Math.min(maxx,a);
			miny = Math.max(miny,b);
			maxy = Math.min(maxy,b);
			
		}
		System.out.println((maxx-minx)*(maxy-miny));
	}
}
