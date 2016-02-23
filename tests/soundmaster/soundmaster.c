#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>

pid_t create_process(void)
{
	pid_t pid;
	do {
		pid = fork();
	} while((pid == -1) && (errno == EAGAIN));

	return pid;
}

void change_volume(const unsigned short volume)
{
	char percentage[10];
	sprintf(percentage, "%d%%", volume);

	char *args[] = {"amixer", "set", "Master", percentage, NULL};

	if(execv("/usr/bin/amixer", args) == -1) {
		perror("amixer :");
		exit(EXIT_FAILURE);
	}
}

int main(int argc, char *argv[])
{
	unsigned short volume;
	pid_t pid = create_process();

	switch(pid) {
		case -1:
			return EXIT_FAILURE;
			break;
		case 0:
			if(argc > 1)
			{
				if(sscanf(argv[1], "%d", &volume) != EOF)
				{
					if(volume >= 0 && volume <= 100)
					{
						change_volume(volume);
					}
				}
			}
		break;
		default:
			if(wait(NULL) == -1) {
				perror("wait :");
				exit(EXIT_FAILURE);
			}
	}

	return 0;
}