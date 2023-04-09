package b5_4999;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		String a = s.next();
		String b = s.next();
		if(a.length() >= b.length())
			System.out.print("go");
		else
			System.out.print("no");
	}

}
