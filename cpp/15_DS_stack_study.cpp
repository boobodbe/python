#include <stdio.h>
#include <stdlib.h>

#define MaxSize 50
typedef int ElemType;

typedef struct
{
	ElemType data[MaxSize];
	int top;  // 指向栈顶
}SqStack;

void InitStack(SqStack &s)
{
	s.top = -1;
}

bool StackEmpty(SqStack s)
{
	if(s.top == -1)
	{
		return true;
	}
	return false;
}

bool push(SqStack &s, ElemType x)
{
	if(s.top == MaxSize-1)
	{
		return false;
	}
	s.data[++s.top] = x;
	return true;
}

bool GetTop(SqStack s, ElemType &m)
{
	if(StackEmpty(s))
	{
		return false;
	}
	m = s.data[s.top];
	return true;
}

bool pop(SqStack &s, ElemType &m)
{
	if(StackEmpty(s))
	{
		return false;
	}
	m = s.data[s.top--];
	return true;
}

void print_stack(SqStack s)
{
	if(StackEmpty(s))
	{
		return;
	}
	for(int i = 0; i <= s.top; i++)
	{
		printf("%d\t", s.data[i]);
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{
	printf("stack study!\n");
	SqStack s;
	InitStack(s);
	bool flag;
	flag = StackEmpty(s);
	if(flag)
	{
		printf("栈是空的。\n");
	}
	push(s, 3);
	push(s, 4);
	push(s, 5);
	print_stack(s);
	ElemType m;
	flag = GetTop(s, m);
	if(flag)
	{
		printf("get top %d\n", m);
	}
	flag = pop(s, m);
	if(flag)
	{
		printf("弹出元素为：%d\n", m);
	}
	print_stack(s);
	return 0;
}