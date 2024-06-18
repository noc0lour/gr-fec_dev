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

    int N_rsc = 2 * (K+std::log2(trellis_size));
    auto enco_n = aff3ct::module::Encoder_RSC_generic_sys<>(K, N_rsc, true, {013, 015});
    auto enco_i = enco_n;

    auto trellis_n = enco_n.get_trellis();
    auto trellis_i = trellis_n;
    
    auto dec_n = aff3ct::module::Decoder_RSC_BCJR_seq_generic_std<>(K, trellis_n, buffered_enc);
    auto dec_i = aff3ct::module::Decoder_RSC_BCJR_seq_generic_std<>(K, trellis_i, buffered_enc);

    auto decoder = std::unique_ptr<aff3ct::module::Decoder_turbo_fast<>>(new aff3ct::module::Decoder_turbo_fast<>(K, N, n_ite, dec_n, dec_i, pi, buffered_enc));
    decoder->decode_siho(in, out, -1);
}

} /* namespace fec */
} /* namespace gr */
