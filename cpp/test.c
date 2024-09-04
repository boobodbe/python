// 随手写的测试代码
#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>

int findSingleNum(int arr[], int n);
int DaysOfMonth[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
bool isLeapYear(int year);
int distance(int year1, int year2, int month1, int month2, int day1, int day2);
int weekday(int year, int month, int day);
int interestRate(void);
int randomCard(void);
bool isPrime(int n);
long long fib(int n);
void hanoi(int n);
void hanoi_helper(int n, char start, char middle, char target);

int main(void)
{
	printf("hello world.\n");

	// 测试输入利率输出金额的interestRate函数
	// interestRate();

	// 测试随机发牌程序
	// randomCard();

	// 测试判断素数程序
	// int test_num;

	// do
	// {
	// 	printf("Enter a number: ");
	// 	scanf("%d", &test_num);
	// 	if(isPrime(test_num)){
	// 		printf("%d is a prime number.\n", test_num);
	// 	}else{
	// 		printf("%d is not a prime number.\n", test_num);
	// 	}
	// }while(test_num);

	// 测试斐波那契数列
	int n;
	printf("Enter a number: ");
	scanf("%d", &n);
	// printf("%d ---> fib ---> %d\n", n, fib(n));

	// 测试汉诺塔问题
	hanoi(n);

	return 0;
}

void hanoi_helper(int n, char start, char middle, char target){
	// 边界条件
	if(n == 1){
	    printf("%c --> %c\n", start, target);
	    return;
	}
	// n == 1
	// 递归公式
	// 1. 将上面n-1个盘子从A移动到B
	hanoi_helper(n-1, start, target, middle);
	// 2. 将第n个盘子从A移动到C
	printf("%c --> %c\n", start, target);
	// 3. 将n-1个盘子从B移动到C
	hanoi_helper(n-1, middle, start, target);
}

void hanoi(int n)
{
	// 汉诺塔问题

	// S(1) = 1
	// S(n) = 2 * S(n-1) + 1
	// S(n) + 1 = 2 *S(n-1) + 2 = ... = 2^n
	// S(n) = 2^n - 1
	long long steps = (1 << n) - 1;
	printf("The number of steps is %lld\n", steps);
	hanoi_helper(n, 'A', 'B', 'C');
}

bool isPrime(int n)
{
	// 判断一个数是否为素数
	for(int i = 2; i * i <= n; i++)
	{
		if(n % i == 0)
		{
			return false;
		}
	}
	return true;
}

int randomCard(void)
{
	// 用户指定发牌的张数，随机发牌，未完成！！！
	int cards;
	printf("Enter number of card: ");
	scanf("%d", &cards);

	const char suits[4] = {'s', 'h', 'c', 'd'};
	const char ranks[13] = {'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'};
	bool in_hand[4][13] = {false};

	// 设置随机种子（只需要设置一次)
	srand(time(NULL));

	printf("Your hand: ");
	while(cards)
	{
		int i = rand() % 4;
		int j = rand() % 13;

		if(!in_hand[i][j])
		{
			in_hand[i][j] = true;
			cards--;
			printf("%c%c  ", ranks[j], suits[i]);
		}
	}
	printf("\n");

	return 0;
}

int interestRate(void)
{
	// 用户输入初始金额，利率和投资年数，程序打印一张表格，表格将小时输入的利率以及紧随其后4个更高利率的总金额
	double init_balance, rate;
	int years;

	printf("Enter initial balance: ");
	scanf("%lf", &init_balance);

	printf("Enter interest rate: ");
	scanf("%lf", &rate);

	printf("Enter number of years: ");
	scanf("%d", &years);

	// 输出第一行
	printf("\nYears");
	for(int i = 0; i < 5; i++)
	{
		printf("%5.0lf%%", rate + i);
	}
	printf("\n");

	// 输出之后的数据行
	double value[5];
	for (int i = 0; i < 5; i++)
	{
		value[i] = init_balance;
	}

	for(int y = 1; y <= years; y++)
	{
		printf("%3d ", y);
		for (int i = 0; i < 5; i++)
		{
			value[i] += value[i] * (rate + i) / 100;
			printf("%7.2lf", value[i]);
		}
		printf("\n");
	}

	return 0;
}

int weekday(int year, int month, int day)
{
	// 一直1970年1月1日星期四，算之后某一天星期几
	int days = distance(1970, 1, 1, year, month, day);
	return (4+days) % 7;
}

void temperature()
{
	// 华氏温度转摄氏温度
	float fahrenheit = 213.0f;
	//printf("Enter Fahrenheit temperature: ");
	//scanf("%f", &fahrenheit);

	float celsius = 5.0 / 9.0 * (fahrenheit - 32.0);
	printf("celsius is %.2f.\n", celsius);
}

void setFebDays(int year){
	// 设置2月份的天数
	if (isLeapYear(year))
	{
		DaysOfMonth[2] = 29;
	}else{
		DaysOfMonth[2] = 28;
	}
}

void theLengthOfMessage()
{
	// 编写一个程序来计算消息的长度：用户输入消息后，程序显示消息的长度。


	printf("Enter a message: ");

	int length = 0;
	while(getchar() != '\n')
	{
		length++;
	}

	printf("Your message was %d character(s) long.", length);
}

void mi()
{
	// 如何判断一个整数是否为2的幂次
	int num;
	scanf("%d", &num);
	if (num % 2 == 0)
	{
		printf("%d is odds.\n", num);
	}else{
		printf("%d is not odds.\n", num);
	}
}

void changeTwoNum()
{
	// 原地交换两个数
	int i = 3, j = 4;
	// scanf("%d %d", &i, &j);
	i = i ^ j;
	j = i ^ j;
	i = i ^ j;
	printf("i = %d, j = %d\n", i, j);
}

void digitsOfNum()
{
	// 算一个数字是几位数
	int num;
	printf("Enter an integer: ");
	scanf("%d", &num);

	int tag = 0;
	do
	{
		tag++;
		num /= 10;
	} while (num != 0);

	printf("The number has %d digit(s).\n", tag);
}

void squared()
{
	// 算一个数的平方
	int n;

	while (1)
	{
		printf("Enter a number (enter 0 to stop): ");
		scanf("%d", &n);

		if (n == 0)
		{
			break;
		}

		printf("%d squared is %d\n", n, n * n);
	}
}

void grade()
{
	// 判断一个数的等级，switch case练习
	int grade;
	scanf("%d", &grade);

	// 参数校验
	if (grade < 0 || grade > 100)
	{
		printf("Illegal arguments: %d\n", grade);
	}
	else
	{
		switch (grade / 10)
		{
		case 10: case 9:
			printf("A\n");
			break;
		case 8:
			printf("B\n");
			break;
		case 7:
			printf("C\n");
			break;
		case 6:
			printf("D\n");
			break;
		default:
			printf("F\n");
			break;
		}
	}
}

bool isLeapYear(int year)
{
	// 判断闰年

	//int year;
	/*
	scanf("%d", &year);
	run = (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) ? 1 : 0;
	if(run)
	{
		printf("%d是闰年\n", year);
	}else{
		printf("%d不是闰年\n", year);
	}
	*/
	// printf("输入一个年份来判断是不是闰年（输入0退出）： ");
	// while(scanf("%d", &year)){
	// 	if(year ==0 )
	// 	{
	// 		break;
	// 	}
	// 	printf("%d --> %s\n", year, (year % 4 == 0 && year % 100 != 0) || year % 400 == 0 ? "是闰年" : "不是闰年");
	// 	printf("输入一个年份来判断是不是闰年（输入0退出）： ");
	// }
	return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}

long long fib(int n)
{
	// 斐波那契数列
	if (n == 0 || n == 1) return n;

	// return fib(n - 1) + fib(n - 2);
	long long a = 0, b = 1;
	for(int i = 2; i <= n; i++)
	{
		long long temp = a + b;
		a = b;
		b = temp;
	}
	return b;
}

int checkbook(void)
{
	// 记账程序
	printf("*** checkbook-balancing program ***\n");
	printf("Commands: 0=clear, 1=credit, 2=debit, 3=balance, 4=exit\n\n");
	int command;
	double balance = 0.0, credit = 0.0, debit = 0.0;

	while(1)
	{
		printf("Enter command: ");
		scanf("%d", &command);
		switch (command)
		{
		case 0:
			balance = 0.0;
			break;
		case 1:
			printf("Enter amount of credit: ");
			scanf("%lf", &credit);
			balance += credit;
			break;
		case 2:
			printf("Enter amount of debit: ");
			scanf("%lf", &debit);
			balance -= debit;
			break;
		case 3:
			printf("Current balance: $%.2lf\n", balance);
			break;
		case 4:
			return 0;
		default:
			printf("Commands: 0=clear, 1=credit, 2=debit, 3=balance, 4=exit\n\n");
			break;
		}
	}
}

void theNextDay(int year, int month, int day)
{
	// 输入一天的年月日，算下一天的日期
	// int year, month, day;
	// scanf("%d%d%d", &year, &month, &day);

	setFebDays(year);

	day++;
	if (day > DaysOfMonth[month]){
		day = 1;
		month++;
	}
	if (month > 12)
	{
		month = 1;
		year++;
	}

	printf("下一天是 --> %d 年 %d 月 %d 日。\n", year, month, day);


	int year1, month1, day1, year2, month2, day2, data;
	scanf("%d%d%d%d%d%d", &year1, &month1, &day1, &year2, &month2, &day2);
	data = distance(year1, year2, month1, month2, day1, day2);
	printf("两个日期相差 %d 天。\n", data);
}

int findSingleNum(int arr[], int n)
{
	/*找到一列数中单独的那一个*/
	int ret = 0;
	for(int i = 0; i < n; i++)
	{
		ret ^= arr[i];
	}
	return ret;
}

int distance(int year1, int month1, int day1, int year2, int month2, int day2){
	/*计算两个日期之间相差多少天*/
	// 计算year1还剩多少天
	int days;
	setFebDays(year1);
	days = DaysOfMonth[month1] - day1;

	for(int m = month1 + 1; m <= 12; m++){
		days += DaysOfMonth[m];
	}
	// 计算中间年份的天数
	for(int y = year1 + 1; y < year2; y++)
	{
		days += 365;
		if(isLeapYear(y)){
			days++;
		}
	}
	// 计算year2过了多少天
	setFebDays(year2);
	for (int m = 1; m < month2; m++){
		days += DaysOfMonth[m];
	}
	days += day2;

	// 如果year1 == year2， 则多算了一整年
	if(year1 == year2)
	{
		days -= 365;
		if (isLeapYear(year2))
		{
			days--;
		}
	}

	return days;
}