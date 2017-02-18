# Normalize string program

**Build**: `g++ -std=c++0x normalize.cpp`

**Speed**: ~10 Gbps on strings of length N with N/3 parent dirs, N/3 current(dot) dirs

**Cyclo complexity**: 4

Sample output - 
```
`normalize` test suite
-- Test 1   PASSED    normalized path for .. == /
-- Test 2   PASSED    normalized path for ../ == /
-- Test 3   PASSED    normalized path for ../.. == /
-- Test 4   PASSED    normalized path for ../../ == /
-- Test 5   PASSED    normalized path for ../././../ == /
-- Test 6   PASSED    normalized path for ../bar == /bar
-- Test 7   PASSED    normalized path for ../foo/bar/baz/../he/ == /foo/bar/he/
-- Test 8   PASSED    normalized path for /foo/../../baz == /baz
-- Test 9   PASSED    normalized path for /foo/bar == /foo/bar
-- Test 10   PASSED    normalized path for /foo/bar/../../../bak == /bak
-- Test 11   PASSED    normalized path for /foo/bar/../baz == /foo/baz
-- Test 12   PASSED    normalized path for /foo/bar/./baz == /foo/bar/baz
-- Test 13   PASSED    normalized path for bar == /bar
`normalize` performance suite
 slashes: 10000000 parent_dirs: 3335752 curr_dirs: 3330580 res_time: 912 millisecs speed: 10.964912 Gbps
 slashes: 10000000 parent_dirs: 3333213 curr_dirs: 3334146 res_time: 920 millisecs speed: 10.869565 Gbps
 slashes: 10000000 parent_dirs: 3331569 curr_dirs: 3335551 res_time: 909 millisecs speed: 11.001100 Gbps
 slashes: 10000000 parent_dirs: 3333909 curr_dirs: 3332704 res_time: 904 millisecs speed: 11.061947 Gbps
 slashes: 10000000 parent_dirs: 3335284 curr_dirs: 3333744 res_time: 1154 millisecs speed: 8.665511 Gbps
 slashes: 10000000 parent_dirs: 3334499 curr_dirs: 3331991 res_time: 907 millisecs speed: 11.025358 Gbps
 slashes: 10000000 parent_dirs: 3333512 curr_dirs: 3333619 res_time: 921 millisecs speed: 10.857763 Gbps
 slashes: 10000000 parent_dirs: 3334718 curr_dirs: 3332011 res_time: 997 millisecs speed: 10.030090 Gbps
 slashes: 10000000 parent_dirs: 3335150 curr_dirs: 3330226 res_time: 914 millisecs speed: 10.940919 Gbps
 slashes: 10000000 parent_dirs: 3335662 curr_dirs: 3333425 res_time: 904 millisecs speed: 11.061947 Gbps
 ```
