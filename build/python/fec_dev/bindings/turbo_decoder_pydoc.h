/*
 * Copyright 2024 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */
#include "pydoc_macros.h"
#define D(...) DOC(gr, fec_dev, __VA_ARGS__)
/*
  This file contains placeholders for docstrings for the Python bindings.
  Do not edit! These were automatically extracted during the binding process
  and will be overwritten during the build process
 */


static const char* __doc_gr_fec_dev_turbo_decoder = R"doc(Turbo Decoding class.

A turbo decoder class that simply passes the input to the output. It is meant to allow us to easily use the FEC API decoder and decoder blocks in an application with no coding.)doc";


static const char* __doc_gr_fec_dev_turbo_decoder_turbo_decoder_0 = R"doc()doc";


static const char* __doc_gr_fec_dev_turbo_decoder_turbo_decoder_1 = R"doc()doc";


static const char* __doc_gr_fec_dev_turbo_decoder_make = R"doc(Build a turbo encoding FEC API object.)doc";


static const char* __doc_gr_fec_dev_turbo_decoder_set_frame_size = R"doc(Sets the uncoded frame size to . If  is greater than the value given to the constructor, the frame size will be capped by that initial value and this function will return false. Otherwise, it returns true.)doc";


static const char* __doc_gr_fec_dev_turbo_decoder_rate = R"doc(Returns the coding rate of this decoder (it will always be 1).)doc";
