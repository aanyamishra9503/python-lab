#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>

int main() {
    int num;
    printf("Welcome to the Number Analyser!\n");
    printf("This program will analyze the properties of a given number.\n");
    
    printf("Enter a number: ");
    if (scanf("%d", &num) != 1) {
        printf("Invalid input.\n");
        return 1;
    }


    // Positive / Negative / Zero
    if (num > 0) printf("Positive\n");
    else if (num < 0) printf("Negative\n");
    else printf("Zero\n");

    // Even or Odd
    if (num % 2 == 0) printf("Even\n");
    else printf("Odd\n");

    // Prime Check
    if (num > 1) {
        bool is_prime = true;
        int limit = (int)sqrt(num);
        for (int i = 2; i <= limit; i++) {
            if (num % i == 0) {
                is_prime = false;
                break;
            }
        }
        if (is_prime) printf("Prime\n");
        else printf("Composite\n");
    } else if (num == 1) {
        printf("Neither Prime nor Composite\n");
    }

    // Perfect Square
    if (num >= 0) {
        int root = (int)sqrt(num);
        if (root * root == num) printf("Perfect Square\n");
    }

    // Divisible by 5 and 10
    if (num % 5 == 0) printf("Divisible by 5\n");
    if (num % 10 == 0) printf("Divisible by 10\n");

    // Armstrong Number Check
    int temp = abs(num);
    int original_temp = temp;
    int digits = 0;
    
    // Count digits
    int count_temp = temp;
    if (count_temp == 0) digits = 1;
    while (count_temp > 0) {
        digits++;
        count_temp /= 10;
    }
    
    // Calculate power sum
    long long total = 0;
    while (temp > 0) {
        int remainder = temp % 10;
        total += pow(remainder, digits);
        temp /= 10;
    }
    if (total == original_temp) printf("Armstrong Number\n");

    // Palindrome Number Check
    temp = abs(num);
    long long reversed_num = 0;
    int rem;
    while (temp != 0) {
        rem = temp % 10;
        reversed_num = reversed_num * 10 + rem;
        temp /= 10;
    }
    if (reversed_num == abs(num)) printf("Palindrome Number\n");
}
