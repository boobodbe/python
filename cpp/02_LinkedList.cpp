// 单链表  2024-03-27

# include <stdio.h>
# define ElemType int
# include <stdlib.h>

typedef struct LNode{
	// 定义单链表节点类型，不带头节点的单链表
	ElemType data;
	struct LNode *next;
}LNode, *LinkList;

bool InitList(LinkList &L){
	// 初始化一个空的单链表
	L = NULL;
	return true;
}

bool InitListHead(LinkList &L){
	// 初始化一个带头结点的单链表
	L = (LNode *) malloc(sizeof(LNode));  // 分配一个头节点
	if(L == NULL)
		return false;  // 内存不足，分配失败
	L->next = NULL;  // 头节点之后暂时还没有节点
	return true;
}

bool Empty(LinkList L){
	// 判断单链表是否为空
	if(L == NULL)
		return true;
	else
		return false;
	// 或者可以直接写为：return (L==NULL);
}

bool EmptyHead(LinkList L){
	// 判断带头结点的单链表是否为空
	if(L->next == NULL)
		return true;
	else
		return false;
}

bool ListInsertHead(LinkList &L, int i, ElemType e){
	// 带头结点的单链表按位序插入元素，在第i个位置插入e
	if(i<1)
		return false;
	LNode *p;  // 指针p指向当前扫描到的节点
	int j = 0; // 当前p指向的是第几个节点
	p = L;  // L指向头节点，头节点是第0个节点，不存数据
	while(p!=NULL && j<i-1){
		// 循环找到第i-1个节点
		p = p->next;
		j++;
	}
	if(p==NULL)  // i值不合法
		return false;
	LNode *s = (LNode *) malloc(sizeof(LNode));
	s->data = e;
	s->next = p->next;
	p->next = s;  // 将节点s连接到p之后
	return true;  // 插入成功
}

bool ListInsert(LinkList &L, int i, ElemType e){
	// 不带头结点的单链表按位序在第i为上插入元素e
	if(i<1)
		return false;
	if(i == 1){
		LNode *s = (LNode *) malloc(sizeof(LNode));
		s->data = e;
		s->next = L;
		L = s;
		return true;
	}
	LNode *p;
	int j = 1;
	p = L;
	while(p!=NULL && j < i-1){
		p = p->next;
		j++;
	}
	if(p==NULL)
		return false;
	LNode *s = (LNode *) malloc(sizeof(LNode));
	s->data = e;
	s->next = p->next;
	p->next = s;
	return true;
}

bool InsertNextNode(LNode *p, ElemType e){
	// 后插操作，在节点p之后插入元素e
	if(p==NULL)
		return false;
	LNode *s = (LNode *) malloc(sizeof(LNode));
	if(s==NULL)
		return false;  // 内存分配失败
	s->data = e;
	s->next = p->next;
	p->next = s;
	return true;
}

bool InsertPriorNode(LNode *p, ElemType e){
	// 前插操作，在p节点之前插入元素e
	if(p==NULL)
		return false;
	LNode *s = (LNode *)malloc(sizeof(LNode));
	if(s==NULL)
		return false;
	s->data = p->data;
	p->data = e;
	s->next = p->next;
	p->next = s;
	return true;
}

bool ListDelete(LNode *L, int i, ElemType &e){
	// 删除操作，删除带头结点表L中第i个位置的元素，并用e返回删除元素的值
	if(i<1)
		return false;
	LNode *s = (LNode *)malloc(sizeof(LNode));
	int j = 0;
	s = L;
	while(s!=NULL && j<i-1){
		s = s->next;
		j++;
	}
	if(s==NULL && s->next==NULL)
		return false;
	LNode *q = s->next;
	e = s->next->data;
	s->next = s->next->next;
	free(q);
	return true;
}

bool DeleteNode(LNode *p){
	// 删除指定节点p
	if(p==NULL)
		return false;
	if(p->next!=NULL){
		// 未解决p->next是NULL的情况
		LNode *q;
		q = p->next;
		p->data = q->data;
		p->next = q->next;
		free(q);
		return true;
	}else{
		return false;
	}
}

bool GetElem(LNode *L, int i){
	// 按位查找操作，获取带头结点表L中第i个位置的元素的值
	if(i<1)
		return false;
	LNode *p = (LNode *)malloc(sizeof(LNode));
	int j = 0;
	p = L;
	while(p!=NULL && j<i){
		p = p->next;
		j++;
	}
	if(p==NULL)
		return false;
	ElemType NodeNum = p->data;
	printf("第%d个元素是：%d.\n", i, NodeNum);
	return true;
}

LNode *GetElemB(LinkList L, int i){
	// 按位查找另一种操作，找到第i个节点
	if(i<0)
		return NULL;
	LNode *p;
	int j = 0;
	p = L;
	while(p!=NULL && j<i){
		p = p->next;
		j++;
	}
	return p;
}

bool LocateElem(LNode *L, ElemType e){
	// 按值查找操作，在带头结点的表中查找具有关键字值的元素
	if(L==NULL)
		return false;  // 空表
	LNode *p = (LNode *)malloc(sizeof(LNode));
	int j = 0;
	p = L;
	while(p!=NULL && p->data!=e){
		p = p->next;
		j++;
	}
	if(p==NULL)
		return false;
	printf("元素%d在第%d个位置.\n", e, j);
	return true;
}

int LocateElemB(LinkList L, ElemType e){
	// 按值查找另一种操作
	if(L = NULL)
		return -1;
	LNode *p;
	int j = 0;
	p = L;
	while(p!=NULL && p->data!=e){
		p = p->next;
		j++;
	}
	if(p==NULL)
		return -1;
	return j;
}

LNode *LocateElemC(LinkList L, ElemType e){
	// 按值查找另一种方法
	LNode *p = L->next;
	while(p!=NULL && p->data!=e)
		p = p->next;
	return p;
}

int length(LinkList L){
	// 求单链表的长度
	int len = 0;
	LNode *p;
	while(p->next != NULL){
		p = p->next;
		len++;
	}
	return len;
}

LinkList List_TailInsert(LinkList &L){
	// 尾插法建立单链表
	int x;  // 输入节点的值
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	LNode *s,*r = L;  // r为表尾指针
	scanf("%d", &x);
	while(x!=9999){
		// 输入9999代表结束
		s = (LNode *)malloc(sizeof(LNode));
		s->data = x;
		r->next = s;
		r = s;
		scanf("%d", &x);
	}
	r->next = NULL;
	return L;
}

LinkList List_HeadInsert(LinkList &L){
	// 头插法建立单链表，重要应用，链表的逆置
	int x;
	L = (LinkList)malloc(sizeof(LNode));
	L->next = NULL;
	LNode *s = L;
	scanf("%d", &x);
	while(x!=9999){
		s = (LNode *)malloc(sizeof(LNode));
		s->data = x;
		s->next = L->next;
		L->next = s;
		scanf("%d", &x);
	}
	return L;
}

void test(){
	LinkList L;  // 声明一个指向单链表的指针
	InitList(L);  // 初始化一个空表
}

int main(){
	test();
	return 0;
}