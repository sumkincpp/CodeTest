/*
 * Memory Performance Information
 *
 * http://msdn.microsoft.com/en-us/library/windows/desktop/aa965225.aspx
 *  System Memory Performance Information
 *   MEMORYSTATUSEX, PERFORMANCE_INFORMATION
 *  Process Memory Performance Information
 *   PROCESS_MEMORY_COUNTERS
*/
#include <iostream>

#define WIN32_WINNt 0x0500
#define WINVER 0x0500

#include <windows.h>
#include <Psapi.h> // library for link - psapi, PERFORMANCE_INFORMATION, PROCESS_MEMORY_COUNTERS
#include <winbase.h>  // MEMORYSTATUSEX

using std::cout;

long int getFreeMemoryInBytes () {
    MEMORYSTATUSEX ms; // http://msdn.microsoft.com/en-us/library/windows/desktop/aa366770.aspx
    ms.dwLength = sizeof (ms);
    GlobalMemoryStatusEx (&ms);

    return ms.ullAvailPhys;
}

long int getPhysicalAvailable () {
    PERFORMANCE_INFORMATION pi; // http://msdn.microsoft.com/en-us/library/windows/desktop/ms684824.aspx
    ZeroMemory (&pi, sizeof(PERFORMANCE_INFORMATION));

    pi.cb = sizeof(PERFORMANCE_INFORMATION);

    if (GetPerformanceInfo(&pi, sizeof(PERFORMANCE_INFORMATION))) {
        return pi.PhysicalAvailable*pi.PageSize;
    }

    return -1;
}

long int getPeakWorkingSetSizeInBytes () {
    PROCESS_MEMORY_COUNTERS pmc;

    if ( GetProcessMemoryInfo( GetCurrentProcess(), reinterpret_cast<PROCESS_MEMORY_COUNTERS*>(&pmc),
                              sizeof(pmc)) ) {
        return  pmc.PeakWorkingSetSize;
    }

    return -1;
}


int main () {
    cout << "There are " <<(getFreeMemoryInBytes()/1024)/1024 << " Mbs free of Physical Memory" << std::endl;
    cout << "Memory " << (getPhysicalAvailable()/1024)/1024 << std::endl;
    cout << "Peak program size " << getPeakWorkingSetSizeInBytes ()/1024 << "Kbs";

    return 0;
}
