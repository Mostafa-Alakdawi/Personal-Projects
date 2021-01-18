#include <iostream>
#include <string>

#include "format.h"

using std::string;

// TODO: Complete this helper function
// INPUT: Long int measuring seconds
// OUTPUT: HH:MM:SS
// REMOVE: [[maybe_unused]] once you define the function
string Format::ElapsedTime(long seconds) { 
    string hour, minute, second, output;
    hour = std::to_string(seconds/(3600));
    minute = std::to_string(seconds/(60));
    second = std::to_string(seconds%(60));    
    output = hour + ":"+minute+":"+second;

    return output; 
    }