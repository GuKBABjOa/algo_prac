import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int index;

		int N = sc.nextInt();
		boolean ans[] = new boolean[N + 1];
		int X = sc.nextInt();
		ans[X] = true;
		index = X;
		int K = sc.nextInt();
		for (int k = 1; k <= K; k++) {
			int A = sc.nextInt();
			int B = sc.nextInt();
			if (ans[A] == true) {
				ans[B] = true;
				ans[A] = false;
				index = B;
			} else if (ans[B] == true) {
				ans[A] = true;
				ans[B] = false;
				index = A;
			} else
				continue;
		}
		System.out.println(index);

	}

}