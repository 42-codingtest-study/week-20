package b5_1032;
import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		
		int N = s.nextInt();
		String[] arr = new String[N];

		for(int i = 0; i < N; i++) {
			String str = s.next();
			for(int j = 0; j < str.length(); j++) {
				arr[i] = str;
			}			
		}
		for(int i = 0; i < arr[0].length(); i++) {
			char c = arr[0].charAt(i);
			for(int j= 1; j < N; j++) {
				
				if(arr[j].charAt(i) != c) {
					c = '?';
					break;
				}
			}
			System.out.print(c);
		}
	}

}
