rm -rf ./build
conan install ../conan -if build -of . -s build_type=Release --build missing
conan install ../conan -if build -of . -s build_type=Debug   --build missing

source build/Release/generators/conanbuild.sh
cmake --preset release
cmake --build --preset release
source build/Release/generators/deactivate_conanbuild.sh

source build/Debug/generators/conanbuild.sh
cmake --preset debug
cmake --build --preset debug
source build/Debug/generators/deactivate_conanbuild.sh


