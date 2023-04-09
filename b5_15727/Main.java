package b5_15727;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int d = s.nextInt();
		if(d % 5 == 0)
			System.out.print(d/5);
		else
			System.out.print(d / 5 + 1);
		
	}

}
