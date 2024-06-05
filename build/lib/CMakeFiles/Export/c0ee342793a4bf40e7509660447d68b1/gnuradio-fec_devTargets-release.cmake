#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "gnuradio::gnuradio-fec_dev" for configuration "Release"
set_property(TARGET gnuradio::gnuradio-fec_dev APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(gnuradio::gnuradio-fec_dev PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libgnuradio-fec_dev.1.0.0.0.dylib"
  IMPORTED_SONAME_RELEASE "/usr/local/lib/libgnuradio-fec_dev.1.0.0.dylib"
  )

list(APPEND _cmake_import_check_targets gnuradio::gnuradio-fec_dev )
list(APPEND _cmake_import_check_files_for_gnuradio::gnuradio-fec_dev "${_IMPORT_PREFIX}/lib/libgnuradio-fec_dev.1.0.0.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
