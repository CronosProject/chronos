#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void getCpuUsage()
{
    void cpuUsage(int *total_jiffies, int *work_jiffies)
    {
      int i; int user; int nice;
      int sys; int idle; int iowait;
      int irq; int softirq;

      char junk[20];
      char info[100];

      FILE *file;
      file = fopen("/proc/stat", "r");
      fgets(info, 100, file);
      fclose(file);

      for(i = 0; i < sizeof(info); i++)
      {
        if(info[i] == ' ' && info[i+1] == ' ')
        {
          info[i] = '.';
        }
      }

      sscanf(info, "%s %d %d %d %d %d %d %d",junk,&user,&nice,&sys,&idle,&iowait,&irq,&softirq);

      *total_jiffies = user+nice+sys+idle+iowait+irq+softirq;
      *work_jiffies = user+nice+sys;
    }

    int total_jiffies1, total_jiffies2;
    int work_jiffies1, work_jiffies2;

    cpuUsage(&total_jiffies1, &work_jiffies1);
    sleep(5);
    cpuUsage(&total_jiffies2, &work_jiffies2);

    double work_over_period = work_jiffies2 - work_jiffies1;
    double total_over_period = total_jiffies2 - total_jiffies1;
    double cpu = work_over_period / total_over_period * 100;

    printf("%f%\n", cpu);
}
int main()
{
    getCpuUsage();
}
