#include "inouth.h"//���������� ����������� �������




void InputMass(int mode)
{  // ������� ��� ���������� ������ �
	int i, j, k;
	int temp = 1; //��������� ����� ��� ��������������� ��� ��������� ������� ����� ������������ ����� A
	int temp1; // ��������� ����� ��� ��������������� ��� ��������� ������� ��� ���������� ������ �, ��� �� ��� ��������-������������
	switch (mode)
	{
	case 1: // �����-������������ ����� �
		for (k = 0; k < P; k++)
			for (j = 0; j < N; j++)
				for (i = 0; i < M; i++)
					A[k][i][j] = temp++;
		break;
	case 2: // ���������� ������ � ���������� �������
		for (k = 0; k < P; k++)
			for (j = 0; j < N; j++)
				for (i = 0; i < M; i++)
					A[k][i][j] =  10 + rand()%90;
		break;
	case 3: // ��������-������������ ����� �

		for (k = 0; k < P; k++) {
			temp1 = M*N;
			for (j = 0; j < N; j++)
			for (i = 0; i < M; i++)
					A[k][i][j] = temp1--;
		}
		break;
	default: break;
	}}
void showArray()
/*
�������, ��� ����������� ��� ������ ������ �� �����
� ������ ������� ������� ������
*/
{
	for (int k = 0;k < P;k++) {
		printf("Number %d\n", k);
		for (int i = 0;i < M; i++) {
			for (int j = 0;j < N;j++) {
				printf("|%4d", A[k][i][j]);
			}
			printf("|\n");
		}
		printf("\n");
	}
}

void rewriting(){//������� ������ � ����� � ������ 0-��������
    int k,j,i;
    for (k = 0; k < P; k++)
			for (j = 0; j < N; j++)
				for (i = 0; i < M; i++)
					a[k][i][j+1] = A[k][i][j];
    }
void rewriting2(){//������� ����� � ���������� �����
    int k,j,i;
    for (k = 0; k < P; k++)
			for (j = 0; j < N; j++)
				for (i = 0; i < M; i++)
					A[k][i][j] = a[k][i][j+1];
}

void InputVec(int mode)
{  // ������� ��� ���������� �������
	int i;
	int temp = 1; //��������� ����� ��� ��������������� ��� ��������� ������� ����� ������������ ����� A
	int temp1; // ��������� ����� ��� ��������������� ��� ��������� ������� ��� ���������� ������ �, ��� �� ��� ��������-������������
	switch (mode)
	{
	case 1: // �����-������������ ����� �
				for (i = 0; i < M*N; i++)
					vec[i] = temp++;
		break;
	case 2: // ���������� ������ � ���������� �������
				for (i = 0; i < M*N; i++)
					vec[i] =  10 + rand()%90;
		break;
	case 3: // ��������-������������ ����� �
            temp1=N;
			for (i = 0; i < M*N; i++)
					vec[i] = temp1--;
		break;
	default: break;}
	}
void showVector()
/*
�������, ��� ����������� ��� ������ ������� �� �����
*/
{
			for (int j = 0;j < M*N;j++)
				printf("|%4d", vec[j]);
}

void rewritevec(){//������� ��� �������� ������� � ������ � ������ 0 ���������
    for(int i=0;i<M*N;i++)
        vec1[i+1]=vec[i];
    }
void rewritevec2(){//������� ��� �������� ������� ����� � ����������
    for(int i=0;i<M*N;i++)
        vec[i]=vec1[i+1];
    }
