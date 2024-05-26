/*
循环队列：
用（Q.rear + 1）% MaxSize = Q.front判断队列满

初始化、判空、入队、出队
*/
#include <stdio.h>

#define MaxSize 6
typedef int ElemType;

typedef struct
{
	ElemType data[MaxSize];
	int front, rear;
}SqQueue;

void InitQueue(SqQueue &q)
{
	q.front = q.rear = 0;
}

bool IsEmpty(SqQueue q)
{
	return q.front == q.rear;
}

bool EnQueue(SqQueue &q, ElemType x)
{
	if((q.rear+1)%MaxSize==q.front)
	{
		return false;
	}
	q.data[q.rear] = x;
	q.rear = (q.rear+1)%MaxSize;
	return true;
}

bool DeQueue(SqQueue &q, ElemType &x)
{
	if(IsEmpty(q))
	{
		return false;
	}
	x = q.data[q.front];
	q.front = (q.front+1) % MaxSize;
	return true;
}

int main(int argc, char const *argv[])
{
	SqQueue q;
	InitQueue(q);
	bool res;
	res = IsEmpty(q);
	if(res)
	{
		printf("the queue is empty.\n");
	}else{
		printf("the queue isn't empty.\n");
	}
	EnQueue(q, 3);
	EnQueue(q, 4);
	EnQueue(q, 5);
	res = EnQueue(q, 6);
	res = EnQueue(q, 7);
	res = EnQueue(q, 8);
	if(res)
	{
		printf("EnQueue is successful.\n");
	}else{
		printf("EnQueue failed.\n");
	}
	ElemType elem;
	res = DeQueue(q, elem);
	if(res)
	{
		printf("DeQueue elem is %d\n", elem);
	}else{
		printf("DeQueue failed.\n");
	}
	res = EnQueue(q, 8);
	if(res)
	{
		printf("EnQueue is successful.\n");
	}else{
		printf("EnQueue failed.\n");
	}
	return 0;
}
