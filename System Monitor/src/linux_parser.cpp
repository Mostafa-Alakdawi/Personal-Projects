#include <dirent.h>
#include <unistd.h>
#include <string>
#include <vector>
#include <iostream>

#include "linux_parser.h"
#include"system.h"

using std::stof;
using std::string;
using std::to_string;
using std::vector;

// DONE: An example of how to read data from the filesystem
string LinuxParser::OperatingSystem() {
  string line;
  string key;
  string value;
  std::ifstream filestream(kOSPath);
  if (filestream.is_open()) {
    while (std::getline(filestream, line)) {
      std::replace(line.begin(), line.end(), ' ', '_');
      std::replace(line.begin(), line.end(), '=', ' ');
      std::replace(line.begin(), line.end(), '"', ' ');
      std::istringstream linestream(line);
      while (linestream >> key >> value) {
        if (key == "PRETTY_NAME") {
          std::replace(value.begin(), value.end(), '_', ' ');
          return value;
        }
      }
    }
  }
  return value;
}

// DONE: An example of how to read data from the filesystem
string LinuxParser::Kernel() {
  string os, version, kernel;
  string line;
  std::ifstream stream(kProcDirectory + kVersionFilename);
  if (stream.is_open()) {
    std::getline(stream, line);
    std::istringstream linestream(line);
    linestream >> os >> version >> kernel;
  }
  return kernel;
}

// BONUS: Update this to use std::filesystem
vector<int> LinuxParser::Pids() {
  vector<int> pids;
  DIR* directory = opendir(kProcDirectory.c_str());
  struct dirent* file;
  while ((file = readdir(directory)) != nullptr) {
    // Is this a directory?
    if (file->d_type == DT_DIR) {
      // Is every character of the name a digit?
      string filename(file->d_name);
      if (std::all_of(filename.begin(), filename.end(), isdigit)) {
        int pid = stoi(filename);
        pids.push_back(pid);
      }
    }
  }
  closedir(directory);
  return pids;
}

// TODO: Read and return the system memory utilization
float LinuxParser::MemoryUtilization() { 
  System system;
  return system.MemoryUtilization(); 
}

// TODO: Read and return the system uptime
long LinuxParser::UpTime() { 
  System system;
  return system.UpTime(); 
}

// TODO: Read and return the number of jiffies for the system
long LinuxParser::Jiffies() { 
  System system;
  return (system.IdleTime() + system.UpTime()); 
  }

// TODO: Read and return the number of active jiffies for a PID
// REMOVE: [[maybe_unused]] once you define the function
long LinuxParser::ActiveJiffies(int pid) { 
  long  jiffies;
  System system;

  for(Process process: system.Processes()){
    if(process.Pid() == pid){
       jiffies = (process.UpTime()*sysconf(_SC_CLK_TCK));
    }
  }

  return jiffies;
}

// TODO: Read and return the number of active jiffies for the system
long LinuxParser::ActiveJiffies() { 
  System system;
  return system.UpTime(); 
}

// TODO: Read and return the number of idle jiffies for the system
long LinuxParser::IdleJiffies() { 
  System system;
  return system.IdleTime(); 
  }

// TODO: Read and return CPU utilization
vector<string> LinuxParser::CpuUtilization() { 
  System system;
  vector<string> cpuU;

  for (Process cpuN: system.Processes())
    cpuU.push_back(std::to_string(cpuN.CpuUtilization()));

  return cpuU; 
}

// TODO: Read and return the total number of processes
int LinuxParser::TotalProcesses() { 
  System system;
  return system.TotalProcesses(); 
}

// TODO: Read and return the number of running processes
int LinuxParser::RunningProcesses() { 
  System system;
  return system.RunningProcesses(); 
}

// TODO: Read and return the command associated with a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::Command(int pid) { 
  string command;
  System system;

  for(Process process: system.Processes()){
    if(process.Pid() == pid){
       command = process.Command();
    }
  }

  return command;
}

// TODO: Read and return the memory used by a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::Ram(int pid) { 
  string ram;
  System system;

  for(Process process: system.Processes()){
    if(process.Pid() == pid){
       ram = process.Ram();
    }
  }

  return ram;
}

// TODO: Read and return the user ID associated with a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::Uid(int pid) { 
  string uid;
  System system;

  for(Process process: system.Processes()){
    if(process.Pid() == pid){
       uid = process.Uid();
    }
  }

  return uid;
}


// TODO: Read and return the user associated with a process
// REMOVE: [[maybe_unused]] once you define the function
string LinuxParser::User(int pid) { 
  string user;
  System system;

  for(Process process: system.Processes()){
    if(process.Pid() == pid){
       user = process.User();
    }
  }

  return user;
}


// TODO: Read and return the uptime of a process
// REMOVE: [[maybe_unused]] once you define the function
long LinuxParser::UpTime(int pid) { 

  string word, line;
  long seconds = 0;
  std::ifstream statfile(kProcDirectory+to_string(pid)+kStatFilename);
  
  if(statfile.is_open()) {
    std::getline(statfile, line);
    std::istringstream stream(line);
    int word_ix(0);
    while(stream >> word){
      if (word_ix == 21){
        break;
      }
      word_ix++;
    }
    seconds = UpTime() - stof(word)/sysconf(_SC_CLK_TCK);
  }
  return seconds; 
  }