#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Usage: day6 input_file\n";
        return 1;
    }
    std::ifstream file(argv[1]);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << argv[1] << std::endl;
        return 1;
    }

    std::string line;
    std::vector<std::string> lines;
    std::unordered_map<int, std::vector<char>> columns;
    std::string message {""};

    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    for (const auto& line: lines) {
        for (int i = 0, n = line.length(); i < n; i++) {
            columns[i].push_back(line[i]);
        }
    }

    for (const auto& k: columns) {
        for (const auto i : k.second) {
            int count = std::count(k.second.begin(), k.second.end(), i);
            // std::cout << count << std::endl;
        }
    }

    std::cout << message << std::endl;

    // This only prints the contentes of the map. Commenting it for now
    // for (const auto& [key, value]: columns) {
    //     std::cout << key << ": ";
    //     for (const auto& i : value) {
    //         std::cout << i << " ";
    //     }
    //     std::cout << std::endl;
    // }

    return 0;
}
