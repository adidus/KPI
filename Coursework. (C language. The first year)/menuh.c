#include <stdio.h>//бібл. вводу-виводу
#include "menuh.h"//підключення інтерфейсної частини


void insertV() {//тестування сортування вставки на векторі
	system("cls");
	printf("Insert #3\n");
	printf("Ordered array\n");
	InputVec(1);
	showVector();
	sortvec1();
	printf("\nAfter sorting\n");
	showVector();
	printf("\n\nRandom array\n");
	InputVec(2);
	showVector();
	sortvec1();
	printf("\nAfter sorting\n");
	showVector();
	printf("\n\nBackOrdered array\n");
	InputVec(3);
	showVector();
	sortvec1();
	printf("\nAfter sorting\n");
	showVector();
	printf("\nPress Enter for back");
	_getch();
}

void selectV() {//тестування сортування вибору вектору
	system("cls");
	printf("Select #5\n");
	printf("Ordered array\n");
	InputVec(1);
	showVector();
	sortvec2();
	printf("\nAfter sorting\n");
	showVector();
	printf("\n\nRandom array\n");
	InputVec(2);
	showVector();
	sortvec2();
	printf("\nAfter sorting\n");
	showVector();
	printf("\n\nBackOrdered array\n");
	InputVec(3);
	showVector();
	sortvec2();
	printf("\nAfter sorting\n");
	showVector();
	printf("\nPress Enter for back");
	_getch();
}

void exchangeV() {//тестування сортування обміну вектора
	system("cls");
	printf("Exchange\n");
	printf("Ordered array\n");
	InputVec(1);
	showVector();
	sortvec3();
	printf("\nAfter sorting\n");
	showVector();
	printf("\n\nRandom array\n");
	InputVec(2);
	showVector();
	sortvec3();
	printf("\nAfter sorting\n");
	showVector();
	printf("\n\nBackOrdered array\n");
	InputVec(3);
	showVector();
	sortvec3();
	printf("\nAfter sorting\n");
	showVector();
	printf("\nPress Enter for back");
	_getch();
}

void HoaraV() {//тестування сортування Хоара на векторі
	system("cls");
	printf("Hoara\n");
	printf("Ordered array\n");
	InputVec(1);
	showVector();
	sortvec4();
	printf("\nAfter sorting\n");
	showVector();
	printf("\n\nRandom array\n");
	InputVec(2);
	showVector();
	sortvec4();
	printf("\nAfter sorting\n");
	showVector();
	printf("\n\nBackOrdered array\n");
	InputVec(3);
	showVector();
	sortvec4();
	printf("\nAfter sorting\n");
	showVector();
	printf("\nPress Enter for back");
	_getch();
}

void selectA() {//тестування сортування вибору на тривимірного масиву
	system("cls");
	printf("Select #5\n");
	printf("Ordered array\n");
    InputMass(1);
    showArray();
	sorting2();
	printf("\nAfter sorting\n");
	showArray();
	printf("\n\nRandom array\n");
    InputMass(2);
	showArray();
	sorting2();
	printf("After sorting\n");
	showArray();
	printf("BackOrdered array\n");
	InputMass(3);
    showArray();
	sorting2();
	printf("After sorting\n");
	showArray();
	printf("\nPress Enter for back");
	_getch();
}

void insertA() {//тестування сорутвання вставки на масиві
	system("cls");
    printf("Insert #3\n");
	printf("Ordered array\n");
    InputMass(1);
    showArray();
	sorting1();
	printf("After sorting\n");
	showArray();
	printf("\nRandom array\n");
    InputMass(2);
	showArray();
	sorting1();
	printf("After sorting\n");
	showArray();
	printf("BackOrdered array\n");
	InputMass(3);
    showArray();
	sorting1();
	printf("After sorting\n");
	showArray();
	printf("\nPress Enter for back");
	_getch();
}
void exchangeA() {//тестування сортування обміну на масиві
	system("cls");
    printf("Exchange\n");
	printf("Ordered array\n");
    InputMass(1);
    showArray();
	sorting3();
	printf("After sorting\n");
	showArray();
	printf("\nRandom array\n");
    InputMass(2);
	showArray();
	sorting3();
	printf("After sorting\n");
	showArray();
	printf("BackOrdered array\n");
	InputMass(3);
    showArray();
	sorting3();
	printf("After sorting\n");
	showArray();
	printf("\nPress Enter for back");
	_getch();
}
void HoaraA() {//тестування сортування Хоара на масиві
	system("cls");
    printf("Hoara\n");
	printf("Ordered array\n");
    InputMass(1);
    showArray();
	sorting4();
	printf("After sorting\n");
	showArray();
	printf("\nRandom array\n");
    InputMass(2);
	showArray();
	sorting4();
	printf("After sorting\n");
	showArray();
	printf("BackOrdered array\n");
	InputMass(3);
    showArray();
	sorting4();
	printf("After sorting\n");
	showArray();
	printf("\nPress Enter for back");
	_getch();
}


