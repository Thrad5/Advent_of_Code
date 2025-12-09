// AoC_7.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <utility>

int number_in(std::string value, char key) {
    int numOccur = 0;
    for (int i = 0; i < value.length(); i++) {
        if (value[i] == key) {
            numOccur++;
        }
    }
    return numOccur;
}


int card_rank(char a) {
    int rank;
    switch ((int)a)
    {
    case (int)'2':
        rank = 1;
        break;
    case (int)'3':
        rank = 2;
        break;
    case (int)'4':
        rank = 3;
        break;
    case (int)'5':
        rank = 4;
        break;
    case (int)'6':
        rank = 5;
        break;
    case (int)'7':
        rank = 6;
        break;
    case (int)'8':
        rank = 7;
        break;
    case (int)'9':
        rank = 8;
        break;
    case (int)'T':
        rank = 9;
        break;
    case (int)'J':
        rank = 0;
        break;
    case (int)'Q':
        rank = 11;
        break;
    case (int)'K':
        rank = 12;
        break;
    case (int)'A':
        rank = 13;
        break;
    default:
        std::cout << "\n Invalid case" << (char)a << "\n";
        rank = 99;
        break;
    }
    return rank;
}

int hand_rank(char a) {
    int rank;
    switch ((int)a)
    {
    case (int)'H':
        rank = 1;
        break;
    case (int)'N':
        rank = 2;
        break;
    case (int)'W':
        rank = 3;
        break;
    case (int)'T':
        rank = 4;
        break;
    case (int)'U':
        rank = 5;
        break;
    case (int)'O':
        rank = 6;
        break;
    case (int)'F':
        rank = 7;
        break;
    default:
        rank = 99;
        std::cout << "\n Invalid case" << a << "\n";
        break;
    }
    return rank;
}

bool a_bigger_than_b_card(char a, char b) {
    if (card_rank(a) > card_rank(b)) {
        return 1;
    }
    else {
        return 0;
    }

}
bool a_bigger_than_b_hand(char a, char b) {
    if (hand_rank(a) > hand_rank(b)) {
        return 1;
    }
    else {
        return 0;
    }

}

bool a_bigger_than_b_points(std::string a, std::string b) {
    if (hand_rank(a[0]) > hand_rank(b[0])) {
        return 1;
    }
    else if (hand_rank(a[0]) == hand_rank(b[0])) {
        if (card_rank(a[1]) > card_rank(b[1])) {
            return 1;
        }
        else if (card_rank(a[1]) == card_rank(b[1])) {
            if (card_rank(a[2]) > card_rank(b[2])) {
                return 1;
            }
            else if (card_rank(a[2]) == card_rank(b[2])) {
                if (card_rank(a[3]) > card_rank(b[3])) {
                    return 1;
                }
                else if (card_rank(a[3]) == card_rank(b[3])) {
                    if (card_rank(a[4]) > card_rank(b[4])) {
                        return 1;
                    }
                    else if (card_rank(a[4]) == card_rank(b[4])) {
                        if (card_rank(a[5]) > card_rank(b[5])) {
                            return 1;
                        }
                        else { return 0; }
                    }
                    else { return 0; }
                }
                else { return 0; }
            }
            else { return 0; }
        }
        else { return 0; }
        
        
    }
    else { return 0; }
    
}
std::string points_won(std::string hand, char cards[13]) {
    int occurences[13];
    std::string points;
    for (int i = 0; i < 13; i++) {
        occurences[i] = number_in(hand, cards[i]);
    }
    bool swapped;
    for (int i = 0; i < 13; i++) {
        swapped = false;
        for (int j = 1; j < (13 - i - 1); j++) {
            if (occurences[j]<occurences[j+1]) {
                std::swap(occurences[j], occurences[j + 1]);
                std::swap(cards[j], cards[j + 1]);
                swapped = true;
            }
        }
        if (not swapped) {
            break;
        }
    }
    //std::cout  << "\nC N\n";
    //for (int i = 0; i < 13; i++) {
    //    std::cout << cards[i] << " " << occurences[i] << "\n";
    //}
    if (occurences[0] == 5) {
        points = "F" + hand;
    }
    else  if (occurences[0] + occurences[1] == 5) {
        points = "F" + hand;
    }
    else if (occurences[0] + occurences[1] == 4) {
        points = "O" + hand;
    }
    else if ((occurences[0] + occurences[1] == 3 and occurences[2] ==2)) {
        points = "U" + hand;
    }
    else if (occurences[0] + occurences[1] == 3) {
        points = "T" + hand;
    }
    else if (occurences[1] == 2 and occurences[2] == 2) {
        points = "W" + hand;
    }
    else if (occurences[0] + occurences[1] == 2) {
        points = "N" + hand;
    }
    else {
        points = "H" + hand;
    }
    
    return points;
    

}




