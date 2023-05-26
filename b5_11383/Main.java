package b5_11383;
import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		int n = s.nextInt(), m = s.nextInt();
		String[] img = new String[n];
		for(int i = 0; i < n; i++) {
			img[i] = s.next();

		}

		for(int i = 0; i < n; i++) {
			if (s.next() == img[i]) break;
			
		}
		
	}

}
