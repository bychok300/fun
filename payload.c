#include <stdio.h>
#include <stdlib.h>

int main()
{

	FILE *fp;


    if (( fp = fopen("C:/Windows/System32/drivers/etc/hosts", "a")) != NULL)
  	    {
    		fprintf(fp, "127.0.0.1 vk.com");
  	    }
    else
	    printf("Не удалось открыть файл");


    fclose(fp);
    return 0;
}
