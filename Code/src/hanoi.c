#include <stdio.h>

#define DISK 16

#define other(i,j) (6-(i+j))
#define mov(x,y,z) doit(x,y,z)  /* for instrumentation */

int num[4];
int count;

int mov(n,f,t){
	
	int o;
	
	if(n == 1) {
		num[f]--;
		num[t]++;
		count++;
  }

   o = other(f,t);
   mov(n-1,f,o);
   mov(1,f,t);
   mov(n-1,o,t);
}

void main(void){

   printf("> Starting...\n");
	 num[0] = 0;
   num[1] = DISK;
   num[2] = 0;
   num[3] = 0;
   count  = 0;

   mov(DISK,1,3);
   printf("> %d moves\n", count);
}