int main()
{
    std::fstream file;
    file.open("D:\\!Advent_of_Code\\2023\\day_7\\input.txt");
    std::string tp;
    const int length = 1000;
    int rank[length];
    int bid[length];
    char cards[13] = { 'J','A','K','Q','T','9','8','7','6','5','4','3','2'};
    std::string points[length];
    std::string hand[length];
    if (file.is_open()) {
        int currline = 0;
        while (getline(file, tp)) {
            std::string temp = "";
            for (int i = 0; i < tp.length(); i++) {
                temp += tp[i];
                if (tp[i] == ' ') {
                    temp = "";
                }
                if (i == 4) {
                    hand[currline] = temp;
                    temp = "";
                }
                if (i == tp.length() - 1) {
                    bid[currline] = std::stoi(temp);
                }
            }
            currline++;
        }
        file.close();
    }
    std::cout << "\n";
    for (int i =0; i < length; i++) {
        points[i] = points_won(hand[i], cards);
        
    }
    std::cout << "Testing hands: N32T3K & TT55J5: " << a_bigger_than_b_points("N32T3K", "TT55J5") << "\n";
    std::cout << "Testing hands: N32T3K & WKK677: " << a_bigger_than_b_points("N32T3K", "WKK677") << "\n";
    std::cout << "Testing hands: N32T3K & NKTJJT: " << a_bigger_than_b_points("N32T3K", "NKTJJT") << "\n";
    std::cout << "Testing hands: N32T3K & TQQQJA: " << a_bigger_than_b_points("N32T3K", "TQQQJA") << "\n";
    std::cout << "Testing hands: TT55J5 & WKK677: " << a_bigger_than_b_points("TT55J5", "WKK677") << "\n";
    std::cout << "Testing hands: TT55J5 & NKTJJT: " << a_bigger_than_b_points("TT55J5", "NKTJJT") << "\n";
    std::cout << "Testing hands: TT55J5 & TQQQJA: " << a_bigger_than_b_points("TT55J5", "TQQQJA") << "\n";
    std::cout << "Testing hands: WKK677 & NKTJJT: " << a_bigger_than_b_points("WKK677", "NKTJJT") << "\n";
    std::cout << "Testing hands: WKK677 & TQQQJA: " << a_bigger_than_b_points("WKK677", "TQQQJA") << "\n";
    std::cout << "Testing hands: NKTJJT & TQQQJA: " << a_bigger_than_b_points("NKTJJT", "TQQQJA") << "\n";
    
    bool swapped;
    for (int i = 0; i < length; i++) {
        swapped = false;
        for (int j = 0; j < (length -i-1); j++) {
            if (a_bigger_than_b_points(points[j], points[j+1])) {
                std::swap(points[j], points[j + 1]);
                std::swap(bid[j], bid[j + 1]);
                std::swap(hand[j], hand[j + 1]);
                swapped = true;
            }
        }
        if (not swapped) {
            break;
        }
    }
    int winning = 0;
    std::cout << "\nHand  Points Bid\n";
    for (int i = 0; i < length; i++) {
        std::cout << hand[i] << " " << points[i] << " "  << bid[i] << "\n";
        winning += bid[i] * (i+1);
    }
    std::cout << "The winnings is: " << winning;

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
