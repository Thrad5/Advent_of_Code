// AoC_8.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>


class Location {
private:
    std::string leftChild;
    std::string rightChild;
public:
    Location();
    void setChildren(std::string leftChild,std::string rightChild);
    std::string get_left_child();
    std::string get_right_child();

};
Location::Location(){}
void Location::setChildren(std::string leftChild, std::string rightChild) {
    this->leftChild = leftChild;
    this->rightChild = rightChild;
}
std::string Location::get_left_child() {
    return this->leftChild;
}
std::string Location::get_right_child() {
    return this->rightChild;
}

int main()
{
    std::cout << "Hello World!\n";
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