void timemeasurement() {//пункт виміру часу в меню
	do {
	system("cls");
	int mode;
	printf("Time measurement\nSizes of array: P=%d M=%d N=%d\n",P,M,N);
	printf("\nChoose sorting:\n");
	printf("1.Insert #3(vector)\n2.Select #5(vector)\n");
	printf("3.Exchange #1(vector)\n4.Hoara (vector)\n");
	printf("5.Insert #3(array)\n6.Select #5(array)\n");
	printf("7.Exchange #1(array)\n8.Hoara (array)\n");
	printf("9.Pack mode(array)\n10.Pack mode(vector)\n");
	printf("\nPlease input the number of menu(0-back):");
	scanf_s("%d", &mode);
	switch (mode)//вибір пункту меню
	{
		case 0: return; break;
		case 1:
			system("cls");
			InputSortVecMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Insert ¹3");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
		case 2:
			system("cls");
			SelectSortVecMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Select ¹5");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
		case 3:
			system("cls");
			ExchangeSortVecMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Exchange ¹1");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
		case 4:
			system("cls");
			QuickSortVecMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Hoara   ");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
		case 5:
			system("cls");
			InputSortMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Insert ¹3");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
		case 6:
			system("cls");
			SelectSortMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Select ¹5");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
        case 7:
			system("cls");
			ExchangeSortMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Exchange ¹1");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
        case 8:
			system("cls");
			QuickSortMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Hoara   ");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
		case 9:
			system("cls");
            printf("Sizes of array:\n P=%d M=%d N=%d", P, M, N);
            printf("\n");
			InputSortMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Insert ¹3");
			OutResults();
			SelectSortMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			printf("Select ¹5");
			OutResults();
			ExchangeSortMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			printf("Exchange ¹1");
			OutResults();
			QuickSortMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			printf("Hoara   ");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
        case 10:
			system("cls");
            printf("Sizes of array:\n M=%d N=%d", M, N);
            printf("\n");
			InputSortVecMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			OutTable();
			printf("Insert ¹3");
			OutResults();
			SelectSortVecMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			printf("Select ¹5");
			OutResults();
			ExchangeSortVecMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			printf("Exchange ¹1");
			OutResults();
			QuickSortVecMeasurement();
			MeasurementProcessing(Res);
            MeasurementProcessing(Res1);
            MeasurementProcessing(Res2);
			printf("Hoara   ");
			OutResults();
			printf("\nPress Enter for back");
			_getch();
			break;
		default:
		printf("Please input CORRECT number (Enter)");
		_getch();
		break;
		}
	} while (1);
}
void testsorting() {//пункт меню для тестування сортування і виводу його на екран
	do {
		system("cls");
		int mode;
	printf("Test sortings\nSizes of array: P=%d M=%d N=%d\n",P,M,N);
	printf("\nChoose sorting:\n");
	printf("1.Insert #3(vector)\n2.Select #5(vector)\n");
	printf("3.Exchange #1(vector)\n4.Hoara (vector)\n");
	printf("5.Insert #3(array)\n6.Select #5(array)\n");
	printf("7.Exchange #1(array)\n8.Hoara (array)\n");
    printf("\nPlease input the number of menu(0-back):");
        scanf_s("%d", &mode);
        switch (mode)//вибір виду сортування
		{
		case 0: return; break;
		case 1:
			insertV();
			break;
		case 2:
			selectV();
			break;
		case 3:
			exchangeV();
			break;
		case 4:
			HoaraV();
			break;
		case 5:
			insertA();
			break;
		case 6:
			selectA();
			break;
        case 7:
			exchangeA();
			break;
        case 8:
			HoaraA();
			break;
		default:
			printf("Please input CORRECT number (Enter)");
			_getch();
			break;
		}
	} while (1);
}
void menu(){//меню з вибором тестування часу і тестування сортувань
	do {
	system("cls");
	printf("Course work #63\n\n");
	printf("Choose mode:\n1- time measurement\n");
    printf("2-testing sorting\n3-exit:\n");
	int vote;
		scanf_s("%d", &vote);
		switch (vote)//вибір одного з двох пунктів
		{
		case 1: timemeasurement(); break;
		case 2: testsorting(); break;
		case 3: return;
		default:
			printf("Please input CORRECT number (Press Enter)");
			_getch();
			break;
		}
	} while (1);
}
