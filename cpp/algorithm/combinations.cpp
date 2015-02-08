/**
 * Generating combinations (i.e. Permutations with Repetitions)
*/
#include <iostream>
#include <cmath>

int main () {
    int width = 3;
    int per_selection = 3;

    long long combinations = pow(per_selection, width);

    for (int i = 0; i < combinations; i++) {
        std::cout << "i: " << i << " "; // << i << " " << i%per_selection << " - " << (i - i%per_selection)/per_selection << std::endl;

        // This one for (c)hecking
        /*std::cout << (i%per_selection - i%1) / 1 << " "
                  << (i%(per_selection*per_selection)-i%per_selection)/(per_selection) << " "
                  << (i-i%(per_selection*per_selection))/(per_selection*per_selection);*/

        for(int j = 0; j < width; j++) {
            int pow_res = pow(per_selection, j);

            std::cout << (i % (per_selection * pow_res) - i%pow_res)/(pow_res);
        }

        std::cout << std::endl;;
    }

}
