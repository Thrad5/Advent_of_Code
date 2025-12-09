// AoC_5.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <format>

bool find_if_present(std::string input, std::string key[][2], int index, int length) {
    for (int i = 0; i < length; i++) {
        if (input == key[index][i]) {
            return true;
        }
    }
    return false;
}

int find_largest_beneath(unsigned long searchThru[][3], unsigned long toFind, int destSource, int searchLength) {
    int result = 0;
    //std::cout << "\n" << toFind << "\n";
    for (int i = 0; i < searchLength; i++) {
        int offset = toFind - searchThru[i][destSource];
        //std::cout << offset << " " << (0 < offset and offset < searchThru[i][2]) << "\n";
        if ((0 < offset and offset < searchThru[i][2])) {
            //std::cout << "\n";
            return i;
            
        }
        else {
            //std::cout << "in else statement \n";
            result = searchLength;
        }
    }
    //std::cout << result << "\n";
    return result;
}

unsigned long find_next_value(unsigned long searchThru[][3], unsigned long toFind, int destSource,int searchLength) {
    int result;
    unsigned long value;
    result = find_largest_beneath(searchThru, toFind, destSource, searchLength);
    if (result == searchLength) {
        value = toFind;
    }
    else {
        int offset = toFind - searchThru[result][destSource];
        if (offset > searchThru[result][2]) {
            std::cout << result << "\n";
            std::cout << "SOMETHING HAS GONE WRONG " << offset << " vs " << searchThru[result][2] << "\n";
            value = 0;
        }
        else {
            if (destSource == 0) {
                value = (toFind - searchThru[result][destSource]) + searchThru[result][1];
            }
            else {
                value = (toFind - searchThru[result][destSource]) + searchThru[result][0];
            }
        }
    }
    return value;
}

bool is_in_iter(unsigned long seed[][2], unsigned long potentialSeed, int searchLength) {
    bool isIn = false;
    for (int i = 0; i < searchLength; i++) {
        int maxval = seed[i][1] + seed[i][0];
        if ((seed[i][0] <= potentialSeed and potentialSeed <= maxval)) {
            isIn= true;
        }
    }
    return isIn;
}


void printarray(unsigned long arrays[][3], int length) {
    for (int i = 0; i < length; i++) {
        std::cout << arrays[i][0] << " " << arrays[i][1] << " " << arrays[i][2] << "\n";
    }
    std::cout << "\n";
}
void printarray(unsigned long arrays[][2], int length) {
    for (int i = 0; i < length; i++) {
        std::cout << arrays[i][0] << " " << arrays[i][1] << "\n";
    }
    std::cout << "\n";
}

unsigned long seed_to_location(unsigned long seed, unsigned long seed2soil[][3], unsigned long soil2fert[][3], unsigned long fert2wat[][3], unsigned long wat2light[][3], unsigned long light2temp[][3], unsigned long temp2humid[][3], unsigned long humid2loc[][3]) {
    int destSource = 1;
    unsigned long location = find_next_value(humid2loc, find_next_value(temp2humid, find_next_value(light2temp, find_next_value(wat2light, find_next_value(fert2wat, find_next_value(soil2fert, find_next_value(seed2soil, seed, destSource, 44), destSource, 22), destSource, 40), destSource, 43), destSource, 34), destSource, 45), destSource, 34);
    return location;
}
unsigned long location_to_seed(unsigned long location, unsigned long seed2soil[][3], unsigned long soil2fert[][3], unsigned long fert2wat[][3], unsigned long wat2light[][3], unsigned long light2temp[][3], unsigned long temp2humid[][3], unsigned long humid2loc[][3]) {
    int destSource = 0;
    unsigned long seed = find_next_value(seed2soil, find_next_value(soil2fert, find_next_value(fert2wat, find_next_value(wat2light, find_next_value(light2temp, find_next_value(temp2humid, find_next_value(humid2loc, location, destSource, 34), destSource, 45), destSource, 34), destSource, 43), destSource, 40), destSource, 22), destSource, 44);
    return seed;
}


