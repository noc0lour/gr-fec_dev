# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.29

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.29.3/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.29.3/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kmcomer/gr-fec_dev

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kmcomer/gr-fec_dev/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/gnuradio-fec_dev.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include lib/CMakeFiles/gnuradio-fec_dev.dir/compiler_depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/gnuradio-fec_dev.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/gnuradio-fec_dev.dir/flags.make

lib/CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o: lib/CMakeFiles/gnuradio-fec_dev.dir/flags.make
lib/CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o: /Users/kmcomer/gr-fec_dev/lib/turbo_encoder_impl.cc
lib/CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o: lib/CMakeFiles/gnuradio-fec_dev.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kmcomer/gr-fec_dev/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o"
	cd /Users/kmcomer/gr-fec_dev/build/lib && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT lib/CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o -MF CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o.d -o CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o -c /Users/kmcomer/gr-fec_dev/lib/turbo_encoder_impl.cc

lib/CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.i"
	cd /Users/kmcomer/gr-fec_dev/build/lib && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/kmcomer/gr-fec_dev/lib/turbo_encoder_impl.cc > CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.i

lib/CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.s"
	cd /Users/kmcomer/gr-fec_dev/build/lib && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/kmcomer/gr-fec_dev/lib/turbo_encoder_impl.cc -o CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.s

# Object files for target gnuradio-fec_dev
gnuradio__fec_dev_OBJECTS = \
"CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o"

# External object files for target gnuradio-fec_dev
gnuradio__fec_dev_EXTERNAL_OBJECTS =

lib/libgnuradio-fec_dev.1.0.0.0.dylib: lib/CMakeFiles/gnuradio-fec_dev.dir/turbo_encoder_impl.cc.o
lib/libgnuradio-fec_dev.1.0.0.0.dylib: lib/CMakeFiles/gnuradio-fec_dev.dir/build.make
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/lib/libgnuradio-fec.gac2244fa1.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/lib/libgnuradio-blocks.gac2244fa1.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/lib/libgnuradio-runtime.gac2244fa1.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/lib/libgnuradio-pmt.gac2244fa1.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/lib/libboost_thread-mt.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/lib/libspdlog.1.13.0.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/lib/libfmt.10.2.1.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/Cellar/gmp/6.3.0/lib/libgmpxx.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/Cellar/gmp/6.3.0/lib/libgmp.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: /usr/local/lib/libvolk.3.1.2.dylib
lib/libgnuradio-fec_dev.1.0.0.0.dylib: lib/CMakeFiles/gnuradio-fec_dev.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/kmcomer/gr-fec_dev/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libgnuradio-fec_dev.dylib"
	cd /Users/kmcomer/gr-fec_dev/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gnuradio-fec_dev.dir/link.txt --verbose=$(VERBOSE)
	cd /Users/kmcomer/gr-fec_dev/build/lib && $(CMAKE_COMMAND) -E cmake_symlink_library libgnuradio-fec_dev.1.0.0.0.dylib libgnuradio-fec_dev.1.0.0.dylib libgnuradio-fec_dev.dylib

lib/libgnuradio-fec_dev.1.0.0.dylib: lib/libgnuradio-fec_dev.1.0.0.0.dylib
	@$(CMAKE_COMMAND) -E touch_nocreate lib/libgnuradio-fec_dev.1.0.0.dylib

lib/libgnuradio-fec_dev.dylib: lib/libgnuradio-fec_dev.1.0.0.0.dylib
	@$(CMAKE_COMMAND) -E touch_nocreate lib/libgnuradio-fec_dev.dylib

# Rule to build all files generated by this target.
lib/CMakeFiles/gnuradio-fec_dev.dir/build: lib/libgnuradio-fec_dev.dylib
.PHONY : lib/CMakeFiles/gnuradio-fec_dev.dir/build

lib/CMakeFiles/gnuradio-fec_dev.dir/clean:
	cd /Users/kmcomer/gr-fec_dev/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/gnuradio-fec_dev.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/gnuradio-fec_dev.dir/clean

lib/CMakeFiles/gnuradio-fec_dev.dir/depend:
	cd /Users/kmcomer/gr-fec_dev/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kmcomer/gr-fec_dev /Users/kmcomer/gr-fec_dev/lib /Users/kmcomer/gr-fec_dev/build /Users/kmcomer/gr-fec_dev/build/lib /Users/kmcomer/gr-fec_dev/build/lib/CMakeFiles/gnuradio-fec_dev.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : lib/CMakeFiles/gnuradio-fec_dev.dir/depend
