#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstring>
#include <dirent.h>
#include <regex>

std::vector<std::string> get_station_macs(const std::string& filename) {
    std::vector<std::string> station_macs;

    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error: Unable to open file '" << filename << "'." << std::endl;
        return station_macs;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::smatch match;
        // Assuming MAC addresses are in the first column and separating columns with ','
        std::regex_search(line, match, std::regex("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})"));
        if (!match.empty()) {
            station_macs.push_back(match[0]);
        }
    }

    file.close();
    return station_macs;
}

int main() {
    std::ofstream outfile("extracted.txt");
    if (!outfile.is_open()) {
        std::cerr << "Error: Unable to open output file 'extracted.txt'." << std::endl;
        return 1;
    }

    DIR* dir;
    struct dirent* entry;

    if ((dir = opendir(".")) != nullptr) {
        while ((entry = readdir(dir)) != nullptr) {
            const std::string filename = entry->d_name;

            // Check if the file has a .csv extension
            if (filename.size() > 4 && filename.substr(filename.size() - 4) == ".csv") {
                // Get station MACs from the CSV file
                std::vector<std::string> station_macs = get_station_macs(filename);

                // Write station MACs to the output file
                for (const auto& mac : station_macs) {
                    outfile << mac << std::endl;
                }
            }
        }
        closedir(dir);

        std::cout << "Station MAC addresses have been extracted and written to 'extracted.txt'." << std::endl;
    } else {
        std::cerr << "Error: Unable to open the current directory." << std::endl;
        return 1;
    }

    outfile.close();
    return 0;
}
