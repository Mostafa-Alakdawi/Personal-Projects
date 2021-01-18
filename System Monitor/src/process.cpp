#include <unistd.h>
#include <cctype>
#include <sstream>
#include <string>
#include <vector>

#include "process.h"
#include "linux_parser.h"
#include "format.h"
#include "system.h"

using namespace LinuxParser;
using namespace Format;

using std::string;
using std::to_string;
using std::vector;

// TODO: Return this process's ID
int Process::Pid() { 
    return Pid_; 
}

long Process::Uid() { 
    string line, text; 
    long uid;

    std::ifstream stream(kProcDirectory + std::to_string(this->Pid_) + kStatusFilename);
    
    while (std::getline(stream, line)) {
        if(line.find("Uid:") != string::npos){
            std::istringstream linestream(line);
            linestream >> text >> uid;
            break;
        }
    }
    this->Uid_ = uid;

    return this->Uid_;
}

// TODO: Return this process's CPU utilization
float Process::CpuUtilization() { 
    string line, text, command;
    System system;
    float seconds, utime, stime, cutime, cstime, starttime, totaltime;

    std::ifstream stream(kProcDirectory + std::to_string(this->Pid_) + kStatFilename);

    if (stream.is_open()) {
        std::getline(stream, line);
        std::istringstream linestream(line);
        for (int count = 0; count < 12; count++)
            linestream >> text;
        linestream >> utime >> stime >> cutime >> cstime;

        for (int count = 0; count < 4; count++)
            linestream >> text;
        linestream >> starttime;
    }

    totaltime = stime + utime + cutime + cstime;
    seconds = system.UpTime() - (starttime/sysconf(_SC_CLK_TCK));
    this->CpuUtilization_ = 100*((totaltime/sysconf(_SC_CLK_TCK))/seconds);

    return this->CpuUtilization_; 
}

// TODO: Return the command that generated this process
string Process::Command() { 
    string line;

    std::ifstream stream(kProcDirectory + std::to_string(this->Pid_) + kCmdlineFilename);

    if (stream.is_open()) {
        std::getline(stream, line);
        std::istringstream linestream(line);
        linestream >> this->Command_;
        }

    return this->Command_; 
}

// TODO: Return this process's memory utilization
string Process::Ram() {     
    string line, text;
    long int VmSize;

    std::ifstream stream(kProcDirectory + std::to_string(this->Pid_) + kStatusFilename);
    
    while (std::getline(stream, line)) {
        if(line.find("VmSize:") != string::npos){
            std::istringstream linestream(line);
            linestream >> text >> VmSize;
            break;
        }
    }

    this->Ram_ = std::to_string(VmSize/1024);

    return this->Ram_; 
}
// TODO: Return the user (name) that generated this process
string Process::User() { 
    string line, text, uid;

    std::ifstream stream(kProcDirectory + std::to_string(this->Pid_) + kStatusFilename);
    
    while (std::getline(stream, line)) {
        if(line.find("Uid:") != string::npos){
            std::istringstream linestream(line);
            linestream >> text >> uid;
            break;
        }
    }

    stream.close();
    std::ifstream stream_2(kPasswordPath);
    
    while (std::getline(stream_2, line)) {
        if(line.find(uid) != string::npos){
            this->User_ = line.substr(0,line.find(":"));
            break;
        }
    }

    return this->User_; 
}

// TODO: Return the age of this process (in seconds)
long int Process::UpTime() {     
    string line, text, command;

    std::ifstream stream(kProcDirectory + std::to_string(this->Pid_) + kStatFilename);

    if (stream.is_open()) {
        std::getline(stream, line);
        std::istringstream linestream(line);
        for (int count = 0; count < 21; count++)
            linestream >> text;
        linestream >>this->UpTime_;
        }
    this->UpTime_ /= sysconf(_SC_CLK_TCK);

    return this->UpTime_; 
}

// TODO: Overload the "less than" comparison operator for Process objects
// REMOVE: [[maybe_unused]] once you define the function
bool Process::operator<(Process const& process) const { 

    if(this->CpuUtilization_ < process.CpuUtilization_)
        return true;
    else
        return false;
     
}