import java.util.*;

public class iscool{
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
String vowels = "aeiou";
String cons = "bcdfghjklmnpqrstvwxyz";
String al = "abcdefghijklmnopqrstuvwxyz";
int dist = 1000000;
int position =0;
char currentVowel = 0;
String text = sc.nextLine();
String word = "";

for(int i = 0; i<text.length(); i++){
    word+=text.charAt(i);
    char cL = text.charAt(i);

    for(int h = 0; h<al.length(); h++){
        if(al.charAt(h)==cL){
            position=h;
        }

    }
    //check for vowel

        if(cL != 'a' && cL !='e' && cL != 'i' && cL != 'o' && cL != 'u'){
            dist=10000000;
                        for(int ii = 0; ii<vowels.length(); ii++){
                for(int y = 0; y<al.length(); y++ ){
                    if(vowels.charAt(ii)==al.charAt(y)){

                        if(Math.abs(position-y)<dist){
                        dist = Math.abs(position-y);
                        currentVowel = vowels.charAt(ii);
                        }
                                            }
                }
            }

            word+=currentVowel;
            for(int a = 0; a<cons.length(); a++){
                if(cons.charAt(a)==cL){
                    if(cons.charAt(a)!='z'){
                    word+=cons.charAt(a+1);
                    }
                    else{word+='z';}
                }
            }
        }



}
System.out.println(word);

    }

}