/*
王道oj：http://oj.lgwenda.com/problem/20
T20：
读取字符串abcdefghij，然后层次建树建立一颗二叉树，然后前序遍历输出abdhiejcfg，注意不要打印前序遍历几个汉字
input: abcdefghij  output: abdhiejcfg
*/
#include <stdio.h>
#include <stdlib.h>

typedef char BiElemType;
typedef struct BiTNode
{
	// 二叉树节点
	BiElemType c;
	struct BiTNode *lchild;
	struct BiTNode *rchild;
}BiTNode, *BiTree;

typedef struct tag
{
	BiTree p;// 树的某一个节点的地址值
	struct tag *pnext;
}tag_t, *ptag_t;

// 下面是队列的实现
typedef BiTree Elemtype;
typedef struct LinkNode{
	Elemtype data;
	struct LinkNode *next;
}LinkNode;
typedef struct{
	LinkNode *front, *rear; // 链表头、链表尾
}LinkQueue;

bool IsEmpty(LinkQueue q)
{
	return q.front==q.rear;
}

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
// 上面是队列的实现

void PreOrder(BiTree tree)
{
	if(tree != NULL)
	{
		printf("%c", tree->c);
		PreOrder(tree->lchild);
		PreOrder(tree->rchild);
	}
}

void InOrder(BiTree tree)
{
	if(tree != NULL)
	{
		InOrder(tree->lchild);
		printf("%c", tree->c);
		InOrder(tree->rchild);
	}
}

void PostOrder(BiTree tree)
{
	if(tree!=NULL)
	{
		PostOrder(tree->lchild);
		PostOrder(tree->rchild);
		printf("%c", tree->c);
	}
}

void LevelOrder(BiTree T)
{
	LinkQueue Q;
	InitQueue(Q);
	BiTree p;
	EnQueue(Q, T);
	while(!IsEmpty(Q))
	{
		DeQueue(Q, p);
		putchar(p->c);
		if(p->lchild)
		{
			EnQueue(Q,p->lchild);
		}
		if(p->rchild)
		{
			EnQueue(Q, p->rchild);
		}
	}
}

int main()
{
	BiTree pnew; // 用来指向新申请的树节点
	BiTree tree = NULL; // 指向树根，代表树
	ptag_t phead = NULL, ptail = NULL, listpnew = NULL,pcur = NULL;
	char c;
	while(scanf("%c", &c))
	{
		if(c=='\n')
		{
			break;
		}
		// 用calloc申请空间，大小是他的两个参数相乘，并对空间进行初始化，初始化为0
		pnew = (BiTree)calloc(1,sizeof(BiTNode));
		pnew->c = c;
		listpnew = (ptag_t)calloc(1,sizeof(tag_t));
		listpnew->p = pnew;
		if(tree == NULL)
		{
			tree = pnew;
			phead = listpnew;
			ptail = listpnew;
			pcur = listpnew;
		}else{
			ptail->pnext = listpnew;
			ptail = listpnew;
			if(pcur->p->lchild == NULL)
			{
				pcur->p->lchild = pnew;
			}else if(pcur->p->rchild == NULL)
			{
				pcur->p->rchild = pnew;
				pcur = pcur->pnext;
			}
		}
	}
	// PreOrder(tree);
	InOrder(tree);
	printf("\n");
	PostOrder(tree);
	printf("\n");
	LevelOrder(tree);
	return 0;
}
// 树的代码完成，oj两个题完成，有点懵，尤其是建树和层序遍历。2024-05-26 21：12