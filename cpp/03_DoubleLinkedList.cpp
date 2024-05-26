// 双链表

# include <stdio.h>
# define ElemType int
# include <stdlib.h>
# define MaxSize 10  // 用在静态链表

typedef struct DNode{
	ElemType data;
	struct DNode *prior, *next;
}DNode, *DLinkList;

bool InitDLinkList(DLinkList &L){
	// 初始化双链表，带头结点
	L = (DNode *)malloc(sizeof(DNode));
	if(L == NULL)
		return false;
	L->prior = NULL;
	L->next = NULL;
	return true;
}

bool Empty(DLinkList L){
	// 双链表判空
	if(L->next == NULL)
		return true;
	else
		return false;
}

bool InsertNextDNode(DNode *p, DNode *s){
	// 在p节点之后插入s节点
	if(p==NULL || s==NULL)
		return false;
	s->next = p->next;
	if(p->next != NULL)
		p->next->prior = s;
	s->prior = p;
	p->next = s;
	return true;
}

bool DeleteNextNode(DNode *p){
	// 删除给定p节点的后继节点
	if(p==NULL)
		return false;
	DNode *q = p->next;
	if(q==NULL)
		return false;
	p->next = q->next;
	if(q->next != NULL)
		q->next->prior = p;
	free(q);
	return true;
}

void DestoryList(DLinkList &L){
	// 循环释放各个数据节点
	while(L->next != NULL)
		DeleteNextNode(L);
	free(L);
	L = NULL;
}

// 双链表不具备随机存取的特性，查找操作只能通过顺序遍历实现

void testDLinkList(){
	// 初始化双链表
	DLinkList L;
	InitDLinkList(L);
}

// 以下是循环单链表部分
typedef struct LNodeXH{
	ElemType data;
	struct LNodeXH *next;
}LNodeXH, *LinkListXH;

bool InitListXH(LinkListXH &L){
	// 初始化一个循环单链表
	L = (LNodeXH *)malloc(sizeof(LNodeXH));
	if(L==NULL)
		return false;
	L->next = L;
	return true;
}

bool EmptyXH(LinkListXH L){
	// 判断循环单链表是否为空
	if(L->next == L)
		return true;
	else
		return false;
}

bool isTail(LinkListXH L, LNodeXH *p){
	// 判断循环链表的的p节点是否为表尾节点
	if(p->next == L)
		return true;
	else
		return false;
}

// 以下是循环双链表部分
bool InitDLinkListXH(DLinkList &L){
	// 初始化循环双链表
	L = (DNode *)malloc(sizeof(DNode));
	if(L==NULL)
		return false;
	L->prior = L;
	L->next = L;
	return true;
}

bool EmptyXHD(DLinkList L){
	// 循环双链表判空
	if(L->next == L)
		return true;
	else
		return false;
}

bool isTailXHD(DLinkList L, DNode *p){
	// 判断节点p是否为循环双链表的表尾节点
	if(p->next == L)
		return true;
	else
		return false;
}

bool InsertNextDNodeXH(DNode *p, DNode *s){
	// 将节点s插入到节点p之后
	s->next = p->next;
	p->next->prior = s;
	s->prior = p;
	p->next = s;
	return true;
}

// 以下是静态链表的部分，有空实现一下静态链表的增删改查，os的文件分配表
struct Node{
	// 定义节点
	ElemType data;
	int next;
};

typedef struct{
	// 静态链表结构类型另一种定义
	ElemType data;
	int next;
}SLinkList[MaxSize];

void testSLinkList(){
	struct Node a;
	printf("the size of Node is %d.\n", sizeof(Node));

	struct Node b[MaxSize];  // 数组a作为静态链表
	printf("the size of struct Node b is %d.\n", sizeof(b));

	SLinkList c;
	printf("the size of SLinkList c is %d.\n", sizeof(c));
}

int main(){
	testSLinkList();
	return 0;
}
