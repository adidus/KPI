#include "Measurement.h"//підключення інтерфейсної частини
#define measurements_number 28//кількість вимірів

clock_t Res[measurements_number];
clock_t Res1[measurements_number];
clock_t Res2[measurements_number];

void OutTable()
{
// Усереднений результат вимірів буде виведено на екран у портібну позицію
    printf("\t\t Ordered \t Random \t BackOrdered \n");}
void OutResults(){//процедура виводу результатів на екран
    printf("\t %6.1f \t %6.1f \t %10.1f \n", (float)Res[0]/20 , (float)Res1[0]/20 , (float)Res2[0]/20);
    printf("\n\n");
}

void InputSortMeasurement()//вимір часу при вставці масиву
{
    for (int i = 0; i < measurements_number; i++)
    {
        InputMass(1);//заповнення впорядковано
        Res[i] = sorting1();
        InputMass(2);//заповнення невпорядковано
        Res1[i] = sorting1();
        InputMass(3);//заповнення обернено-впорядковано
        Res2[i] = sorting1();
    }
}

void InputSortVecMeasurement()//вимір часу при вставці вектора
{
    for (int i = 0; i < measurements_number; i++)
    {
        InputVec(1);//заповнення впорядковано
        Res[i] = sortvec1();
        InputVec(2);//заповнення невпорядковано
        Res1[i] = sortvec1();
        InputVec(3);//заповнення обернено-впорядковано
        Res2[i] = sortvec1();
    }
}
void SelectSortMeasurement()//вимірт часу при виборі №5
{
    for (int i = 0; i < measurements_number; i++)
    {
        InputMass(1);//заповнення впорядковано
        Res[i] = sorting2();
        InputMass(2);//заповнення невпорядковано
        Res1[i] = sorting2();
        InputMass(3);//заповнення обернено-впорядковано
        Res2[i] = sorting2();
    }
}

void SelectSortVecMeasurement()//вимір при сорутванні вибору №5 вектора
{
    for (int i = 0; i < measurements_number; i++)
    {
        InputVec(1);//заповнення впорядковано
        Res[i] = sortvec2();
        InputVec(2);//заповнення невпорядковано
        Res1[i] = sortvec2();
        InputVec(3);//заповнення обернено-впорядковано
        Res2[i] = sortvec2  ();
    }
}

void ExchangeSortMeasurement()//вимір при сортуванні бульбашкою масива
{
    for (int i = 0; i < measurements_number; i++)
    {
        InputMass(1);//заповнення впорядковано
        Res[i] = sorting3();
        InputMass(2);//заповнення невпорядковано
        Res1[i] = sorting3();
        InputMass(3);//заповнення обернено-впорядковано
        Res2[i] = sorting3();
    }
}

void ExchangeSortVecMeasurement()//вимір при сортуванні бульбашкою вектору
{
    for (int i = 0; i < measurements_number; i++)
    {
        InputVec(1);//заповнення впорядковано
        Res[i] = sortvec3();
        InputVec(2);//заповнення невпорядковано
        Res1[i] = sortvec3();
        InputVec(3);//заповнення обернено-впорядковано
        Res2[i] = sortvec3();
    }
}


void QuickSortMeasurement()//вимір при сортуванні Хоара масиву
{
    for (int i = 0; i < measurements_number; i++)
    {
        InputMass(1);//заповнення впорядковано
        Res[i] = sorting4();
        InputMass(2);//заповнення невпорядковано
        Res1[i] = sorting4();
        InputMass(3);//заповнення обернено-впорядковано
        Res2[i] = sorting4();
    }
}

void QuickSortVecMeasurement()//вимір при сортуванні Хоара вектору
{
    for (int i = 0; i < measurements_number; i++)
    {
        InputVec(1);//заповнення впорядковано
        Res[i] = sortvec4();
        InputVec(2);//заповнення невпорядковано
        Res1[i] = sortvec4();
        InputVec(3);//заповнення обернено-впорядковано
        Res2[i] = sortvec4();
    }
}


void MeasurementProcessing(clock_t* Res)
{
    long int Sum,Min1,Min2,Min3,Max1,Max2,Max3;
    int imin1,imin2,imin3,imax1,imax2,imax3;
// Два перших виміри (0-й та 1-й) відкидаються
// Серед інших елементів знаходимо три мінімальних та три максимальних
// елементи і віднімаємо їх значення із загальної суми
// Знаходимо мінімальний та максимальний елементи і виключаємо їх з наступних
// пошуків, встановивши їм значення -1
    Sum = Res[2]; Min1 = Res[2]; Max1 = Res[2]; imin1 = 2; imax1 = 2;
    for (int i = 3; i < measurements_number; i++)
    {
        Sum = Sum + Res[i];
        if (Res[i] > Max1) { Max1 = Res[i]; imax1 = i; }
        else if (Res[i] < Min1) { Min1 = Res[i]; imin1 = i; }
    }
    Res[imin1]=-1; Res[imax1]=-1;

// Знаходимо другий мінімальний та другий максимальний елементи
// і виключаємо їх з наступних пошуків, встановивши їм значення -1
    if (Res[2] == -1) {Min2 = Res[3]; imin2 = 3;}
    else {Min2 = Res[2]; imin2 = 2;}
    Max2 = Res[2]; imax2 = 2;
    for (int i = 3; i < measurements_number; i++)
    {
        if (Res[i] > Max2) { Max2 = Res[i]; imax2 = i; }
        else if (Res[i]<Min2 && Res[i]!=-1) { Min2 = Res[i]; imin2 = i; }
    }
    Res[imin2]=-1; Res[imax2]=-1;

// Знаходимо третій мінімальний та третій максимальний елементи
    if (Res[2] == -1)
        if (Res[3] == -1) {Min3 = Res[4]; imin3 = 4;}
        else {Min3 = Res[3]; imin3 = 3;}
    else {Min3 = Res[2]; imin3 = 2;}
    Max3 = Res[2]; imax3 = 2;
    for (int i = 3; i < measurements_number; i++)
    {
        if (Res[i] > Max3) { Max3 = Res[i]; imax3 = i; }
        else if (Res[i]<Min3 && Res[i]!=-1) { Min3 = Res[i]; imin3 = i; }
    }

// Сума всіх вимірів мінус три максимальних та три мінімальних значення буде записана до 0-го елемента масива Res
    Res[0] = Sum - Min1 - Min2 - Min3 - Max1 - Max2 - Max3;
}

