rm -rf ./build
conan install ../conan -if build/Release -s build_type=Release --build missing
conan install ../conan -if build/Debug   -s build_type=Debug   --build missing

source build/Release/conanbuild.sh
cmake --preset release -B ./build/Release -S .
cmake --build ./build/Release 
source build/Release/deactivate_conanbuild.sh

source build/Debug/conanbuild.sh
cmake --preset debug -B ./build/Debug -S .
cmake --build ./build/Debug 
source build/Debug/deactivate_conanbuild.sh


