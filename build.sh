#!/usr/bin/env bash

set -ex

conan remove emscripten-test/* -f
conan create . -k -pr emscripten-test.profile --build missing
conan install conanfile.txt -pr emscripten-test.profile
