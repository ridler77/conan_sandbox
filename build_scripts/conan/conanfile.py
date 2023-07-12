from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
import os

class TopLevelProject(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = [ \
      # Below packages were tested with Ubuntu 20
      "boost/1.79.0", # conan latest is 1.82.0
      "ceres-solver/2.0.0", # conan latest is 2.1.0
      "dlib/19.24",  # want dlib-19.3 - conan latest is 19.24
      "eigen/3.3.7", # conan latest is 3.4.0
      "ffmpeg/5.1", # want ffmpeg-5.1.2, conan latest is 6.0. SYSTEM LIBS
      "fftw/3.3.9", # conan latest is 3.3.10 which contains a minor bugfix
      "gdal/3.1.2", # conan latest is 3.5.2 - SLOW BUILD
      "geographiclib/1.50.1", # want geographic_lib-1.46, conan latest is 1.52
      "gsl/2.7", # conan latest is 2.7
      "gtest/1.11.0", # conan latest is 1.13.0
      "hdf5/1.8.21",  # closest compatible version to hdf5-1.8.20, conan latest is 1.14.1
      "libharu/2.3.0", # conan latest is 2.4.3
      "libjpeg/9d", # conan latest is 9e
      # "libpng/1.6.40", # want libpng-1.6.21, but that's really old. Overriden later
      # NO VERSIONS ON CONAN - marble-20.04.3_no_opengl
      "nanomsg/1.2", # want nanomsg-1.0.0, conan only has 1.2.  Creator says to use nng, no more work on nanomsg
      # DOESN'T BUILD ON UBUNTU 20 "opencv/4.5.0" or 4.5.5, # want opencv-4.2.0, conan latest is 4.5.5. SYSTEM LIBS
      "proj/6.3.1", # want proj-6.2.0, conan latest is 9.2.1
      "protobuf/3.9.1", # want protobuf-3.9.0, conan latest is 3.21.12
      "qt/5.15.10", # want qt-5.11.1, conan latest is 5.15.10 and 6.5.1 - SLOW BUILD
      # want sqlite3-3.30.1, conan latest is 3.42.0.  Overriden later
      "libtiff/4.0.9", # conan latest is 4.5.1
      "xerces-c/3.2.4", # conan latest is 3.2.4
      "zlib/1.2.13", # conan latest is 1.2.13
      # overrides to get packages on the same version \
      "libpng/1.6.40",  # 'freetype/2.13.0' requires 'libpng/1.6.40' while 'dlib/19.24' requires 'libpng/1.6.37', conan latest is 1.6.40
      "libwebp/1.3.1",  # 'ffmpeg/5.1' requires 'libwebp/1.3.0' while 'dlib/19.24' requires 'libwebp/1.2.2', conan latest is 1.3.1
      "sqlite3/3.42.0", # 'proj/8.1.1' requires 'sqlite3/3.36.0' while 'dlib/19.24' requires 'sqlite3/3.38.5', conan latest is 3.42.0
      "libiconv/1.17",  # 'gdal/3.1.2' requires 'libiconv/1.16' while 'ffmpeg/5.1' requires 'libiconv/1.17', conan latest is 1.17
   ]
   
   tool_requires = "cmake/3.26.4"
   generators = "CMakeDeps", "CMakeToolchain", "VirtualBuildEnv"

   #default_options = {"opencv:with_webp" : False,
   #                   "opencv:dnn" : False}

   def generate(self):
      tc = CMakeToolchain(self)
      # Our conanfile.py does not live in the same folder as the project's CML.txt file
      # By defualt the CMakeUserPresets.json file is created with the conanfile
      # Find the path to the project, stepping up from the build or build/Release directory
      p = os.path.split(self.build_folder)
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
