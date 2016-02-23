#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>

void getCpuUsage(int& total_jiffies, int& work_jiffies)
{
    std::string junk;
    int user;
    int nice;
    int sys;
    int idle;
    int iowait;
    int irq;
    int softirq;

    std::ifstream file("/proc/stat");
    file >> junk;
    file >> user;
    file >> nice;
    file >> sys;
    file >> idle;
    file >> iowait;
    file >> irq;
    file >> softirq;
    file.close();

    total_jiffies = user+nice+sys+idle+iowait+irq+softirq;
    work_jiffies = user+nice+sys;
}
int main()
{
    int total_jiffies1, total_jiffies2;
    int work_jiffies1, work_jiffies2;

    getCpuUsage(total_jiffies1, work_jiffies1);
    sleep(5);
    getCpuUsage(total_jiffies2, work_jiffies2);

    double work_over_period = work_jiffies2 - work_jiffies1;
    double total_over_period = total_jiffies2 - total_jiffies1;
    double cpu = work_over_period / total_over_period * 100;

    std::cout << cpu << "%" << std::endl;

}
