// AoC_3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>

int main()
{
    char CharArray[140][140];
    bool HasChecked[140][140] = {0};
    std::fstream file;
    file.open("D:\\!Advent_of_Code\\2023\\day_3\\input.txt", std::ios::in);
    if (file.is_open()) {
        int i = 0;
        std::string line;
        while (getline(file, line)) {
            for (int j = 0; j < line.length(); j++) {
                CharArray[i][j] = line[j];
            }
            i++;
        }
        file.close();
    }
    int special = 0;
    std::string notSpecial = "0123456789.#%+/=@$-&";
    std::string notNum = "*#%+/=@$-&.";
    for (int i = 0; i < notNum.length(); i++) {
        std::cout << notNum[i] << " " << notNum.find(notNum[i]) << " " << notSpecial.find(notNum[i]) << "\n";
    }
    for (int i = 0; i < notSpecial.length(); i++) {
        std::cout << notSpecial[i] << " " << notNum.find(notSpecial[i]) << " " << notSpecial.find(notSpecial[i]) << "\n";
    }
    std::string typChar = "";
    for (int i = 0; i < 140; i++) {
        for (int j = 0; j < 140; j++) {
            if (typChar.find(CharArray[i][j]) == 4294967295) {
                typChar += CharArray[i][j];
            }
            
        }
    }
    std::cout << "The characters are: " << typChar << "\n";
    int total = 0;
    for (int i = 0; i < 140; i++) {
        for (int j = 0; j < 140; j++) {
            if (notSpecial.find(CharArray[i][j]) == 4294967295) {
                special++;
                std::cout << "Special number: " << special;
                std::cout << "    Special character: " << CharArray[i][j] << "\n";
                std::string normal1 = "";
                std::string normal2 = "";
                int value1 = 0;
                int value2 = 0;
                int numofval = 0;
                for (int k = -1; k < 2; k++) {
                    
                    for (int l = -1; l < 2; l++){ 
                        int rowloc = i + k;
                        int colloc = j + l;
                        
                        if ( (rowloc) >= 0 and rowloc < 140 and 0 <= (colloc) < 140) {
                            
                            if (notNum.find(CharArray[rowloc][colloc]) == 4294967295 and not HasChecked[rowloc][colloc]) {
                                if (numofval == 0) {
                                    normal1 = CharArray[rowloc][colloc];
                                }
                                else if (numofval == 1) {
                                    normal2 = CharArray[rowloc][colloc];
                                }
                                
                                
                                if (colloc - 1 >= 0 and notNum.find(CharArray[rowloc][colloc - 1]) == 4294967295) {
                                    if (numofval == 0) {
                                        normal1 = CharArray[rowloc][colloc - 1] + normal1;
                                    }
                                    else if (numofval == 1) {
                                        normal2 = CharArray[rowloc][colloc - 1] + normal2;
                                    }
                                    
                                    HasChecked[rowloc][colloc - 1] = true;
                                    if (not (colloc - 2 < 0) and notNum.find(CharArray[rowloc][colloc - 2]) == 4294967295) {
                                        if (numofval == 0) {
                                            normal1 = CharArray[rowloc][colloc - 2] + normal1;
                                        }
                                        else if (numofval == 1) {
                                            normal2 = CharArray[rowloc][colloc - 2] + normal2;
                                        }
                                        
                                        HasChecked[rowloc][colloc - 2] = true;

                                    }
                                }
                                if ((colloc + 1) < 140 and notNum.find(CharArray[rowloc][colloc + 1]) == 4294967295) {
                                    if (numofval == 0) {
                                        normal1 += CharArray[rowloc][colloc + 1];
                                    }
                                    else if (numofval == 1) {
                                        normal2 += CharArray[rowloc][colloc + 1];
                                    }
                                    
                                    HasChecked[rowloc][colloc + 1] = true;
                                    if ((colloc + 2) < 140 and notNum.find(CharArray[rowloc][colloc + 2]) == 4294967295) {
                                        if (numofval == 0) {
                                            normal1 += CharArray[rowloc][colloc + 2];
                                        }
                                        else if (numofval == 1) {
                                            normal2 += CharArray[rowloc][colloc + 2];
                                        }
                                        
                                        HasChecked[rowloc][colloc + 2] = true;

                                    }
                                }
                                //std::cout << CharArray[rowloc][colloc] << ", " << normal << ", " << value << "\n";
                                numofval++;
                            }
                            HasChecked[rowloc][colloc] = true;
                            
                        
                            
                        }
                
                        
                    }
                    
                }
                if (normal1 != "" and normal2 != "" and numofval == 2) {
                    value1 = std::stoi(normal1);
                    value2 = std::stoi(normal2);
                    total += value1 * value2;
                    std::cout << value1 << ", " << value2 << "\n";
                }
                
            }
            else {}
            
        }
        //std::cout << "\n";
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
