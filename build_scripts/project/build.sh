rm -rf ./build
conan install ../conan -if build/Release -pr:b=../conan/profiles/gcc9_release -pr:h=../conan/profiles/gcc9_release --build missing
conan install ../conan -if build/Debug   -pr:b=../conan/profiles/gcc9_debug -pr:h=../conan/profiles/gcc9_debug     --build missing

source build/Release/conanbuild.sh
cmake --preset release -B ./build/Release -S .
cmake --build ./build/Release 
source build/Release/deactivate_conanbuild.sh

source build/Debug/conanbuild.sh
cmake --preset debug -B ./build/Debug -S .
cmake --build ./build/Debug 
source build/Debug/deactivate_conanbuild.sh


