# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.11

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake

# The command to remove a file.
RM = /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /hepustc/home/hengli/testarea/RPCRel21Prod/source

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /hepustc/home/hengli/testarea/RPCRel21Prod/build

# Utility rule file for PhysicsRPCProdConfigurables.

# Include the progress variables for this target.
include PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/progress.make

PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables: x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdConf.py
PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables: x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.confdb


x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdConf.py: x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.so
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/hepustc/home/hengli/testarea/RPCRel21Prod/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating ../x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdConf.py, ../x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.confdb"
	cd /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd && /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake -E make_directory /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd/genConf
	cd /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd && ../atlas_build_run.sh /cvmfs/atlas.cern.ch/repo/sw/software/21.0/GAUDI/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/bin/genconf.exe -o /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd/genConf -p PhysicsRPCProd --no-init -i libPhysicsRPCProd.so
	cd /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd && /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake -E copy /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd/genConf/PhysicsRPCProd.confdb /hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.confdb
	cd /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd && /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake -E make_directory /hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/python/PhysicsRPCProd
	cd /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd && /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake -E copy /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd/genConf/PhysicsRPCProdConf.py /hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdConf.py
	cd /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd && /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake -E touch /hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/__init__.py || :

x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.confdb: x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdConf.py
	@$(CMAKE_COMMAND) -E touch_nocreate x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.confdb

PhysicsRPCProdConfigurables: PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables
PhysicsRPCProdConfigurables: x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdConf.py
PhysicsRPCProdConfigurables: x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.confdb
PhysicsRPCProdConfigurables: PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/build.make

.PHONY : PhysicsRPCProdConfigurables

# Rule to build all files generated by this target.
PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/build: PhysicsRPCProdConfigurables

.PHONY : PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/build

PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/clean:
	cd /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd && $(CMAKE_COMMAND) -P CMakeFiles/PhysicsRPCProdConfigurables.dir/cmake_clean.cmake
.PHONY : PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/clean

PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/depend:
	cd /hepustc/home/hengli/testarea/RPCRel21Prod/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /hepustc/home/hengli/testarea/RPCRel21Prod/source /hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd /hepustc/home/hengli/testarea/RPCRel21Prod/build /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd /hepustc/home/hengli/testarea/RPCRel21Prod/build/PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : PhysicsRPCProd/CMakeFiles/PhysicsRPCProdConfigurables.dir/depend
