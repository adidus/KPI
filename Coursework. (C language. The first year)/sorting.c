#include "sortingh.h"//���������� ����������� �������

clock_t sorting1(){//������� ���������� ������� �3
    long int i, j, kk, sw;//������������� ������
    rewriting();//������������� � ����� ����� � ������ ������� ����������
    clock_t time_start, time_stop;
    time_start = clock();//������� �����
    for (kk=0; kk<P; kk++){//���� ��� �������
    for (j=1; j<N+1; j++){
        sum[j]=0;
        for (i=0; i<M; i++)
                sum[j]+=a[kk][i][j];} // ���������� ������� ��� ��������� ��������
    for (i=2;i<=N;i++){//������� ����������
        sum[0]=sum[i];//������� �-���� �������� � �������
        for (sw=0; sw<M; sw++){//����, ���� ����������� ������� �������� �� ������
                    a[kk][sw][0]=a[kk][sw][i];
                }
        j=i;
        while(sum[0]<sum[j-1]){
            sum[j]=sum[j-1];
            for (sw=0; sw<M; sw++){
                    a[kk][sw][j]=a[kk][sw][j-1];
                }
            j=j-1;}
        sum[j]=sum[0];
        for (sw=0; sw<M; sw++){
                    a[kk][sw][j]=a[kk][sw][0];
                }
    }
        sum[j]=sum[0];
        for (sw=0; sw<M; sw++){
                    a[kk][sw][0]=a[kk][sw][i];
                }

        }
        time_stop = clock();//��������� �����
        rewriting2();//������� � ���������� ����� � ������ "� ���'����
    return time_stop - time_start;}


clock_t sorting2(){//������� ���������� ������� ������ �5
    long int min, s, i, Amin[M], imin, sw, kk, j;//������������� ������
    clock_t time_start, time_stop;
    time_start = clock();//������� �����
    for (kk=0; kk<P; kk++){//���� ��� �������
    for (j=0; j<N; j++){
        Sum[j]=0;
        for (i=0; i<M; i++)
                Sum[j]+=A[kk][i][j];} // ���������� ������� ��� ��������� ��������
    for(s=0;s<N-1;s++){
        min=Sum[s];//�����*������� �����
        imin=s;//�����*������� �������
            if(Sum[i]<min){//������ �����
        for(i=(s+1);i<N;i++){//������ ������ � ������ ��������� ���������������
                min=Sum[i];
                imin=i;
                for (sw=0; sw<M; sw++){
                        Amin[sw]=A[kk][sw][i];
                    }
                }}
            if(imin!=s){
                Sum[imin]=Sum[s];
                Sum[s]=min;
                for (sw=0; sw<M; sw++){
                        A[kk][sw][imin]=A[kk][sw][s];
                        A[kk][sw][s]=Amin[sw];
                    }
                }

        }}
     time_stop = clock();//����� �����
return time_stop - time_start;}//��������� ������ � ���


clock_t sorting3(){//������� ���������� ����������
long int R, B, D, kk, i, j;//������������� ������
 clock_t time_start, time_stop;
    time_start = clock();//������� �����
for (kk=0; kk<P; kk++){//���� ��� �������
    for (j=0; j<N; j++){
        Sum[j]=0;
        for (i=0; i<M; i++)
                Sum[j]+=A[kk][i][j];} // ���������� ������� ��� ��������� ��������
                 for (R=N-1; R>=1; R--){//
        for (j=0; j<=R-1; j++){//������ �� �������������
            if (Sum[j]>Sum[j+1]){//��������� �����
                    B = Sum[j];
                    Sum[j] = Sum[j+1];
                    Sum[j+1] = B;//������
                    for (i=0; i<M; i++){
                        D = A[kk][i][j];
                        A[kk][i][j] =  A[kk][i][j+1];
                        A[kk][i][j+1] = D;
                    }
            }
        }
    }}
    time_stop = clock();//����� �����
    return time_stop - time_start;}//��������� ������ � ���



