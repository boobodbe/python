// oj19题：http://oj.lgwenda.com/problem/19
#include <stdio.h>

#define MaxSize 5

typedef struct
{
	int data[50];
	int top;
}Stack;

void InitStack(Stack &s)
{
	s.top = -1;
}

typedef struct 
{
	int data[5];
	int front, rear;
}Queue;

void EnStack(Stack &s, int x)
{
	if(s.top==49){
		return;
	}
	s.data[++s.top] = x;
}

void DeStack(Stack &s, int &elem)
{
	if(s.top == -1)
	{
		return;
	}
	elem = s.data[s.top--];
}

void InitQueue(Queue &q)
{
	q.front = q.rear = 0;
}

bool EnQueue(Queue &q, int x)
{
	if((q.rear+1)%MaxSize==q.front)
	{
		return false;
	}
	q.data[q.rear] = x;
	q.rear = (q.rear+1) % MaxSize;
	return true;
}

bool DeQueue(Queue &q, int &x)
{
	if(q.rear == q.front)
	{
		return false;
	}
	x = q.data[q.front];
	q.front = (q.front+1) % MaxSize;
	return true;
}

int main()
{
	Stack s;
	InitStack(s);
	int x;
	for(int i = 0; i<3; i++)
	{
		scanf("%d", &x);
		EnStack(s, x);
	}
	int elem;
	for(int i = 0; i<3; i++)
	{
		DeStack(s, elem);
		printf("%2d", elem);
	}
	printf("\n");
	Queue q;
	InitQueue(q);
	bool ret;
	for(int i = 0; i < MaxSize; i++)
	{
		scanf("%d", &elem);
		ret = EnQueue(q, elem);
		if(not ret)
		{
			printf("false\n");
			break;
		}
	}
	bool flag = true;
	while(flag)
	{
		flag = DeQueue(q, elem);
		if(flag)
		{
			printf("%2d", elem);
		}
	}
	printf("\n");
	return 0;
}