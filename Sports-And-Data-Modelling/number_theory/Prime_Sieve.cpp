#include <iostream>     // Required for input/output stream
#include <vector>       // Required for using the vector container
#include <cmath>        // Required for math operations like sqrt()
#include <iomanip>      // Required for formatted output (setw)

// Function to visually print the sieve result
void printSieve(const std::vector<bool>& isPrime) {
    std::cout << "\nVisualising sieve (P = prime, - = not prime):\n";
    for (size_t i = 2; i < isPrime.size(); ++i) {
        // Print index (number) and mark it as Prime (P) or Not Prime (-)
        std::cout << std::setw(3) << i << ": " << (isPrime[i] ? "P" : "-") << "\n";
    }
}

int main() {
    int limit;

    // Prompt the user for the upper bound of the prime search
    std::cout << "Enter the upper limit to find all prime numbers up to: ";
    std::cin >> limit;

    // Edge case: if input is less than 2, there are no primes to show
    if (limit < 2) {
        std::cout << "There are no primes less than 2.\n";
        return 0;
    }

    // Step 1: Initialize a boolean vector `isPrime` with all values set to true
    // Index `i` of the vector represents the number `i`
    std::vector<bool> isPrime(limit + 1, true);
    
    // 0 and 1 are not primes, so we mark them false
    isPrime[0] = isPrime[1] = false;

    int step = 0; // Counter to track steps in the sieve process
    std::cout << "\nStarting Sieve of Eratosthenes...\n";

    // Step 2: Implementing the Sieve of Eratosthenes
    // We only need to go up to sqrt(limit) to mark multiples
    for (int i = 2; i * i <= limit; ++i) {
        if (isPrime[i]) {
            // Display progress
            std::cout << "Step " << ++step << ": Eliminating multiples of " << i << "...\n";
            
            // Mark all multiples of i as not prime
            for (int j = i * i; j <= limit; j += i) {
                isPrime[j] = false;
            }
        }
    }

    // Step 3: Output the sieve state
    printSieve(isPrime);

    // Step 4: Display all numbers marked as prime
    std::cout << "\nList of prime numbers up to " << limit << ":\n";
    for (int i = 2; i <= limit; ++i) {
        if (isPrime[i]) {
            std::cout << i << " ";
        }
    }
    std::cout << "\n";

    return 0; // End program
}
