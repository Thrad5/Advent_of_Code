// AoC_2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
int main()
{
    
    std::fstream file;
    file.open("D:\\!Advent_of_Code\\2023\\day_2\\input.txt", std::ios::in);
    if (file.is_open()) {
        std::string tp;
        int total = 0;
        int iterator = 0;
        while (getline(file, tp)) {// goes through each line which is a game
            iterator += 1;
            int blue = 0;
            int red = 0;
            int green = 0;
            int temp;
            std::string game;
            std::istringstream games(tp);
            int power = 0;
            while (getline(games, game, ':')) {//gets the game from the line
            
                if (game.length()>8) {
                    std::string drawn;
                    std::istringstream drawns(game);
                    while (getline(drawns, drawn, ';')) {// gets the draws from the game
                        std::string block;
                        std::istringstream blocks(drawn);
                        while (getline(blocks, block, ',')) {// seperates each draw
                            std::string num;
                            std::istringstream nums(block);
                            int it2 = 0;
                            while (getline(nums, num, ' ')) {// seperates the numbers out
                                if (it2 % 3 == 0) {}
                                else if (it2 % 3 == 1) {
                                    temp = std::stoi(num);
                                }
                                else {
                                    if (num == "red" and temp > red) {
                                        red = temp;
                                    }
                                    else if (num == "blue" and temp > blue) {
                                        blue = temp;
                                    }
                                    else if (num == "green" and temp > green) {
                                        green = temp;
                                    }
                                }
                                
                                it2++;
                            }
                            
                        }
                    }
                }
            }
            power = red * blue * green;
            total += power;
            file.close();
        }
        std::cout << total;
    }
    else {
        std::cout << "File not open,";
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
