package b5_20492;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		int N = s.nextInt();
		double a = N * 0.78, b = N*(0.8+0.2*0.78);
		System.out.printf("%d %d", (int)a, (int)b);
	}

}
