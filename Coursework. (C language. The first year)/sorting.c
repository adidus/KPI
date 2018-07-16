#include "sortingh.h"//підключення інтерфейсної частини

clock_t sorting1(){//функція сортування вставки №3
    long int i, j, kk, sw;//ініціалізування змінних
    rewriting();//переписування в інший масив з вільним нулевим стовбчиком
    clock_t time_start, time_stop;
    time_start = clock();//початок виміру
    for (kk=0; kk<P; kk++){//цикл для перерізів
    for (j=1; j<N+1; j++){
        sum[j]=0;
        for (i=0; i<M; i++)
                sum[j]+=a[kk][i][j];} // формування вектора сум відповідних стовпців
    for (i=2;i<=N;i++){//початок сортування
        sum[0]=sum[i];//перепис і-того елемента в нулевий
        for (sw=0; sw<M; sw++){//цикл, який переставляє стовпці відповідно до ключів
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
        time_stop = clock();//закінчення виміру
        rewriting2();//перепис в початковий масив з масиву "з бар'єром
    return time_stop - time_start;}


clock_t sorting2(){//функція сортування методом вибору №5
    long int min, s, i, Amin[M], imin, sw, kk, j;//ініціалізування змінних
    clock_t time_start, time_stop;
    time_start = clock();//початок виміру
    for (kk=0; kk<P; kk++){//цикл для перерізів
    for (j=0; j<N; j++){
        Sum[j]=0;
        for (i=0; i<M; i++)
                Sum[j]+=A[kk][i][j];} // формування вектора сум відповідних стовпців
    for(s=0;s<N-1;s++){
        min=Sum[s];//запам*ятовуємо мінімум
        imin=s;//запам*ятовуємо позицію
            if(Sum[i]<min){//шукаємо мінімум
        for(i=(s+1);i<N;i++){//міняємо місцями з першим елементом невідсортованого
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
     time_stop = clock();//кінець виміру
return time_stop - time_start;}//повертаємо різницю в часі


clock_t sorting3(){//функція сортування бульбашкою
long int R, B, D, kk, i, j;//ініціалізування змінних
 clock_t time_start, time_stop;
    time_start = clock();//початок виміру
for (kk=0; kk<P; kk++){//цикл для перерізів
    for (j=0; j<N; j++){
        Sum[j]=0;
        for (i=0; i<M; i++)
                Sum[j]+=A[kk][i][j];} // формування вектора сум відповідних стовпців
                 for (R=N-1; R>=1; R--){//
        for (j=0; j<=R-1; j++){//прохід по невідсортованій
            if (Sum[j]>Sum[j+1]){//порівнюємо сусідн
                    B = Sum[j];
                    Sum[j] = Sum[j+1];
                    Sum[j+1] = B;//міняємо
                    for (i=0; i<M; i++){
                        D = A[kk][i][j];
                        A[kk][i][j] =  A[kk][i][j+1];
                        A[kk][i][j+1] = D;
                    }
            }
        }
    }}
    time_stop = clock();//кінець виміру
    return time_stop - time_start;}//повертаємо різницю в часі



clock_t sorting4(){//функція виклику сортування методом Хоара
long int i,j,kk;//ініціалізуємо змінні
clock_t time_start, time_stop;
time_start = clock();
for (kk=0; kk<P; kk++){//прохід по перерізах
    for (int j=0; j<N; j++){
        Sum[j]=0;
        for (i=0; i<M; i++)
                Sum[j]+=A[kk][i][j];} // формування вектора сум відповідних стовпців
void qsort(int l,int r){//сама функція сортування Хоара
long int x,tmp,z;
x=Sum[(l+r)/2];//беремо довільний елемент
i=l; j=r;
while(i<=j){//проходимо зліва направо
    while(Sum[i]<x)
    i+=1;
    while(Sum[j]>x)
    j-=1;
if(i<=j){//умова зупинки
    tmp=Sum[i];
    Sum[i]=Sum[j];
    Sum[j]=tmp;
    for(z=0;z<M;z++){//переставляємо стовбчики
        tmp=A[kk][z][i];
        A[kk][z][i]=A[kk][z][j];
        A[kk][z][j]=tmp;}
    i+=1;
    j-=1;
    }
}
if(l<j)//рекурсивний запуск
    qsort(l,j);
if(i<r)
    qsort(i,r);
}
qsort(0,N-1);//запуск функції сортування
}time_stop = clock();//зупинка виміру
return time_stop - time_start;}

clock_t sortvec1(){//сорутвання вектора вставкою №3 вектора
    long int i, j;
    rewritevec();//переписую у інший вектор для звільнення бар*єра
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
        rewritevec2();//переписую назад в вектор з індексацією з 0
return P*(time_stop - time_start);}//повертаю час пропорційно перерізам у масиві

clock_t sortvec2(){ //сортування вибором №5 вектора
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
return P*(time_stop - time_start);}//повертаю час пропорційно перерізам у масиві

clock_t sortvec3(){//сортування обміном вектора
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
return P*(time_stop - time_start);}//повертаю час пропорційно перерізам у масиві

clock_t sortvec4(){//запуск сортування вектора Хоарою
long int i,j;
clock_t time_start, time_stop;
time_start = clock();
void qsort(int l,int r){//сортування методом Хоара
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
return P*(time_stop - time_start);}//повертаю час пропорційно перерізам у масиві
