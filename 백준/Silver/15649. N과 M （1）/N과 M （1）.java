import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int N = sc.nextInt();
	static int M = sc.nextInt();
	static int ans[] = new int [N];
	static boolean[] v = new boolean[N];
	public static void NandM (int count) {
		if(count == M) {
			for(int i = 0; i<M;i++)
			{
				System.out.print(ans[i] + " ");
			}
			System.out.println();
			
		}else {
			for(int i = 0;i<N;i++)
			{
				if(!v[i]) { 
					ans[count] = i + 1;
					v[i] = true;
					NandM(count + 1);
					v[i] = false;
				}
			
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		NandM(0);
		
	}

}