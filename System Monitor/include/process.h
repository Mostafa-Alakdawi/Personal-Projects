#ifndef PROCESS_H
#define PROCESS_H

#include <string>

/*
Basic class for Process representation
It contains relevant attributes as shown below
*/
class Process
{
  // TODO: Declare any necessary private members
 private:
    int Pid_;
    long Uid_;
    std::string User_;
    std::string Command_;
    float CpuUtilization_;
    std::string Ram_;
    long int UpTime_;

 public:
  Process(int pid) : Pid_(pid){};
  int Pid();                               // TODO: See src/process.cpp
  std::string User();                      // TODO: See src/process.cpp
  long Uid();                      
  std::string Command();                   // TODO: See src/process.cpp
  float CpuUtilization();                  // TODO: See src/process.cpp
  std::string Ram();                       // TODO: See src/process.cpp
  long int UpTime();                       // TODO: See src/process.cpp
  bool operator<(Process const& a) const;  // TODO: See src/process.cpp
};

#endif