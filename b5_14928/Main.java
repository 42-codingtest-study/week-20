package b5_14928;
import java.math.BigInteger;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		BigInteger N = s.nextBigInteger();
		System.out.print(N.mod(20000303));
	}

}

