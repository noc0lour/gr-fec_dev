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

# Utility rule file for fec_dev_docstrings.

# Include any custom commands dependencies for this target.
include python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/compiler_depend.make

# Include the progress variables for this target.
include python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/progress.make

python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings: python/fec_dev/bindings/docstring_status

python/fec_dev/bindings/docstring_status:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/Users/kmcomer/gr-fec_dev/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Adding docstrings into fec_dev pybind headers ..."
	cd /Users/kmcomer/gr-fec_dev/build/python/fec_dev/bindings && /usr/local/bin/python3 /Users/kmcomer/gr-fec_dev/docs/doxygen/update_pydoc.py sub --json_path /Users/kmcomer/gr-fec_dev/build/python/fec_dev/bindings/extracted_docstrings.json --bindings_dir /Users/kmcomer/gr-fec_dev/python/fec_dev/bindings/docstrings --output_dir /Users/kmcomer/gr-fec_dev/build/python/fec_dev/bindings --filter gr::fec_dev

fec_dev_docstrings: python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings
fec_dev_docstrings: python/fec_dev/bindings/docstring_status
fec_dev_docstrings: python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/build.make
.PHONY : fec_dev_docstrings

# Rule to build all files generated by this target.
python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/build: fec_dev_docstrings
.PHONY : python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/build

python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/clean:
	cd /Users/kmcomer/gr-fec_dev/build/python/fec_dev/bindings && $(CMAKE_COMMAND) -P CMakeFiles/fec_dev_docstrings.dir/cmake_clean.cmake
.PHONY : python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/clean

python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/depend:
	cd /Users/kmcomer/gr-fec_dev/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kmcomer/gr-fec_dev /Users/kmcomer/gr-fec_dev/python/fec_dev/bindings /Users/kmcomer/gr-fec_dev/build /Users/kmcomer/gr-fec_dev/build/python/fec_dev/bindings /Users/kmcomer/gr-fec_dev/build/python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : python/fec_dev/bindings/CMakeFiles/fec_dev_docstrings.dir/depend
