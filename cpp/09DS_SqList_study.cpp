// 顺序表的初始化及实战
#include <stdio.h>

#define MaxSize 50
typedef int ElemType;

typedef struct {
	ElemType data[MaxSize];
	int length;
}SqList;

bool ListInsert(SqList &L, int pos, ElemType element)
{
	if(pos<1 || pos>L.length+1)
	{
		return false;
	}
	if(L.length == MaxSize)
	{
		return false;
	}
	for(int j = L.length; j >= pos ; j--)
	{
		L.data[j] = L.data[j-1];
	}
	L.data[pos-1] = element;
	L.length++;
	return true;
}

bool ListDelete(SqList &L, int pos, ElemType &del)
{
	if(pos<1 || pos>L.length)
	{
		return false;
	}
	del = L.data[pos-1];
	for(int i = pos; i<L.length; i++)
	{
		L.data[i-1] = L.data[i];
	}
	L.length--;
	return true;
}

int LocateElem(SqList L, ElemType element)
{
	for(int i = 0; i<L.length; i++)
	{
		if(element == L.data[i])
		{
			return i+1;
		}
	}
	return 0;
}

void PrintList(SqList L)
{
	for(int j = 0; j<L.length; j++)
	{
		printf("%d\t", L.data[j]);
	}
	printf("\n");
}

int main()
{
	SqList L;
	bool res;
	L.data[0] = 1;
	L.data[1] = 2;
	L.data[2] = 3;
	L.length = 3;
	res = ListInsert(L, 2, 50);
	if(res)
	{
		printf("insert sqlist successful！\n");
	}
	else
	{
		printf("insert sqlist failed！\n");
	}
	PrintList(L);
	printf("------------------------------\n");
	ElemType del;
	res = ListDelete(L, 1, del);
	if(res)
	{
		printf("delete sqlist elem successful！\n");
		printf("del element = %d\n", del);
		PrintList(L);
	}
	else
	{
		printf("delete elem failed！\n");
	}
	printf("------------------------------\n");
	int pos;  // 查找函数辅助元素位置
	pos = LocateElem(L, 4);
	if(pos)
	{
		printf("the locate of elem is %d\n", pos);
	}
	else
	{
		printf("no elem\n");
	}
	return 0;
}
