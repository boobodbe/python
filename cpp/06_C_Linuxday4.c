// 项目c课程作业
# include <stdio.h>
# include <stdlib.h>

void ninenine(){
	// 打印99乘法表
	int i, j;
	for(i = 1; i<10;i++){
		for(j = 1; j<i+1; j++){
			printf("%d * %d = %-4d", j, i, j*i);
		}
		printf("\n");
	}
}

void lingxing(){
	// 打印菱形
	int i, j;
	for(i = 1; i <= 9; i++){
		for(j = 1; j <= (5-i>0?5-i:i-5); j++){
			// 其中 (5-i>0?5-i:i-5) 可以换成abs(5-i)
			printf(" ");
		}
		for(j = 1; j <= 9 - 2*abs(5-i); j++){
			if(j % 2 == 1){
			printf("*");
		}else{
			printf(" ");
		}
		}
		printf("\n");
	}
}

void lingxing2(){
	// 打印空心的菱形
	int i, j; 
	for(i = 1; i <= 9; i++){
		for(j = 1; j <= abs(5-i); j++){
			printf(" ");
		}
		for(j = 1; j <= 9 - 2*abs(5-i); j++){
			if(j==1 || j==(9-2*abs(5-i))){
				printf("*");
			}else{
				printf(" ");
			}
		}
		printf("\n");
	}
}

// 求两个有序数组的公共元素
int compare_two_array(int a[], int b[], int lena, int lenb, int result[]){
    // 找两个数组的公共元素
    int i, j, count = 0;
    for(i = 0, j = 0; i<lena&&j<lenb;){
        if(a[i] == b[j]){
            result[count] = a[i];
            i++; j++; count++;
        }else if(a[i] > b[j]){
            j++;
        }else{
            i++;
        }
    }
    return count;
}
// 求三个有序数组的公共元素

// 找到一个数组的最大元素和次大的元素
void find_two_big_num(int a[], int len){
	int max1, max2;
	max1 = a[0]>a[1]?a[0]:a[1];
	max2 = a[0]<a[1]?a[0]:a[1];
	for(int i = 2; i < len; i++){
		if(a[i]>max1){
			max2 = max1;
			max1 = a[i];
		}else if(a[i]>max2){
			max2 = a[i];
		}
	}
	printf("The biggest num is %d, the second big num is %d.\n", max1, max2);
}

// 给定一个n个整形元素的数组a，其中有一个元素出现次数超过n/2次，求这个元素。
int find_the_most_num(int a[], int len){
	// 选举人法
	int candidate = a[0];
	int vote = 0; // 得票数
	int i;
	for(i = 0; i < len; i++){
		if(a[i] == candidate){
			vote++;
		}else{
			vote--;
			if(vote<0){
				candidate = a[i];
				vote = 1;
			}
		}
	}
	return candidate;
}


void test(){
	//调用测试函数
	//ninenine();
	// lingxing2();
	int a[] = {1,3,5,8,9,13,25,32};
    int b[] = {1,2,3,4,5,6,7,8};
    int c[] = {1,2,1,3,1,4,1,5,1,1};
    int result[10];
    int count = compare_two_array(a, b, 8, 8, result);
    printf("There are %d number is same.\n", count);
    find_two_big_num(a, 8);
    printf("The most num is %d.\n", find_the_most_num(c, 10));
}

int main(){
	test();
}