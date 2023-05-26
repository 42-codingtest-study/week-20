package b5_25372;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		int N = s.nextInt();
		for(int i = 0; i < N; i++) {
			String str = s.next();
			if(str.length() >=6 && str.length() <=9)
				System.out.print("yes");
			else
				System.out.print("no");
		}
	}

}
