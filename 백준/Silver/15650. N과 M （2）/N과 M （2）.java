import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int N = sc.nextInt();
	static int M = sc.nextInt();
	static int ans[] = new int[N];

	public static void NandM(int count, int start) {
		if (count == M) {
			for (int i = 0; i < M; i++) {
				System.out.print(ans[i] + " ");
			}
			System.out.println();

		} else {
			for (int i = start; i < N; i++) {

				ans[count] = i + 1;
				NandM(count + 1, i + 1);
			}
		}
	}

	public static void main(String[] args) {

		NandM(0, 0);

	}

}