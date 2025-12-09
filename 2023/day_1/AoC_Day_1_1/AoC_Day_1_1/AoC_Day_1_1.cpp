// AoC_Day_1_1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
int main()
{
    std::fstream file;
    file.open("D:\\!Advent_of_Code\\2023\\day_1\\input.txt", std::ios::in);
    std::cout << "Hello World" << "\n";
    std::cout << file.is_open() << "\n";
    if (file.is_open()) {
        std::string tp;
        int total = 0;
        while (getline(file, tp)) {
            int num;
            int tens = 0;

            // Need strings of length 3(one,two,six); 4(zero,four,five,nine); 5(three,seven,eight)
            for (int i = 0; i < tp.length(); i++) {
                std::string len3str = "aaa";
                std::string len4str = "aaaa";
                std::string len5str = "aaaaa";
                if (i > 1) {
                    len3str = tp.substr(i - 2, 3);
                }
                else {
                    len3str = "aaa";
                }
                if (i > 2) {
                    len4str = tp.substr(i - 3, 4);
                }
                else {
                    len4str = "aaaa";
                }
                if (i > 3) {
                    len5str = tp.substr(i - 4, 5);
                }
                else {
                    len5str = "aaaaa";
                }
                char temp = tp[i];
                if (temp == '0' or len3str == "zero"){
                    tens = 0;
                    break;
                }
                else if (temp == '1' or len3str == "one") {
                    tens = 10;
                    break;
                }
                else if (temp == '2' or len3str == "two") {
                    tens = 20;
                    break;
                }
                else if (temp == '3' or len5str == "three") {
                    tens = 30;
                    break;
                }
                else if (temp == '4' or len4str == "four") {
                    tens = 40;
                    std::cout << len4str<<"\n";

                    break;
                }
                else if (temp == '5' or len4str == "five") {
                    tens = 50;
                    break;
                }
                else if (temp == '6' or len3str == "six") {
                    tens = 60;
                    break;
                }else if (temp == '7' or len5str == "seven") {
                    tens = 70;
                    break;
                }
                else if (temp == '8' or len5str == "eight") {
                    tens = 80;
                    break;
                }
                else if (temp == '9' or len4str == "nine") {
                    tens = 90;
                    std::cout << len4str << "," << len5str << ",\n";
                    break;
                    }
                
            }

            int ones = 0;
            for (int i = 0; i < tp.length(); i++) {
                std::string len3str = "aaa";
                std::string len4str = "aaaa";
                std::string len5str = "aaaaa";
                if (i > 1) {
                    len3str = tp.substr(i-2,3);
                }
                else {
                    len3str = "aaa";
                }
                if (i > 2) {
                    len4str = tp.substr(i - 3, 4);
                }
                else {
                    len4str = "aaaa";
                }
                if (i > 3) {
                    len5str = tp.substr(i - 4, 5);
                }
                else {
                    len5str = "aaaaa";
                }
                char temp = tp[i];
                if (temp == '0' or len4str == "zero") {
                    ones = 0;
                    
                }
                else if (temp == '1' or len3str == "one") {
                    ones = 1;
                }
                else if (temp == '2' or len3str == "two") {
                    ones = 2;
                }
                else if (temp == '3' or len5str == "three") {
                    ones = 3;
                }
                else if (temp == '4' or len4str == "four") {
                    ones = 4;
                }
                else if (temp == '5' or len4str == "five") {
                    ones = 5;
                }
                else if (temp == '6' or len3str == "six") {
                    ones = 6;
                }
                else if (temp == '7' or len5str == "seven") {
                    ones = 7;
                }
                else if (temp == '8' or len5str == "eight") {
                    ones = 8;
                }
                else if (temp == '9' or len4str == "nine") {
                    ones = 9;
                }
            }
            num = tens + ones;
            total += num;
            std::cout << num << "\n";
        }
        std::cout << "The total is: " << total;
        file.close();
    }
    else {
        std::cout << "File not open";
    }
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
