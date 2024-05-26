// 2019真题41题
#include <stdio.h>
#include <stdlib.h>

typedef struct LNode
{
	int data;
	struct LNode *next;
}LNode, *LinkList;

void list_tail_insert(LinkList &L)
{
	// 尾插法建立单链表
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	int x;
	scanf("%d", &x);
	LNode *s, *r=L;
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

void print_list(LinkList L)
{
	L = L->next;
	while(L!=NULL)
	{
		printf("%4d", L->data);
		L = L->next;
	}
	printf("\n");
}

void find_middle(LinkList L, LinkList &L2)
{
	L2 = (LinkList)malloc(sizeof(LNode));
	LinkList pcur, ppre; // 双指针法
	pcur = ppre = L->next;
	while(pcur)
	{
		pcur = pcur->next;
		if(pcur==NULL)
		{
			break;
		}
		pcur = pcur->next;
		if(pcur == NULL)
		{
			break;// 偶数个节点判断
		}
		ppre = ppre->next;
	}
	L2->next = ppre->next; // L2指向后半条链表的头节点
	ppre->next = NULL; // 前一半链表的最后一个节点指向NULL
}

void reverse(LinkList L2)
{	
	LinkList r,s,t;
	r = L2->next;
	if(r == NULL)
	{
		return;// 链表为空
	}
	s= r->next;
	if(s==NULL)
	{
		return;//链表只有一个车节点
	}
	t = s->next;
	while(t)
	{
		s->next = r;//原地逆置
		r=s;
		s=t;
		t=t->next;
	}
	s->next = r;
	L2->next->next = NULL;//逆置后第一个节点的next为NULL
	L2->next = s;
}

void merge(LinkList L, LinkList L2)
{
	//合并两个链表
	LinkList pcur, p, q;
	pcur = L->next;// pcur始终指向组合后链表的链表尾
	p = pcur->next;
	q = L2->next;
	while(p!=NULL&&q!=NULL)
	{
		pcur->next = q;
		q=q->next;
		pcur = pcur->next;
		pcur->next = p;
		p = p->next;
		pcur = pcur->next;
	}
	if(p!=NULL)
	{
		pcur->next = p;
	}
	if(q!=NULL)
	{
		pcur->next = q;
	}
}

int main()
{
	LinkList L;
	list_tail_insert(L);
	print_list(L);
	// 寻找中间节点
	LinkList L2;
	find_middle(L, L2);
	printf("---------------------\n");
	print_list(L);
	print_list(L2);
	printf("---------------------\n");
	reverse(L2);
	print_list(L2);
	printf("---------------------\n");
	merge(L, L2);
	free(L2);
	print_list(L);
	return 0;
}

