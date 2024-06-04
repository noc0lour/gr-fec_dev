/* -*- c++ -*- */
/*
 * Copyright 2024 gr-fec_dev author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FEC_DEV_TURBO_ENCODER_IMPL_H
#define INCLUDED_FEC_DEV_TURBO_ENCODER_IMPL_H

#include <gnuradio/fec_dev/turbo_encoder.h>

namespace gr {
  namespace fec_dev {

    class turbo_encoder_impl : public turbo_encoder
    {
     private:
      // plug into the generic fec api
      void generic_work(const void* inbuffer, void* outbuffer) override;
      int get_output_size() override;
      int get_input_size() override;
      const char* get_input_conversion() override;
      const char* get_output_conversion() override;
      bool d_pack_input;
      bool d_packed_bits_output;

      unsigned int d_max_frame_size;
      unsigned int d_frame_size;

     public:
      turbo_encoder_impl();
      ~turbo_encoder_impl();

      bool set_frame_size(unsigned int frame_size) override;
      double rate() override;
    };

  } // namespace fec_dev
} // namespace gr

#endif /* INCLUDED_FEC_DEV_TURBO_ENCODER_IMPL_H */
