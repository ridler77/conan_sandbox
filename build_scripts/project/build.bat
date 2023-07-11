rmdir /S /Q build
conan install . -if build -of . -s build_type=Release --build missing
conan install . -if build -of . -s build_type=Debug   --build missing

call build\generators\conanbuild.bat
cmake --preset default
cmake --build ./build --config Release
cmake --build ./build --config Debug
call build\generators\deactivate_conanbuild.bat