clock_t sorting4(){//������� ������� ���������� ������� �����
long int i,j,kk;//���������� ����
clock_t time_start, time_stop;
time_start = clock();
for (kk=0; kk<P; kk++){//������ �� ��������
    for (int j=0; j<N; j++){
        Sum[j]=0;
        for (i=0; i<M; i++)
                Sum[j]+=A[kk][i][j];} // ���������� ������� ��� ��������� ��������
void qsort(int l,int r){//���� ������� ���������� �����
long int x,tmp,z;
x=Sum[(l+r)/2];//������ �������� �������
i=l; j=r;
while(i<=j){//��������� ���� �������
    while(Sum[i]<x)
    i+=1;
    while(Sum[j]>x)
    j-=1;
if(i<=j){//����� �������
    tmp=Sum[i];
    Sum[i]=Sum[j];
    Sum[j]=tmp;
    for(z=0;z<M;z++){//������������� ���������
        tmp=A[kk][z][i];
        A[kk][z][i]=A[kk][z][j];
        A[kk][z][j]=tmp;}
    i+=1;
    j-=1;
    }
}
if(l<j)//����������� ������
    qsort(l,j);
if(i<r)
    qsort(i,r);
}
qsort(0,N-1);//������ ������� ����������
}time_stop = clock();//������� �����
return time_stop - time_start;}

clock_t sortvec1(){//���������� ������� �������� �3 �������
    long int i, j;
    rewritevec();//��������� � ����� ������ ��� ��������� ���*���
    clock_t time_start, time_stop;
    time_start = clock();
    for (i=2;i<=M*N;i++){
        vec1[0]=vec1[i];
        j=i;
        while(vec1[0]<vec1[j-1]){
            vec1[j]=vec1[j-1];
            j=j-1;}
        vec1[j]=vec1[0];
    }
        vec1[j]=vec1[0];
        time_stop = clock();
        rewritevec2();//��������� ����� � ������ � ����������� � 0
return P*(time_stop - time_start);}//�������� ��� ����������� �������� � �����

clock_t sortvec2(){ //���������� ������� �5 �������
    long int min, s, i, imin;
    clock_t time_start, time_stop;
    time_start = clock();
    for(s=0;s<M*N-1;s++){
        min=vec[s];
        imin=s;
        for(i=(s+1);i<M*N;i++){
            if(vec[i]<min){
                min=vec[i];
                imin=i;
                }}
            if(imin!=s){
                vec[imin]=vec[s];
                vec[s]=min;}
        }
     time_stop = clock();
return P*(time_stop - time_start);}//�������� ��� ����������� �������� � �����

clock_t sortvec3(){//���������� ������ �������
long int R, B, j;
clock_t time_start, time_stop;
time_start = clock();
for (R=M*N-1; R>=1; R--){
        for (j=0; j<=R-1; j++){
            if (vec[j]>vec[j+1]){
                    B = vec[j];
                    vec[j] = vec[j+1];
                    vec[j+1] = B;
            }
        }
    }
    time_stop = clock();
return P*(time_stop - time_start);}//�������� ��� ����������� �������� � �����

clock_t sortvec4(){//������ ���������� ������� ������
long int i,j;
clock_t time_start, time_stop;
time_start = clock();
void qsort(int l,int r){//���������� ������� �����
int x,tmp;
x=vec[(l+r)/2];
i=l; j=r;
while(i<=j){
    while(vec[i]<x)
    i+=1;
    while(vec[j]>x)
    j-=1;
if(i<=j){
    tmp=vec[i];
    vec[i]=vec[j];
    vec[j]=tmp;
    i+=1;
    j-=1;
    }
}
if(l<j)
    qsort(l,j);
if(i<r)
    qsort(i,r);
}
qsort(0,M*N-1);
time_stop = clock();
return P*(time_stop - time_start);}//�������� ��� ����������� �������� � �����
