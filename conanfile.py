from conans import ConanFile, CMake


class EmscriptenTest(ConanFile):
    name = "emscripten-test"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Emscriptentest here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = {"os": ["Emscripten"]}
    exports_sources = ["CMakeLists.txt", "version.hpp.in", "src/main.cpp"]
    generators = "cmake"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
