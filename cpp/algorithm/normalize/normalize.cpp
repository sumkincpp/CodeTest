// 
// Normalize string program
// 
// Build: g++ -std=c++0x normalize.cpp
//
// Speed: ~10 Gbps on strings of length N with N/3 parent dirs, N/3 current(dot) dirs
// Cyclo complexity: 4
//
#include <iostream>
#include <vector>
#include <map> // for tests
#include <chrono>

// ------------------------------------------------------------------------------------

std::string normalize(const std::string &path);

void test_normalize(const std::string& path, const std::string& normalized);
void test_normalize_suite();
void test_normalize_speed();

// ------------------------------------------------------------------------------------
namespace sc = std::chrono;

inline long current_millis() {
  auto time = sc::system_clock::now(); // get the current time
  auto since_epoch = time.time_since_epoch(); // get the duration since epoch

  auto millis = sc::duration_cast<sc::milliseconds>(since_epoch);
  return millis.count();
}

inline long get_exec_time (std::function<void()> func) {
    long now = current_millis(), final; // just like java (new Date()).getTime();
    func();
    final = current_millis() - now;
    return final;
}
// ------------------------------------------------------------------------------------
int main () 
{
	test_normalize_suite();	
	test_normalize_speed();
}
// ------------------------------------------------------------------------------------
void test_normalize_speed_single(int length = 10000000) 
{
	std::string seed_string = "";
	seed_string.reserve(length);

	int int_prob = 3;
	int slashes = 0;
	int parent_dirs = 0;
	int curr_dirs = 0;

	for(int i = 0; i < length; i++) {
		int rand_val = rand();

		seed_string += "/";
		slashes ++;
		switch(rand_val % int_prob) {
			case 0:
				seed_string += "..";
				parent_dirs ++;
				break;
			case 1:
				seed_string += ".";
				curr_dirs ++;
				break;
			default: 
				seed_string += "a";
				break;
		}
	}

	long res_time = get_exec_time ([&seed_string] () {
		normalize(seed_string);
	});

	// byte/millisec = KByte/sec => Gbyte /1000
	double speed = double(length)/(res_time*1000);

	// printf(" %s (truncated) \n", seed_string.substr(0, 70).c_str());

	printf(" slashes: %5d parent_dirs: %5d curr_dirs: %5d res_time: %ld millisecs speed: %5f Gbps \n", 
			slashes, parent_dirs, curr_dirs, res_time, speed);

}
// ------------------------------------------------------------------------------------
void test_normalize_speed() 
{
	std::cout << "`normalize` performance suite" << std::endl;

	for (int i = 0; i < 10; i++)
		test_normalize_speed_single();
}

// ------------------------------------------------------------------------------------
void test_normalize_suite() 
{
	std::cout << "`normalize` test suite" << std::endl;
	std::map<std::string, std::string> normalize_tests = {
		{"../", "/"},
		{"../..", "/"},
		{"../../", "/"},
		{"..", "/"},
		{"../././../", "/"},
		{"../bar", "/bar"},
		{"bar", "/bar"},
		{"/foo/bar", "/foo/bar"},
		{"/foo/bar/../../../bak", "/bak"},
		{"/foo/bar/../baz", "/foo/baz"},
		{"/foo/bar/./baz", "/foo/bar/baz"},
		{"/foo/../../baz", "/baz"},
		{"../foo/bar/baz/../he/", "/foo/bar/he/"},
	};

	for(auto it = normalize_tests.begin(); it != normalize_tests.end(); ++it) {
		test_normalize(it->first, it->second);
	}
}
// ------------------------------------------------------------------------------------
void test_normalize(const std::string& path, const std::string& expected) 
{
	static int i = 1;
	std::cout << "-- Test " << i;

	std::string computed = normalize(path);
	bool is_passed = computed == expected;

	if (is_passed) {
		std::cout << "   PASSED ";
	} else {
		std::cout << "   FAILED ";
	}
	
	std::cout << "   normalized path for " << path << " == " << expected;

	if (!is_passed) {
		std::cout << " --- computed " << computed;
	}

	std::cout << std::endl;
	i += 1;
}
// ------------------------------------------------------------------------------------
struct url_part {
	int start;
	int end;

	// just for convenience, there might be default parameters/constructor
	url_part(int start_, int end_): 
		start(start_),
		end(end_)
		{ }

	void print(const std::string& str) {
		std::cout << " - start " << start << " end " << end << " == "<< str.substr(start, end-start);
		std::cout << std::endl;
	}
};
// ------------------------------------------------------------------------------------
// cyclo complexity ~= 1 + 13 + 1 + 5 - (1 + 11 + 1 + 5) + 2 = 18 - 16 + 2 = 4
std::string normalize(const std::string &path) 
{	
	std::vector<url_part> parts;

	int prev_start = 0;
	int length = path.length();

	// N slashes -> N*
	// node = 10, edge = 12
	// with cycle, node = 11, edge = 13
	while (prev_start < length + 1) {
		// node = 1, edge = 1
		int new_found = path.find_first_of("/", prev_start);

		// node = 2, edge = 2
		if (new_found == std::string::npos) {
			new_found = length; // for breaking loop condition
		}

		// node=5+1=6, edge= 7 + 1
		if (new_found != prev_start) {
			// node 5, edge 7 = (3 + 2 + 1 + 1)
			if (new_found == prev_start + 2 &&
				path.compare(prev_start, 2, "..") == 0) {

				// node=2, edge=2
				if (parts.size() > 0)
					parts.pop_back();

				// This part might be for POSIX real_path behaviour, actually -->
				// else 
				// 	parts.push_back(url_part(prev_start, prev_start+2, PT_PARENT));			
			} else if (new_found == prev_start + 1 &&
				path[prev_start] == '.') {
				// node 1, edge 1
				// simply ignoring current folder dot
			} else {
				// node=1, edge=1
				parts.push_back(url_part(prev_start, new_found));
			}
		}
		// node = 1, edge = 1
		prev_start = new_found + 1;
	}

	std::string rel_path = "/";

	// std::cout << std::endl;
	// for (int i = 0; i < parts.size(); ++i)
	// 	parts[i].print(path);

	int i = 0;

	// node = 5, edge = 5
	if (parts.size() > 0) {
		// node = 3, edge = 3
		for (; i < parts.size()-1; ++i) {
			rel_path += path.substr(parts[i].start, parts[i].end-parts[i].start) + "/";
		}

		// node = 1, edge = 1
		rel_path += path.substr(parts[i].start, parts[i].end);
	}

	return rel_path;
}
