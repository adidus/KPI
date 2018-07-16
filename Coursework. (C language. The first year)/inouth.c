#include "inouth.h"//підключення інтерфейсної частини




void InputMass(int mode)
{  // функція для заповнення масиву А
	int i, j, k;
	int temp = 1; //тимчасова змінна яка використовується для зберігання значень якими заповнюється масив A
	int temp1; // тимчасова змінна яка використовується для зберігання значень при заповнення масиву А, щоб він був обернено-відсортований
	switch (mode)
	{
	case 1: // прямо-відсортований масив А
		for (k = 0; k < P; k++)
			for (j = 0; j < N; j++)
				for (i = 0; i < M; i++)
					A[k][i][j] = temp++;
		break;
	case 2: // заповнення масиву А рандомними числами
		for (k = 0; k < P; k++)
			for (j = 0; j < N; j++)
				for (i = 0; i < M; i++)
					A[k][i][j] =  10 + rand()%90;
		break;
	case 3: // обернено-відсортований масив А

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
Функція, яка призначення для виводу масиву на екран
у вигляді матриці перерізів масиву
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

void rewriting(){//перепис масиву у новий з вільним 0-стовбцем
    int k,j,i;
    for (k = 0; k < P; k++)
			for (j = 0; j < N; j++)
				for (i = 0; i < M; i++)
					a[k][i][j+1] = A[k][i][j];
    }
void rewriting2(){//перепис назад у початковий масив
    int k,j,i;
    for (k = 0; k < P; k++)
			for (j = 0; j < N; j++)
				for (i = 0; i < M; i++)
					A[k][i][j] = a[k][i][j+1];
}

void InputVec(int mode)
{  // функція для заповнення вектора
	int i;
	int temp = 1; //тимчасова змінна яка використовується для зберігання значень якими заповнюється масив A
	int temp1; // тимчасова змінна яка використовується для зберігання значень при заповнення масиву А, щоб він був обернено-відсортований
	switch (mode)
	{
	case 1: // прямо-відсортований масив А
				for (i = 0; i < M*N; i++)
					vec[i] = temp++;
		break;
	case 2: // заповнення масиву А рандомними числами
				for (i = 0; i < M*N; i++)
					vec[i] =  10 + rand()%90;
		break;
	case 3: // обернено-відсортований масив А
            temp1=N;
			for (i = 0; i < M*N; i++)
					vec[i] = temp1--;
		break;
	default: break;}
	}
void showVector()
/*
Функція, яка призначення для виводу вектора на екран
*/
{
			for (int j = 0;j < M*N;j++)
				printf("|%4d", vec[j]);
}

void rewritevec(){//функція для перепису вектора в вектор з пустим 0 елементом
    for(int i=0;i<M*N;i++)
        vec1[i+1]=vec[i];
    }
void rewritevec2(){//функція для перепису вектора назад в початковий
    for(int i=0;i<M*N;i++)
        vec[i]=vec1[i+1];
    }
