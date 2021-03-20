import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		String b = sc.nextLine();
		int sum=0; int oca=0;
		sc.close();
		
		for (int i=1; i <= a; i++) {
			for (int p=0; p<b.length(); p++) {
				if (b.charAt(p)=='O') {
					oca++;
				    sum += oca; 
				} else { 
					oca = 0;
				}
			}
			System.out.println(sum);
		}
	}
}