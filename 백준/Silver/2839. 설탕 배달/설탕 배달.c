#include<stdio.h>
#pragma warning(disable:4996)

int main()
{
	int a;
	int min = 2000;

	scanf("%d", &a);
	if (a == 4)
	{
		printf("-1");
		return 0;
	}
	if (a % 5 == 0)
	{
		printf("%d", a/5);
		return 0;
	}
	for (int i = 5; i <= a; i+=5)
	{
		if ((a - i) % 3 == 0)
			if (min > i / 5 + (a - i) / 3)
				min = i / 5 + (a - i) / 3;
	}
	if (min != 2000)
	{
		printf("%d", min);
		return 0;
	}
	if ((a % 3) == 0)
	{
		printf("%d", a / 3);
		return 0;
	}

	printf("-1");
	return 0;
}