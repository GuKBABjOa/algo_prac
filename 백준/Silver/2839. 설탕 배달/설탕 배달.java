import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		int min = 2000;

		if (a == 4) {
			System.out.println(-1);
			return;
		}
		if (a % 5 == 0) {
			System.out.println(a / 5);
			return;
		}
		for (int i = 5; i <= a; i += 5) {
			if ((a - i) % 3 == 0)
				if (min > i / 5 + (a - i) / 3)
					min = i / 5 + (a - i) / 3;
		}
		if (min != 2000) {
			System.out.println(min);
			return;
		}
		if ((a % 3) == 0) {
			System.out.println(a / 3);
			return;
		}

		System.out.println(-1);
	}

}