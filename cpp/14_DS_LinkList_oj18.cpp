//王道oj18题：http://oj.lgwenda.com/problem/18

#include <stdio.h>
#include <stdlib.h>

typedef struct LNode
{
	int data;
	struct LNode *next;
}LNode, *LinkList;

void PrintList(LinkList L)
{
	L = L->next;
	while (L != NULL)
	{
		printf("%3d", L->data);//打印当前结点数据
		L = L->next;//指向下一个结点
	}
	printf("\n");
}

void list_tail_insert(LinkList &L)
{
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	int x;
	scanf("%d", &x);
	LinkList s, r=L;
	while(x!=9999)
	{
		s = (LinkList)malloc(sizeof(LNode));
		s->data = x;
		r->next = s;
		r=s;
		scanf("%d", &x);
	}
	r->next = NULL;
}

LinkList GetElem(LinkList L, int pos)
{
	int i = 1;
	LinkList r = L->next;
	while(i<pos && r)
	{
		r = r->next;
		i++;
	}
	if(r)
	{
		return r;
	}
	return NULL;
}

void list_insert(LinkList L, int pos, int elem)
{
	LinkList r = GetElem(L, pos-1);
	LinkList s = (LinkList)malloc(sizeof(LNode));
	s->data = elem;
	s->next = r->next;
	r->next = s;
}

void list_del(LinkList L, int pos)
{
	LinkList r = GetElem(L, pos-1);
	LinkList q = r->next;
	r->next = q->next;
	free(q);
}

int main()
{
	LinkList L;
	list_tail_insert(L);
	LinkList second; 
	second = GetElem(L, 2);
	printf("%d\n", second->data);
	list_insert(L, 2, 99);
	PrintList(L);
	list_del(L, 4);
	PrintList(L);
	return 0;
}