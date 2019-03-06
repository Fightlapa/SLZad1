// JezykiSkryptowe1C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <time.h>
#include <fstream>
#include <vector>
#include <sstream>
#include <iostream>

#define SIZE 0x1ffff

std::vector<std::string> split(const std::string& s, char delimiter)
{
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter))
    {
        tokens.push_back(token);
    }
    return tokens;
}

std::string my_oct(int value)
{
    std::string octValue = "";
    std::string octPrefix = "";
    if (value < 0)
    {
        octPrefix = "-0o";
        value = -value;
    }
    else if (value > 0)
        octPrefix = "0o";
    else
        return "0o0";
    while (value > 0)
    {
        std::string character = std::to_string(value & 0b111);
        value = value >> 3;
        octValue = character + octValue;
    }
    return (octPrefix.append(octValue));

}

double measure()
{
    double emptyLoopStart, emptyLoopEnd, loopStart, loopEnd;
    emptyLoopStart = clock();
    for (int i = -SIZE; i < SIZE; i++)
    {
        std::string this_is_to_avoid_negative_time = "Problem exists probably because of the cycles required to perform both loops and it occurs, that empty one executes slower.";
    }
    emptyLoopEnd = clock();
    loopStart = clock();
    for (int i = -SIZE; i < SIZE; i++)
    {
        std::string this_is_to_avoid_negative_time = "Problem exists probably because of the cycles required to perform both loops and it occurs, that empty one executes slower.";
        my_oct(i);
    }
    loopEnd = clock();
    return (loopEnd - loopStart) - (emptyLoopEnd - emptyLoopStart);
}

void test()
{
    std::string wholeFile;
    std::ifstream nameFileout;

    nameFileout.open("TestData.txt");
    std::getline(nameFileout, wholeFile);
    std::vector<std::string> results = split(wholeFile, ',');
    for (int i = 0; i < SIZE; i+=2)
    {
        if (my_oct(atoi(results[i].c_str())) != results[i + 1])
            std::cout << "Error";
    }
}

int main()
{
    //test();
    std::cout << "Precyzja to:" << 1.0 / CLOCKS_PER_SEC << std::endl;
    double clocks = measure();
    std::cout << clocks * 1 / CLOCKS_PER_SEC;
    return 0;
}

