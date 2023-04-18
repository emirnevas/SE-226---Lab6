#include <iostream>

double sum_computer() {
    int n;
    std::cout << "Enter the value of n: ";
    std::cin >> n;
    
    if (n <= 0) {
        return 0;
    } else {
        return (-1) * ((n % 2) * 2 - 1) * (1.0 / n) + sum_computer(n - 1);
    }
}

int main() {
    double result = sum_computer();
    std::cout << "Summation: " << result << std::endl;

    return 0;
}
