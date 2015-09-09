# https://github.com/zeromq/libzmq/blob/4e5843b8ff6ff4f32b80ddd17b7ad10c8966480a/CMakeLists.txt
#-----------------------------------------------------------------------------
# force off-tree build

if(${CMAKE_CURRENT_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_BINARY_DIR})
message(FATAL_ERROR "CMake generation is not allowed within the source directory!
Remove the CMakeCache.txt file and try again from another folder, e.g.:
   rm CMakeCache.txt
   mkdir cmake-make
   cd cmake-make
   cmake ..
")
endif()
