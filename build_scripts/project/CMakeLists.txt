cmake_minimum_required(VERSION 3.15)

project(
    top
    VERSION 1.0
    DESCRIPTION
        "Top level roll up project"
    LANGUAGES CXX
)

if (NOT TARGET project_lib)
   add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../../source/project_lib project_lib)
endif()

if (NOT TARGET messages)
   add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../../source/messages messages)
endif()

if (NOT TARGET project_exe)
   add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../../source/project_exe project_exe)
endif()