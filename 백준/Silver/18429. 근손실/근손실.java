import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int N = sc.nextInt();
	static int K = sc.nextInt();
	static int count = 0;

	static int m[] = new int[N];
	static boolean v[] = new boolean[N];
	static boolean isok[] = new boolean[N];

	public static void healthy(int day, boolean[] isok, int w) {
		if (day == N) {
			for (int i = 0; i < N; i++) {
				if (!isok[i])
					return;
			}
			count += 1;
		}
		for (int i = 0; i < N; i++) {
			if (!v[i]) {
				v[i] = true;
				int weight = w + m[i] - K;
				if (weight >= 500)
					isok[day] = true;
				else
					isok[day] = false;
				healthy(day + 1, isok, weight);
				v[i] = false;

			}
		}
	}

	public static void main(String[] args) {
		for (int i = 0; i < N; i++) {
			m[i] = sc.nextInt();
		}
		healthy(0, isok, 500);
		System.out.println(count);
	}
}