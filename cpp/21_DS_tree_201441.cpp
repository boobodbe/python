/*
2014  41.（13分）
二叉树的带权路径长度（WPL）是二叉树中所有叶结点的带权路径长度之和。给定一棵二叉树T，采用二叉链表存储，结点结构如下：
		left   weight   right
其中叶结点的weight域保存该结点的非负权值。
设root为指向T的根结点的指针，请设计求T的WPL的算法，要求：
1）给出算法的基本设计思想。
2）使用c或C++语言，给出二叉树结点的数据类型定义。
3）根据设计思想，采用C或C++语言描述算法，关键之处给出注释。

二叉树的带权路径长度为每个叶子节点的深度与权值之积的总和。
解析用到静态局部变量，有点难理解。
*/
#include <stdio.h>
#include <stdlib.h>

typedef int BiElemType;
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

int wpl = 0;
void PreOrder(BiTree p, int deep)
{
	// 前序遍历，先序遍历，深度优先遍历
	if(p!=NULL)
	{
		// printf("%c --> %d\n", p->c, deep);
		if(p->lchild==NULL && p->rchild==NULL)
		{
			wpl = wpl+p->c*deep;
		}
		PreOrder(p->lchild, deep+1);
		PreOrder(p->rchild, deep+1);
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
	PreOrder(tree,0);
	printf("wpl = %d\n", wpl);
	return 0;
}
