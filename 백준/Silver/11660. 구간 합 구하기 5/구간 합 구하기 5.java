import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int map[][] = new int[N + 1][N + 1];
		int sum[][] = new int[N + 1][N + 1];
		for (int i = 1; i < N + 1; i++) {
			for (int j = 1; j < N + 1; j++) {
				map[i][j] = sc.nextInt();
				sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + map[i][j];
			}
		}
		for (int i = 0; i < M; i++) {
			int startR = sc.nextInt();
			int startC = sc.nextInt();
			int endR = sc.nextInt();
			int endC = sc.nextInt();
			System.out.println(
					sum[endR][endC] - sum[endR][startC - 1] - sum[startR - 1][endC] + sum[startR - 1][startC - 1]);
		}

	}

}