package javastuff;
import java.util.*;
public class ECOO3 {

   public static void main(String[] args){
       Scanner s = new Scanner(System.in);
       for (int i = 0; i < 10; i++) {
           int numMountains = s.nextInt();
           int[] heights = new int[numMountains];
           for (int j = 0; j < numMountains; j++) {
               heights[j] = s.nextInt();
           }
           int[] scores = new int[numMountains];
          
           for (int x = 0; x < numMountains; x++) {
               int yI = heights[x];
               int xI = x;
               //Left
               double mLast = Double.POSITIVE_INFINITY;
               for (int j = xI-1; j >= 0; j--) {
                   int yT = heights[j];
                   int xT = j;
                   double m = (double)(yT-yI)/(xT-xI);
                   if(m<mLast){
                       mLast = m;
                       scores[x]++;
                   }
               }
               //Right
               mLast = Double.NEGATIVE_INFINITY;
               for (int j = xI+1; j < numMountains; j++) {
                   int yT = heights[j];
                   int xT = j;
                   double m = (double)(yT-yI)/(xT-xI);
                   if(m>mLast){
                       mLast = m;
                       scores[x]++;
                   }
               }
           }
          
           int maxScore = 0;
           int maxPosition = 0;
           for (int j = 0; j < numMountains; j++) {
               if(scores[j]>maxScore){
                   maxScore = scores[j];
                   maxPosition = j;
               }
           }
           System.out.println(maxPosition+1);
       }
   }
  
}