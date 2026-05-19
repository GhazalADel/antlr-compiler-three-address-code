#include<stdio.h>

// Helper macros for common operations
#define printInt(k) printf("%d\n", k)
#define printDouble(x) printf("%f\n",x)
#define printString(t) printf("%s\n", t)

// Functions to read integers and doubles from the user
int readInt() {
	int x;
	scanf(" %d", &x);
	return x;
}

double readDouble() {
	double x;
	scanf(" %f", &x);
	return x;
}

// Define a union for different types of cells
union cell {
	int i;
	double d;
	void* l;
};

// Define a large array of cells to act as the memory
int stack_size = 1000000;
union cell m[stack_size];
int top = 0; // Represents the current top of the stack
int bottom = stack_size - 1; // Represents the start of the current function's activation record


int main() {
	// Initialize your environment or variables if necessary
	// For example, setting the initial top of the stack or initializing variables

	// Your three-address code statements go here
	// Replace statement_1, statement_2, ..., statement_n with actual operations
	// Example:
	// m[top].i = 5; // Assigning integer 5 to the top of the stack
	// top++; // Moving top of the stack
    
	// Use labels as targets for goto statements
	// Labels correspond to positions in your three-address code where control may jump to
	label_1:
    	// Corresponding operations for label_1
    	// ...

	// Continue with other statements and labels as needed
	// ...

	return 0; // End of main function
}
