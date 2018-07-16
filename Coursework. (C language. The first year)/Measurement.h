#ifndef __Measurement_H__
#define __Measurement_H__
#include <time.h>//бібліотека для роботи з часом
#include <stdio.h>//бібліотека вводу-виводу
#include "inouth.h"////модуль вводу-виводу масива-вектора
#include "CommonVector.h"//модуль з розмірами
#define measurements_number 28//кількість вимірів

extern clock_t Res[measurements_number];//вектор для часів впорядкованого
extern clock_t Res1[measurements_number];//вектор для часів невпорядкованого
extern clock_t Res2[measurements_number];//вектор для часів обернено-впорядкованого
//прототипи
void OutTable();
void OutResults();
void InputSortMeasurement();
void InputSortVecMeasurement();
void SelectSortMeasurement();
void SelectSortVecMeasurement();
void ExchangeSortMeasurement();
void ExchangeSortVecMeasurement();
void QuickSortMeasurement();
void QuickSortVecMeasurement();
void MeasurementProcessing(clock_t* Res);

#endif
