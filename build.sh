#!/bin/bash

rm -rf build
mkdir build
cmake -S ./ -B build
cd build && make && make install
