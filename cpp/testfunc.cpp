#include <functional>

typedef void(*void_fptr)();

// Declare simple prototype 
// FOR EXAMPLE : STRICT prototype that is used in library, that you are linking
void old_school_func(void_fptr ptr) { 
	ptr(); 
}

void foo() { }

int main () {
	old_school_func(foo); // OK! old style call

	int a = 0;
	auto good_lambda = [] () { "lambda"; };
	auto bad_lambda = [&] () { a++; "lambda"; };

	old_school_func(good_lambda); // OK! Seems to be pointer to function (Clever GCC auto)
	old_school_func(bad_lambda); // NOPE :( Function object -> similar to std::function

	std::function<void()> func_obj = [] () { "yeap"; };
	old_school_func(func_obj);	// NOPE :( std::function is func object, it cannot be converted to old school function pointers

	// SO: HOW TO convert the *func_obj* variable to call *old_school_func* function? 
	// ANSWER: seems to be NO WAY.  C++ ;(

}