/* -*- c++ -*- */
/*
 * Copyright 2014 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "turbo_decoder_impl.h"
#include <volk/volk.h>
#include <cmath>
#include <cstdio>
#include <sstream>
#include <vector>

namespace gr {
namespace fec_dev {

fec::generic_decoder::sptr turbo_decoder::make(int frame_size)
{
    return fec::generic_decoder::sptr(new turbo_decoder_impl(frame_size));
}

turbo_decoder_impl::turbo_decoder_impl(int frame_size) : generic_decoder("turbo_decoder")
{
    // Set max frame size here; all buffers and settings will be
    // based on this value.
    d_max_frame_size = frame_size;
    set_frame_size(frame_size);
}

turbo_decoder_impl::~turbo_decoder_impl() {}

int turbo_decoder_impl::get_output_size()
{
    // unpacked bits
    return d_frame_size;
}

int turbo_decoder_impl::get_input_size() { return d_frame_size; }

int turbo_decoder_impl::get_input_item_size() { return sizeof(float); }

const char* turbo_decoder_impl::get_input_conversion() { return "none"; }

bool turbo_decoder_impl::set_frame_size(unsigned int frame_size)
{
    bool ret = true;
    if (frame_size > d_max_frame_size) {
        d_logger->info("tried to set frame to {:d}; max possible is {:d}",
                       frame_size,
                       d_max_frame_size);
        frame_size = d_max_frame_size;
        ret = false;
    }

    d_frame_size = frame_size;

    return ret;
}

double turbo_decoder_impl::rate() { return 1.0; }

void turbo_decoder_impl::generic_work(const void* inbuffer, void* outbuffer)
{
    const float* in = (const float*)inbuffer;
    int* out = (int*)outbuffer;

    int K = d_frame_size;
    int trellis_size = 8;
    int N = 3*K + 4*std::log2(trellis_size);
    int n_ite = 6;
    aff3ct::tools::Interleaver_core_LTE<> core(K);
	aff3ct::module::Interleaver<float> pi(core);
    bool buffered_enc = true;

    auto siso_n = aff3ct::module::Decoder_SISO<>(K, N);
    auto siso_i = siso_n;

    auto decoder = std::unique_ptr<aff3ct::factory::Decoder_turbo<>>(new aff3ct::factory::Decoder_turbo<>(K, N, n_ite, siso_n, siso_i, pi, buffered_enc));
    // decoder->decode_siho(in, out, -1);
    // auto codec = std::unique_ptr<aff3ct::tools::Codec_turbo<>>(new aff3ct::tools::Codec_turbo<>(K,N);
    memcpy(out, in, d_frame_size*sizeof(char));
}

} /* namespace fec */
} /* namespace gr */
