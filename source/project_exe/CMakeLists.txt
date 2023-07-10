cmake_minimum_required(VERSION 3.15)

project(
    project_exe
    VERSION 1.0
    DESCRIPTION
        "Executable main.cpp with classes"
    LANGUAGES CXX
)

if (NOT TARGET project_lib)
   add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../project_lib project_lib)
endif()

set(src 
   a_class.hpp
   b_class.cpp
   b_class.h
   main.cpp
)

add_executable(${PROJECT_NAME} ${src})
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_LIST_DIR})
target_link_libraries(${PROJECT_NAME} PRIVATE project_lib)
