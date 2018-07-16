#ifndef __Measurement_H__
#define __Measurement_H__
#include <time.h>//�������� ��� ������ � �����
#include <stdio.h>//�������� �����-������
#include "inouth.h"////������ �����-������ ������-�������
#include "CommonVector.h"//������ � ��������
#define measurements_number 28//������� �����

extern clock_t Res[measurements_number];//������ ��� ���� ��������������
extern clock_t Res1[measurements_number];//������ ��� ���� ����������������
extern clock_t Res2[measurements_number];//������ ��� ���� ��������-��������������
//���������
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