int main()
{
    const int numClmn = 3;
    unsigned long seed2soil[44][numClmn];//First column is soil values the second is the seed values
    unsigned long soil2fert[22][numClmn];
    unsigned long fert2wat[40][numClmn];
    unsigned long wat2light[43][numClmn];
    unsigned long light2temp[34][numClmn];
    unsigned long temp2humid[45][numClmn];
    unsigned long humid2loc[34][numClmn];
    unsigned long seeds[10][2];
    std::fstream file;
    std::string tp;
    file.open("D:\\!Advent_of_Code\\2023\\day_5\\input.txt", std::ios::in);
    if (file.is_open()) {
        int currentline = 1;
        int block = 0;
        int seedline =0;
        while (getline(file, tp)) {
            std::string temp = "";
            unsigned long temp2 = 0;
            if (currentline == 1) {
                int currentSeed = 0;
                
                for (int i = 0; i < tp.length(); i++) {
                    
                    if (tp[i] =='s' or tp[i] == 'e' or tp[i] == 'd' or tp[i] == ':'){
                        //std::cout << "letter\n";
                    }
                    else if ((tp[i] == ' ' and temp != "")) {
                        
                        temp2 = std::stoul(temp);
                        if (currentSeed % 2 == 0) {
                            seeds[currentSeed/2][0] = temp2;
                        }
                        else {
                            seeds[currentSeed / 2][1] = temp2;
                        }
                        
                        temp = "";
                        currentSeed++;
                    }
                    else if (tp[i] == ' ' and temp == "") {
                        //std::cout << "Space and empty string\n";
                    }
                    else {
                        temp += tp[i];
                        if (i == tp.length() - 1) {
                            temp2 = std::stoul(temp);
                            if (currentSeed % 2 == 0) {
                                seeds[currentSeed / 2][0] = temp2;
                            }
                            else {
                                seeds[currentSeed / 2][1] = temp2;
                            }
                            temp = "";
                        }
                        
                    }
                }
            }
            else if (tp[0] == 's' or tp[0] == 'f' or tp[0] == 'w' or tp[0] == 'l' or tp[0] == 't' or tp[0] == 'h') {
                temp = "";
                temp2 = 0;
                seedline = 0;
                //std::cout << tp[0] << " " << std::format("0x{:x}", (int)tp[0]) << " " << temp << "\n";
            }
            else if (tp == "") {
                block++;
            }
            else {
                if (block == 1) {
                    int counter = 0;
                    
                    for (int i = 0; i < tp.length(); i++) {

                        if ((tp[i] == ' ' and temp != "")) {

                            temp2 = std::stoul(temp);
                            seed2soil[seedline][counter] = temp2;
                            temp = "";
                            counter++;
                            
                        }
                        else if (tp[i] == ' ' and temp == "") {
                            //std::cout << "Space and empty string\n";
                        }
                        else {
                            temp += tp[i];
                            if (i == tp.length() - 1) {
                                temp2 = std::stoul(temp);
                                seed2soil[seedline][counter] = temp2;
                                temp = ""; 
                                if (counter == 2) {
                                    seedline++;
                                }
                            }

                        }
                    }
                }
                else if (block == 2) {
                    int counter = 0;

                    for (int i = 0; i < tp.length(); i++) {

                        if ((tp[i] == ' ' and temp != "")) {

                            temp2 = std::stoul(temp);
                            soil2fert[seedline][counter] = temp2;
                            temp = "";
                            counter++;
                            
                        }
                        else if (tp[i] == ' ' and temp == "") {
                            //std::cout << "Space and empty string\n";
                        }
                        else {
                            temp += tp[i];
                            if (i == tp.length() - 1) {
                                temp2 = std::stoul(temp);
                                soil2fert[seedline][counter] = temp2;
                                temp = "";
                                if (counter == 2) {
                                    seedline++;
                                }
                            }
                        }
                    }
                }
                else if (block == 3) {
                    int counter = 0;

                    for (int i = 0; i < tp.length(); i++) {

                        if ((tp[i] == ' ' and temp != "")) {

                            temp2 = std::stoul(temp);
                            fert2wat[seedline][counter] = temp2;
                            temp = "";
                            counter++;
                            
                        }
                        else if (tp[i] == ' ' and temp == "") {
                            //std::cout << "Space and empty string\n";
                        }
                        else {
                            temp += tp[i];
                            if (i == tp.length() - 1) {
                                temp2 = std::stoul(temp);
                                fert2wat[seedline][counter] = temp2;
                                temp = "";
                                if (counter == 2) {
                                    seedline++;
                                }
                            }
                        }
                    }
                }
                else if (block == 4) {
                    int counter = 0;

                    for (int i = 0; i < tp.length(); i++) {

                        if ((tp[i] == ' ' and temp != "")) {

                            temp2 = std::stoul(temp);
                            wat2light[seedline][counter] = temp2;
                            temp = "";
                            counter++;
                            
                        }
                        else if (tp[i] == ' ' and temp == "") {
                            //std::cout << "Space and empty string\n";
                        }
                        else {
                            temp += tp[i];
                            if (i == tp.length() - 1) {
                                temp2 = std::stoul(temp);
                                wat2light[seedline][counter] = temp2;
                                temp = "";
                                if (counter == 2) {
                                    seedline++;
                                }
                            }
                        }
                    }
                }
                else if (block == 5) {
                    int counter = 0;

                    for (int i = 0; i < tp.length(); i++) {

                        if ((tp[i] == ' ' and temp != "")) {

                            temp2 = std::stoul(temp);
                            light2temp[seedline][counter] = temp2;
                            temp = "";
                            counter++;
                            
                        }
                        else if (tp[i] == ' ' and temp == "") {
                            //std::cout << "Space and empty string\n";
                        }
                        else {
                            temp += tp[i];
                            if (i == tp.length() - 1) {
                                temp2 = std::stoul(temp);
                                light2temp[seedline][counter] = temp2;
                                temp = "";
                                if (counter == 2) {
                                    seedline++;
                                }
                            }
                        }
                    }
                }
                else if (block == 6) {
                int counter = 0;

                for (int i = 0; i < tp.length(); i++) {

                    if ((tp[i] == ' ' and temp != "")) {

                        temp2 = std::stoul(temp);
                        temp2humid[seedline][counter] = temp2;
                        temp = "";
                        counter++;
                        
                    }
                    else if (tp[i] == ' ' and temp == "") {
                        //std::cout << "Space and empty string\n";
                    }
                    else {
                        temp += tp[i];
                        if (i == tp.length() - 1) {
                            temp2 = std::stoul(temp);
                            temp2humid[seedline][counter] = temp2;
                            temp = "";
                            if (counter == 2) {
                                seedline++;
                            }
                        }
                    }
                }
                }
                else if (block == 7) {
                int counter = 0;

                for (int i = 0; i < tp.length(); i++) {

                    if ((tp[i] == ' ' and temp != "")) {

                        temp2 = std::stoul(temp);
                        humid2loc[seedline][counter] = temp2;
                        temp = "";
                        counter++;
                        
                    }
                    else if (tp[i] == ' ' and temp == "") {
                        //std::cout << "Space and empty string\n";
                    }
                    else {
                        temp += tp[i];
                        if (i == tp.length() - 1) {
                            temp2 = std::stoul(temp);
                            humid2loc[seedline][counter] = temp2;
                            temp = "";
                            if (counter == 2) {
                                seedline++;
                            }
                        }
                    }
                }
                }
            }

            currentline++;
        }
        file.close();

    }
    printarray(seeds, 10);
    //printarray(seed2soil, 44);
    //printarray(soil2fert, 22);
    //printarray(fert2wat, 40);
    //printarray(wat2light, 43);
    //printarray(light2temp, 34);
    //printarray(temp2humid, 45);
    //printarray(humid2loc, 34);
    unsigned long minLoc = 0xFFFFFFFF;
    unsigned long potLoc = 0;
    /*
    std::cout << "Initial seed Location Out Seed out init seed == seed out\n";
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 2; j++) {
            unsigned long loc = seed_to_location(seeds[i][j] ,seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2humid, humid2loc);
            unsigned long seed = location_to_seed(loc, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2humid, humid2loc);
            std::cout << seeds[i][j] << " " << loc << " " << seed << " " << is_in_iter(seeds,seed,10) << "\n";
        }
    }
    std::cout << "Initial loc Seed Out Location Out init loc == loc out\n";
    for (int i = 0; i < 100; i++) {
        unsigned long seed = location_to_seed(i, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2humid, humid2loc);
        unsigned long loc = seed_to_location(seed, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2humid, humid2loc);
        std::cout << i << " " << seed << " " << loc << " " << is_in_iter(seeds,seed,10) << "\n";
    }
    */

    for (int i = 0; i < 10; i++) {
        std::cout << "Going Through: " << seeds[i][0] << "\n";
        for (unsigned long j = 0; j <= seeds[i][1]; j++) {
            unsigned long seed = seeds[i][0] + j;
            unsigned long location = seed_to_location(seed, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2humid, humid2loc);
            if (location < minLoc) {
                minLoc = location;
            }
        }
    }
    std::cout << "The Location is: " << minLoc;
    /*
    while (potLoc< 11611183) {
        std::cout << "Trying position: " << potLoc << "\n";
        unsigned long seed = location_to_seed(potLoc, seed2soil, soil2fert, fert2wat, wat2light, light2temp, temp2humid, humid2loc);
        if (is_in_iter(seeds, seed, 10)) {
            std::cout << "The Location is: " << potLoc;
            return 0;
        }
        else {
            potLoc++;
        }
        
    }*/


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
