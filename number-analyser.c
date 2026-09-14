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

    printf("\n========================================\n");
    printf("Analysis Result\n");
    printf("========================================\n");

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

    printf("========================================\n");
    printf("\nWould you like to see any additional information?\n");

    int choice;
    while (1) {
        printf("\n1. Multiplication Table\n");
        printf("2. Square, Cube & Square Root\n");
        printf("3. Factors\n");
        printf("4. Sum of Digits\n");
        printf("5. Reverse Number\n");
        printf("6. Exit\n\n");
        
        printf("Enter your choice (1-6): ");
        if (scanf("%d", &choice) != 1) {
            printf("Invalid selection!\n");
            break;
        }

        if (choice == 1) {
            printf("\nMultiplication Table of %d\n", num);
            for (int i = 1; i <= 10; i++) {
                printf("%d x %d = %d\n", num, i, num * i);
            }
        }
        else if (choice == 2) {
            printf("\nSquare : %ld\n", (long)num * num);
            printf("Cube   : %ld\n", (long)num * num * num);
            if (num >= 0) {
                printf("Square Root : %.2f\n", sqrt(num));
            } else {
                printf("Square Root : Not a real number\n");
            }
        }
        else if (choice == 3) {
            printf("Factors: [");
            int absolute_num = abs(num);
            bool first = true;
            for (int i = 1; i <= absolute_num; i++) {
                if (num % i == 0) {
                    if (!first) printf(", ");
                    printf("%d", i);
                    first = false;
                }
            }
            printf("]\n");
        }
        else if (choice == 4) {
            int digit_sum = 0;
            int n = abs(num);
            while (n > 0) {
                digit_sum += n % 10;
                n /= 10;
            }
            printf("Sum of Digits: %d\n", digit_sum);
        }
        else if (choice == 5) {
            int n = abs(num);
            long long rev = 0;
            while (n > 0) {
                rev = rev * 10 + (n % 10);
                n /= 10;
            }
            if (num < 0) printf("Reverse: -%lld\n", rev);
            else printf("Reverse: %lld\n", rev);
        }
        else if (choice == 6) {
            printf("\nThank you for using Number Analyzer!\n");
            break;
        }
        else {
            printf("Invalid choice! Please try again.\n");
        }
    }

    printf("Thank you for using the Number Analyser!\n");
    return 0;
}