/*
今天是2024-05-25 18：30
开始学：树，数据结构代码
树是一种逻辑结构
满二叉树共有 2^n - 1 个节点
完全二叉树是缺失右下节点的二叉树

通过辅助队列建议二叉树

前序遍历：也叫先序遍历，属于深度优先遍历
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

void PreOrder(BiTree p)
{
	// 前序遍历，先序遍历，深度优先遍历
	if(p!=NULL)
	{
		printf("%c ", p->c);
		PreOrder(p->lchild);
		PreOrder(p->rchild);
	}
}

void InOrder(BiTree p)
{
	if(p!=NULL)
	{
		InOrder(p->lchild);
		printf("%c ", p->c);
		InOrder(p->rchild);
	}
}

void PostOrder(BiTree p)
{
	if(p!=NULL)
	{
		PostOrder(p->lchild);
		PostOrder(p->rchild);
		printf("%c ", p->c);
	}
}

void LevelOrder(BiTree T)
{
	// 层序遍历，也叫广度优先遍历
	LinkQueue Q;
	InitQueue(Q);
	BiTree p;// 存储出队的节点
	EnQueue(Q, T);
	while(!IsEmpty(Q))
	{
		DeQueue(Q, p);
		putchar(p->c);
		if(p->lchild)
		{
			EnQueue(Q, p->lchild);
		}
		if(p->rchild)
		{
			EnQueue(Q, p->rchild);
		}
	}
}

int main(int argc, char const *argv[])
{
	BiTree pnew; // 用来指向新申请的树节点
	BiTree tree = NULL;//tree 是指向树根的，代表树
	ptag_t phead = NULL, ptail = NULL, listpnew = NULL, pcur = NULL;
	char c;  // abcdefghij
	while(scanf("%c", &c))
	{
		if(c=='\n')
		{
			break;
		}
		// calloc申请的空间大小是他的两个参数相乘，并对空间进行初始化，初始化为0
		pnew = (BiTree)calloc(1, sizeof(BiTNode));
		pnew->c = c;
		listpnew = (ptag_t)calloc(1, sizeof(tag_t));
		// 给队列节点申请空间
		listpnew->p = pnew;
		// 如果是树的第一个节点
		if(tree == NULL) // 这里之前写错了，if(pnew==NULL)
		{
			tree = pnew;// tree指向根节点
			phead = listpnew;
			ptail = listpnew;//第一个节点，既是队列头，也是队列尾
			pcur = listpnew;//pcur指向要进入树的父亲元素
		}else{
			//让元素入队列
			ptail->pnext = listpnew;
			ptail = listpnew;
			//接下来把b放入数组
			if(pcur->p->lchild == NULL)
			{
				pcur->p->lchild = pnew;
			}else if(pcur->p->rchild == NULL)
			{
				pcur->p->rchild = pnew;//pcur->p右孩子为空，就放入右孩子
				pcur = pcur->pnext;//当前节点的左右孩子都满了，指向辅助队列的下一个
			}
		}
	}
	printf("-------PreOrder-----------\n");
	PreOrder(tree);
	printf("\n-------IreOrder-----------\n");
	InOrder(tree);
	printf("\n-------PostOrder-----------\n");
	PostOrder(tree);
	printf("\n-------LevelOrder-----------\n");
	LevelOrder(tree);
	return 0;
}
// 学到二叉树的4种遍历方式，明天继续，还有一个真题和oj，2024-05-25  20：22