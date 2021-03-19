cmake_minimum_required(VERSION 2.8)

project(Test_lib_1)

add_library(test_lib_1 test_lib_1.cpp)

install(TARGETS test_lib_1 DESTINATION lib)
install(FILES test_lib_1.h DESTINATION include)