import java.util.Scanner;

public class Main {
//	(int) (r-Math.pow(2, N-1))
	static int count = 0;

	public static void findRC(int N, int r, int c) {
		if (N == 1) {
			if (r == 0 && c == 0)
				return;
			else if (r == 0 && c == 1) {
				count += 1;
				return;
			} else if (r == 1 && c == 0) {
				count += 2;
				return;
			} else if (r == 1 && c == 1) {
				count += 3;
				return;
			}

		}
		int mp = (int) (Math.pow(2, N - 1));
		if (r < mp && c < mp)// 1번 위치
		{
			findRC(N - 1, r, c);
		} else if (r < mp && c >= mp)// 2번 위치
		{
			count += mp * mp;
			findRC(N - 1, r, c - mp);
		} else if (r >= mp && c < mp)// 3번 위치
		{
			count += mp * mp * 2;
			findRC(N - 1, r - mp, c);
		} else // 4번 위치
		{
			count += mp * mp * 3;
			findRC(N - 1, r - mp, c - mp);
		}

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int r = sc.nextInt();
		int c = sc.nextInt();

		findRC(N, r, c);
		System.out.println(count);
	}

}