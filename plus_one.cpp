#include<stdio.h>
#include <stdlib.h>

void arryprint(int *arry, int* size)//´òÓ¡º¯Êý
{
	for (int i = 0; i < (*size); i++)
	{
		printf("%d ", arry[i]);
	}
	printf("\n");
}
int plusOne()
{
	int arry1[] = { 1, 2, 4 };
	int arry2[] = { 1, 2, 9 };
	int arry3[] = { 9, 9, 9 };
 
	int *size1 = (int *)malloc(sizeof(int));
	int*rn1 = plusOne(arry1, 3, size1);
	arryprint(rn1, size1);
 
	int *size2 = (int *)malloc(sizeof(int));
	int*rn2 = plusOne(arry2, 3, size2);
	arryprint(rn2, size1);
 
	int *size3 = (int *)malloc(sizeof(int));
	int*rn3 = plusOne(arry3, 3, size3);
	arryprint(rn3, size3);
	
	printf("pause");
	return 0;
}
