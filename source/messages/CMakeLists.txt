cmake_minimum_required(VERSION 3.15)
project(messages CXX)

find_package(Protobuf REQUIRED)

protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS example_msg.proto)

add_library(${PROJECT_NAME} ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(${PROJECT_NAME} PUBLIC protobuf::libprotobuf)
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_BINARY_DIR})
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_14)