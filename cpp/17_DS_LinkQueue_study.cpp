// 通过链表实现队列
#include <stdio.h>
#include <stdlib.h>

typedef int Elemtype;
typedef struct LinkNode{
	Elemtype data;
	struct LinkNode *next;
}LinkNode;
typedef struct{
	LinkNode *front, *rear; // 链表头、链表尾
}LinkQueue;

void InitQueue(LinkQueue &q)
{
	q.front = q.rear = (LinkNode*)malloc(sizeof(LinkNode));
	q.front->next = NULL;
}

void EnQueue(LinkQueue &q, Elemtype x)
{
	LinkNode *pnew = (LinkNode*)malloc(sizeof(LinkNode));
	pnew->data = x;
	pnew->next = NULL;
	q.rear->next = pnew;
	q.rear = pnew;
}

bool DeQueue(LinkQueue &q, Elemtype &elem)
{
	if(q.rear == q.front){
		return false;
	}
	LinkNode *qnew = q.front->next;
	elem = qnew->data;
	q.front->next = qnew->next;
	if(q.rear == qnew){
		q.rear = q.front; // 链表只剩一个节点
	}
	free(qnew);
	return true;
}

int main(int argc, char const *argv[])
{
	LinkQueue q;
	bool ret;
	Elemtype elem;
	InitQueue(q);
	EnQueue(q, 3);
	EnQueue(q, 4);
	EnQueue(q, 5);
	EnQueue(q, 6);
	EnQueue(q, 7);
	ret = DeQueue(q, elem);
	if(ret)
	{
		printf("出队成功，元素为%d\n", elem);
	}else{
		printf("出队失败。\n");
	}
	return 0;
}