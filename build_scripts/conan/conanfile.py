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
      # Find the path to the project, stepping up from the build or build/Release directory
      p = os.path.split(self.build_path)
      while p[1] in ['Release', 'Debug', 'build']:
         p = os.path.split(p[0])
      proj_path = os.path.join(p[0], p[1])
      # St the path so the json file is created in the correct place
      tc.user_presets_path = os.path.join(proj_path, "CMakeUserPresets.json")
      tc.generate()

      deps = CMakeDeps(self)
      deps.generate()

   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()
   
   def layout(self):
      cmake_layout(self)
