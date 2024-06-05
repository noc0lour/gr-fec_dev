/* -*- c++ -*- */
/*
 * Copyright 2024 gr-fec_dev author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "turbo_encoder_impl.h"
#include <gnuradio/fec/generic_encoder.h>
#include <volk/volk.h>
#include <sstream>

namespace gr {
namespace fec_dev {

fec::generic_encoder::sptr turbo_encoder::make(int frame_size, bool pack, bool packed_bits)
{
    return fec::generic_encoder::sptr(new turbo_encoder_impl(frame_size, pack, packed_bits));
}


/*
* The private constructor
*/
turbo_encoder_impl::turbo_encoder_impl(int frame_size, bool pack, bool packed_bits)
    : generic_encoder("turbo_encoder"),
    d_pack_input(pack),
    d_packed_bits_output(packed_bits)
{
    d_max_frame_size = frame_size;
    set_frame_size(frame_size);
}

/*
* Our virtual destructor.
*/
turbo_encoder_impl::~turbo_encoder_impl()
{
}

int turbo_encoder_impl::get_output_size() { return d_frame_size; }

int turbo_encoder_impl::get_input_size() { return d_frame_size; }

const char* turbo_encoder_impl::get_input_conversion()
{
    return d_pack_input ? "pack" : "none";
}

const char* turbo_encoder_impl::get_output_conversion()
{
    return d_packed_bits_output ? "packed_bits" : "none";
}

bool turbo_encoder_impl::set_frame_size(unsigned int frame_size)
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

double turbo_encoder_impl::rate() { return 1.0; }

void turbo_encoder_impl::generic_work(const void* inbuffer, void* outbuffer)
{
    const unsigned char* in = (const unsigned char*)inbuffer;
    unsigned char* out = (unsigned char*)outbuffer;

    memcpy(out, in, d_frame_size * sizeof(char));
}

} /* namespace fec_dev */
} /* namespace gr */
