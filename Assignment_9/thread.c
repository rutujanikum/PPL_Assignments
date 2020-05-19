#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>  //Header file for sleep(). man 3 sleep for details. 
#include <pthread.h>
int count; 
int sec = 0;
int min = 0;
int hrs = 0;
int isMinUpd = 0;
int isHrUpd = 0;
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
void *CalcSec(void *vargp) 
{ 
	while(1){
		if(isMinUpd || isHrUpd) {
			pthread_mutex_lock(&mutex1);
		}
		else {
			sleep(1); 
			sec++;
			printf("%d:%d:%d\n",hrs,min,sec);
			if(sec == 59) {
				isMinUpd = 1;
				sec = 0;
			}
		}
		pthread_mutex_unlock(&mutex1);
	} 
	return NULL; 
} 

void *CalcMin(void *vargp) 
{ 
    while(1){
		if(!isMinUpd) {
			pthread_mutex_lock(&mutex1);
		}
		else {
			min++;
			isMinUpd = 0;			
			if(min == 59) {
				isHrUpd = 1;
				min = 0;
			}
		}
		pthread_mutex_unlock(&mutex1);
	} 
	return NULL; 
} 

void *CalcHrs(void *vargp) 
{ 
    while(1){
		if(!isHrUpd) {
			pthread_mutex_lock(&mutex1);
		}
		else {
			hrs++;
			isHrUpd = 0;
			if(hrs == 23) {
				hrs = 0;
			}
		}
		pthread_mutex_unlock(&mutex1);
	} 
	return NULL; 
} 

int main() 
{ 
	pthread_t th_sec, th_min, th_hr; 
	int data = 10;

	// ---------to get current time--------- 
	time_t s; 
	struct tm* current_time; 

	s = time(NULL); 

	current_time = localtime(&s); 
	sec = current_time->tm_sec;
	min = current_time->tm_min;
	hrs = current_time->tm_hour;

	printf("H:M:S\n"); 
	pthread_create(&th_sec, NULL, CalcSec, &data);
	pthread_create(&th_min, NULL, CalcMin, &data);
	pthread_create(&th_hr, NULL, CalcHrs, &data);
	pthread_join(th_sec, NULL); 
	pthread_join(th_min, NULL); 
	pthread_join(th_hr, NULL); 
	pthread_exit(NULL);
	
}
