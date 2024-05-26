// 王道oj的题：http://oj.lgwenda.com/problem/17
#include <stdio.h>
#include <stdlib.h>

typedef struct LNode
{
	int data;
	struct LNode *next;
}LNode, *LinkList;

//打印链表中每个结点的值
void PrintList(LinkList L)
{
	L=L->next;
	while(L!=NULL)
	{
		printf("%d",L->data);//打印当前结点数据
		L=L->next;//指向下一个结点
		if(L!=NULL)
		{
			printf(" ");
		}
	}
	printf("\n");
}

void ListHeadInsert(LinkList &L)
{
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	int x;
	scanf("%d", &x);
	LNode *s;
	while(x!=9999)
	{
		s = (LinkList)malloc(sizeof(LNode));
		s->data = x;
		s->next = L->next;
		L->next = s;
		scanf("%d", &x);
	}
}

void ListTailInsert(LinkList &L)
{
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	int x;
	scanf("%d", &x);
	LNode *s, *r = L;
	while(x!=9999)
	{
		s = (LinkList)malloc(sizeof(LNode));
		s->data = x;
		r->next = s;
		r = s;
		scanf("%d", &x);
	}
	r->next = NULL;
}

int main(int argc, char const *argv[])
{
	LinkList L;
	ListHeadInsert(L);
	PrintList(L);
	ListTailInsert(L);
	PrintList(L);
	return 0;
}
