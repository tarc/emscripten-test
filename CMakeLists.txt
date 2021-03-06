set( ProjectName emscripten-test )

project( ${ProjectName} )
cmake_minimum_required( VERSION 3.10 )


# Multi configuration build setup:

include( ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake )

conan_basic_setup( TARGETS )


# Versioning the project (if git can be found)

find_package( Git )

set ( MAJOR_VERSION_NUMBER "0" )
set ( MINOR_VERSION_NUMBER "0" )
set ( PATCH_VERSION_NUMBER "0" )

if ( Git_FOUND )

  message( "Git found: ${GIT_EXECUTABLE}" )

  execute_process( COMMAND ${GIT_EXECUTABLE} describe --abbrev=0 --tags --always
    OUTPUT_VARIABLE GIT_REPO_VERSION )

  if ( GIT_REPO_VERSION MATCHES "v([0-9]*)\\.([0-9]*)\\.([0-9]*)" )
    message( "Parsing version: ${CMAKE_MATCH_1}.${CMAKE_MATCH_2}.${CMAKE_MATCH_3}" )

    set ( MAJOR_VERSION_NUMBER ${CMAKE_MATCH_1} )
    set ( MINOR_VERSION_NUMBER ${CMAKE_MATCH_2} )
    set ( PATCH_VERSION_NUMBER ${CMAKE_MATCH_3} )

  else ( )

    message( "Could not extract version from: ${GIT_REPO_VERSION}" )

  endif ( )

endif ( )

configure_file ( version.hpp.in version.hpp )


# Setting targets:

add_executable( ${ProjectName}
  ${CMAKE_SOURCE_DIR}/src/main.cpp )

target_include_directories( ${ProjectName}
  PRIVATE ${CMAKE_SOURCE_DIR}/include
  PRIVATE ${CMAKE_CURRENT_BINARY_DIR} )

# target_link_libraries( ${ProjectName}
#  PRIVATE CONAN_PKG::some-package )

set_target_properties(${PROJECT_NAME} PROPERTIES
  SUFFIX ".html"
  LINK_FLAGS "--emrun")

install(TARGETS ${PROJECT_NAME}
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib)
  
install(FILES
  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}.js
  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}.wasm
  DESTINATION bin)


# Force C++17 standard:

set_property ( TARGET ${ProjectName} PROPERTY CXX_STANDARD 17 )
set_property ( TARGET ${ProjectName} PROPERTY CXX_STANDARD_REQUIRED ON )
