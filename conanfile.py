from conans import ConanFile, CMake


class TestLib1Conan(ConanFile):
    name = "test_lib_1"
    version = "1.0.1"
    author = "A. Sokolov <AUSokolov@luxoft.com>"
    description = "Created for testing of conan usage"
    scm = {"type": "git", "url": "auto", "revision": "auto"}
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    no_copy_source = True

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["test_lib_1"]
