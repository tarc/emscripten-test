include(default)

[settings]
os=Emscripten
arch=asm.js
compiler=clang
compiler.version=6.0
compiler.libcxx=libc++

[options]

[build_requires]
emsdk_installer/1.38.29@bincrafters/stable

[env]
