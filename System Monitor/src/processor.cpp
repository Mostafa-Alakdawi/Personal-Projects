#include "processor.h"

// TODO: Return the aggregate CPU utilization
float Processor::Utilization() { 
    float total, idleTotal, nonIdle, utilization;

    total = user + nice + system+ idle+ iowait+ irq+ softirq+ steal+ guest+ guest_nice;
    idleTotal = idle+ iowait;
    nonIdle = user+ nice+ system+ irq+ softirq+ steal+ guest+ guest_nice;
    utilization = (nonIdle-idleTotal)/total;

    return utilization; 
}

//Processor::Processor() { Utilization(); }
