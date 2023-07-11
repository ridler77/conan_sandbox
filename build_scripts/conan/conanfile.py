from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
import os

class TopLevelProject(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "protobuf/3.9.1"
   tool_requires = "cmake/3.26.4"
   generators = "CMakeDeps", "CMakeToolchain", "VirtualBuildEnv"

   def generate(self):
      tc = CMakeToolchain(self)
      # Our conanfile.py does not live in the same folder as the project's CML.txt file
      # By defualt the CMakeUserPresets.json file is created with the conanfile
      tc.user_presets_path = os.path.join(self.build_folder,"..","..","CMakeUserPresets.json")
      tc.generate()

      deps = CMakeDeps(self)
      deps.generate()

   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()
   
   def layout(self):
      cmake_layout(self)
