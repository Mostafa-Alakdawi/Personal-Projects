#ifndef PROCESSOR_H
#define PROCESSOR_H

class Processor {
 public:
  //Processor();
  float Utilization();  // TODO: See src/processor.cpp
  void User(long u){user = u;}
  void Nice(long n){nice = n;}
  void System(long s){system = s;}
  void Idle(long i){idle = i;}
  void Iowait(long io){iowait = io;}
  void Irq(long ir){irq = ir;}
  void Softirq(long so){softirq = so;}
  void Steal(long st){steal = st;}
  void Guest(long g){guest = g;}
  void Guest_nice(long gn){guest_nice = gn;}

  // TODO: Declare any necessary private members
 private:
    long user;
    long nice;
    long system;
    long idle;
    long iowait;
    long irq;
    long softirq;
    long steal;
    long guest;
    long guest_nice;
};

#endif