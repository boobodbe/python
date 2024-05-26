#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;


typedef struct LNode
{
	ElemType data;
	struct LNode *next;
}LNode, *LinkList;

void list_head_insert(LinkList &L)
{
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	ElemType x;
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

void list_tail_insert(LinkList &L)
{
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	ElemType x;
	scanf("%d", &x);
	LNode *s, *r = L;
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

LinkList GetElem(LinkList L, int SearchPos)
{
	int i = 0;
	while(L && i<SearchPos)
	{
		L = L->next;
		i++;
	}
	return L;
}

LinkList LocateElem(LinkList L, ElemType SearchVal)
{
	while(L)
	{
		if(L->data == SearchVal)
		{
			return L;
		}
		L = L->next;
	}
	return NULL;
}

bool ListFrontInsert(LinkList L, int i, ElemType InsertVal)
{
	// 为什么L不需要引用
	LinkList p = GetElem(L, i-1);
	if(p == NULL)
	{
		return false;
	}
	LinkList q;
	q = (LinkList)malloc(sizeof(LNode));
	q->data = InsertVal;
	q->next = p->next;
	p->next = q;
	return true;
}

bool ListDelete(LinkList L, int i)
{
	// 删除时L是不会变的，所以不需要加引用
	LinkList p = GetElem(L, i-1);
	if(p == NULL)
	{
		return false;
	}
	LinkList q = p->next;
	p->next = q->next;
	free(q);
	return true;
}

void PrintList(LinkList L)
{
	L = L->next;
	while(L != NULL)
	{
		printf("%4d", L->data);
		L = L->next;
	}
	printf("\n");
}

int main(int argc, char const *argv[])
{
	// 链表
	LinkList L;
	// list_head_insert(L);
	list_tail_insert(L);
	PrintList(L);
	// int SearchPos;
	// scanf("%d", &SearchPos);
	// search = GetElem(L, SearchPos);
	// printf("%d\n", search->data);
	// int SearchVal;
	// scanf("%d", &SearchVal);
	// search = LocateElem(L, SearchVal);
	// printf("%d\n", search->data);
	// ListFrontInsert(L, 10, 99);
	// PrintList(L);
	printf("删除节点操作！\n");
	int i;
	scanf("%d", &i);
	ListDelete(L, i);
	PrintList(L);
	return 0;
}
