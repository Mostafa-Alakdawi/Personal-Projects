#include <dirent.h>
#include <unistd.h>
#include <cstddef>
#include <set>
#include <string>
#include <vector>
#include <iostream>

#include "system.h"
#include "process.h"
#include "processor.h"
#include "linux_parser.h"

using namespace LinuxParser;

using std::set;
using std::size_t;
using std::string;
using std::vector;

// TODO: Return the system's CPU
Processor& System::Cpu() {
    long user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice;
    string cpuN, line;

    std::ifstream stream(kProcDirectory + kStatusFilename);

    if (stream.is_open()) {
        std::getline(stream, line);
        std::istringstream linestream(line);
        linestream >> cpuN >> user >> nice >> system >> idle; 
        linestream >> iowait >> irq >> softirq >> steal >> guest >> guest_nice;
        }
    
    this->cpu_.User(user);
    this->cpu_.Nice(nice);
    this->cpu_.System(system);
    this->cpu_.Idle(idle);
    this->cpu_.Iowait(iowait);
    this->cpu_.Irq(irq);
    this->cpu_.Softirq(softirq);
    this->cpu_.Steal(steal);
    this->cpu_.Guest(guest);
    this->cpu_.Guest_nice(guest_nice);
    this->cpu_.Utilization();

    return this->cpu_; 
}

// TODO: Return a container composed of the system's processes
vector<Process>& System::Processes() {
    for(int pid :LinuxParser::Pids()){
        Process process(pid);
        this->processes_.push_back(process);
    }
    return this->processes_; 
}

// TODO: Return the system's kernel identifier (string)
std::string System::Kernel() {
    string kernel, os, version, line;

    std::ifstream stream(kProcDirectory + kVersionFilename);

    if (stream.is_open()) {
        std::getline(stream, line);
        std::istringstream linestream(line);
        linestream >> os >> version >> kernel;
        }

    return kernel; 
}

// TODO: Return the system's memory utilization
float System::MemoryUtilization() {
    string text, line;
    float MemTotal, MemFree;

    std::ifstream stream(kProcDirectory + kMeminfoFilename);
    
    while (std::getline(stream, line)) {
        std::istringstream linestream(line);
        linestream >> text;
        
        if(text == "MemTotal:"){
            linestream >> MemTotal;
        }
        else if(text == ("MemFree:")){
            linestream >> MemFree;
        }
        else{
            break;
        }
    }
    
    return ((MemTotal - MemFree)/MemTotal); 
}

// TODO: Return the operating system name
std::string System::OperatingSystem() {
    string os,osVersion , line;
    std::ifstream stream(kOSPath);
    
    while (std::getline(stream, line)) {
        if(line.find("PRETTY_NAME") != string::npos){
            break;
        }
    }

    os = line.substr(13,18);

    return os; 
}

// TODO: Return the number of processes actively running on the system
int System::RunningProcesses() {
    
    string line, text;
    int runningProcesses;

    std::ifstream stream(kProcDirectory + kStatFilename);
    
    while (std::getline(stream, line)) {
        if(line.find("procs_running") != string::npos){
            std::istringstream linestream(line);
            linestream >> text >> runningProcesses;
            break;
        }
    }

    return runningProcesses; 
}

// TODO: Return the total number of processes on the system
int System::TotalProcesses() {
    string line, text;
    int processes;

    std::ifstream stream(kProcDirectory + kStatFilename);
    
    while (std::getline(stream, line)) {
        if(line.find("processes") != string::npos){
            std::istringstream linestream(line);
            linestream >> text >> processes;
        }
    }

    return processes;
}

// TODO: Return the number of seconds since the system started running
long int System::UpTime() {
    string line;
    int upTime;

    std::ifstream stream(kProcDirectory + kUptimeFilename);
    
    if (stream.is_open()) {
        std::getline(stream, line);
        std::istringstream linestream(line);
        linestream >> upTime;
    }

    return upTime; 
}

long int System::IdleTime() {
    string line, text;
    int idleTime;

    std::ifstream stream(kProcDirectory + kUptimeFilename);
    
    if (stream.is_open()) {
        std::getline(stream, line);
        std::istringstream linestream(line);
        linestream >> text >> idleTime;
    }

    return idleTime; 
}
