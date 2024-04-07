// 顺序表课后题

# include <stdio.h>
# include <stdlib.h>
# define ElemType int
# define MaxSize 10



typedef struct 
{
	ElemType data[MaxSize];
	int length;
}SqList;

bool InitList(SqList &L){
	for(int i = 0; i < MaxSize; i++)
		L.data[i] = 0;
	L.length = 0;
	int s;
	int j = 0;
	scanf("%d", &s);
	while(s != 9999){
		if(L.length<MaxSize){
			L.data[j] = s;
			L.length++;
			j++;
			scanf("%d", &s);
		}
	}
	return true;
}

bool ListInsert(SqList &L, int i, ElemType e){
	if(i<1 || i>L.length+1)
		return false;
	if(L.length == MaxSize)
		return false;
	for(int j = L.length; j>=i; j--)
		L.data[j] = L.data[j-1];
	L.data[i-1] = e;
	L.length++;
	return true;
}

bool TailInsert(SqList &L, ElemType e){
	if(L.length >= MaxSize)
		return false;
	ListInsert(L, L.length, e);
	return true;
}

bool print(SqList L){
	if(L.length == 0){
		printf("当前表为空。\n");
		return false;
	}
	for(int i = 0; i<L.length; i++)
		printf("%d\t", L.data[i]);
	printf("\n");
	return true;
}

bool GetMinNum(SqList &L, ElemType &e){
	/*从顺序表中删除具有最小值的元素（假设唯一）并由函数返回被删除元素的值。空出的位置由最后一个元素填补，若顺序表为空则显示出错信息并退出运行。*/
	if(L.length == 0)
		return false;
	if(L.length == 1 || L.length == MaxSize){   // 该判断可省略
		e = L.data[L.length-1];
		L.length--;
		return true;
	}
	int flag = 0;
	e = L.data[0];
	for(int j = 1; j<L.length; j++){
		if(e > L.data[j]){
			e = L.data[j];
			flag = j;
		}
	}
	if(flag == L.length-1){  // 该判断可省略
		L.length--;
		return true;
	}
	L.data[flag] = L.data[L.length-1];
	L.length--;
	return true;
}

void ListReverse(SqList &L){
	// 设计一个高效的算法，将顺序表的所有元素逆置，要求算法的空间复杂度为O(1)
	ElemType e;
	for(int i = 0; i<(L.length/2); i++){
		e = L.data[i];
		L.data[i] = L.data[L.length-1-i];
		L.data[L.length-1-i] = e;
	}
	printf("逆置后的表是：\t");
	print(L);
}

bool DelSameNum(SqList &L, ElemType e){
	// 长度为n的顺序表L，编写一个时间复杂度为O(n)、空间复杂度为O(1)的算法，该算法删除线性表中所有值为x的数据元素。第17页，第3题
	if(L.length == 0)
		return false;
	int i = 0;
	while(i < L.length){
		if(L.data[i] == e){
			L.data[i] = L.data[L.length-1];
			L.length--;
		}else{
			i++;
		}
	}
	printf("删除所有%d以后的列表为：\t", e);
	print(L);
	return true;
}

bool removeSameNum(SqList &L, ElemType e){
	// 上一题的优化解法
	if(L.length == 0)
		return false;
	int i, j = 0;
	for(i = 0; i < L.length; i++){
		if(L.data[i] != e){
			L.data[j] = L.data[i];
			j++;
		}
	}
	L.length = L.length-j;
	for(i = j; i < L.length; i++)
		L.data[i] = 0;
	printf("删除所有%d以后的列表为：\t", e);
	print(L);
	return true;
}

void test(){
	SqList L;
	InitList(L);
	// printf("新增元素成功。\n");
	// printf("当前表长为：%d\n", L.length);
	printf("初始化的表为：\t");
	print(L);
	int MinNum;
	if(GetMinNum(L, MinNum)){
		printf("最小元素是：%d\n", MinNum);
		printf("删除最小元素%d的表是：\t", MinNum);
		print(L);
	}
	else{
		printf("表为空.\n");
	}
	ListReverse(L);
	// DelSameNum(L, 3);
	removeSameNum(L, 3);
}

int main(){
	test();
	return 0;
}