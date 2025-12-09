// AoC_day_4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
bool find_if_present(std::string input, std::string key[10][211], int index) {
    for (int i = 0; i < 10; i++) {
        if (input == key[i][index]) {
            return true;
        }
    }
    return false;
}

int num_wins(std::string win[10][211], std::string drawn[25][211],int index) {
    int wins = 0;
    for (int j = 0; j < 25; j++) {
        if (find_if_present(drawn[j][index], win,index)) {
            wins++;
        }
    }
    return wins;
}

int main()
{
    std::fstream file;
    std::string allWins[10][211] = { "" };
    std::string allDrawn[25][211] = { "" };
    int numberDrawn[211];
    std::fill_n(numberDrawn, 211, 1);
    file.open("D:\\!Advent_of_Code\\2023\\day_4\\input.txt", std::ios::in);
    
    int total = 0;
    int startGap = 10;
    int gapToDrawn = 42;
    int runs = 0;
    if (file.is_open()) {
        std::string tp;
        while (getline(file, tp)) {
            std::string winningNums[10] = { "" };
            std::string drawnNums[25] = {};
            int numOfWins = 0;
            int points = 0;
            for (int i = 0; i < 10; i++) {
                
                std::string temp = "";
                temp += tp[startGap + i * 3];
                temp += tp[startGap + i * 3 + 1];
                allWins[i][runs] = temp;
            }
            for (int i = 0; i < 25; i++) {
                std::string temp = "";
                temp += tp[gapToDrawn + i * 3];
                temp += tp[gapToDrawn + i * 3 + 1];
                allDrawn[i][runs] = temp;
            }
            runs++;
        }
        file.close();
    }
    for (int i = 0; i < 211; i++) {
        std::cout << numberDrawn[i] << ",";
    }
    std::cout << "\n";
    for (int i = 0; i < 211; i++) {
        int numWins = 0;
        numWins = num_wins(allWins, allDrawn,i);
        for (int j = 0; j < numWins; j++) {
            numberDrawn[i + j + 1] += numberDrawn[i];
        }
        total += numberDrawn[i];
        //std::cout << numberDrawn[i] << "\n";

    }
    std::cout << total;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
