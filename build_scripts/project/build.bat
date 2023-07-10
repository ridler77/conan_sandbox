conan install ../conan -if build -pr:b=../conan/profiles/msvc16_release_mt -pr:h=../conan/profiles/msvc16_release_mt --build missing
conan install ../conan -if build -pr:b=../conan/profiles/msvc16_debug_mt -pr:h=../conan/profiles/msvc16_debug_mt --build missing

call build\conanbuild.bat

cmake --preset default -B ./build -S .
cmake --build ./build --config Release
cmake --build ./build --config Debug

build/deactivate_conanbuild.bat