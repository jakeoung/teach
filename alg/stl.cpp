// Tutorial on STL

#include <iostream>
#include <vector>
#include <tuple>

auto func(int a, int b) {
    return {a, b, a+b}; // how to fix it?
}

int main() {
    auto [a,b,c] = func(3, 4);

    std::cout << a << std::endl;
    return 0;
}