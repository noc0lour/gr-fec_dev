#!/bin/bash

rm -rf build
mkdir build
cmake -S ./ -B build -DCMAKE_BUILD_TYPE=DEBUG -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++
cd build && make && make install
