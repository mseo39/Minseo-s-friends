import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		sc.close();
		
		for (int i=1; i<=a; i++) {
			for (int p=1; p<=i; p++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}