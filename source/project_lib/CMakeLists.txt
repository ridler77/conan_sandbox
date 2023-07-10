cmake_minimum_required(VERSION 3.15)

project(
    project_lib
    VERSION 1.0
    DESCRIPTION
        "Example library project"
    LANGUAGES CXX
)

set(src 
   lib.cpp
   lib.h
   internal_subproject/class_x.cpp
   internal_subproject/class_x.h
)

add_library(${PROJECT_NAME} ${src})
target_include_directories(${PROJECT_NAME} 
   PUBLIC ${CMAKE_CURRENT_LIST_DIR}
   PRIVATE ${CMAKE_CURRENT_LIST_DIR}/internal_subproject
)
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_14)