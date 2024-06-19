/* -*- c++ -*- */
/*
 * Copyright 2024 gr-fec_dev author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_FEC_DEV_TURBO_ENCODER_IMPL_H
#define INCLUDED_FEC_DEV_TURBO_ENCODER_IMPL_H

#include <gnuradio/fec_dev/turbo_encoder.h>
#include <aff3ct.hpp>
#include <map>
#include <string>

namespace gr {
namespace fec_dev {
    
class FEC_API turbo_encoder_impl : public turbo_encoder
{
private:
  // plug into the generic fec api
  void generic_work(const void* inbuffer, void* outbuffer) override;

  unsigned int d_frame_size;
  unsigned int d_max_frame_size;
  std::vector<int> d_polys;
  enc_standard_t d_standard;
  enc_sub_type_t d_subencoder;
  bool d_buffered;
  int d_output_size;
  int d_trellis_size;

public:
  turbo_encoder_impl(int frame_size,
                     enc_standard_t standard=LTE,
                     enc_sub_type_t subencoder=RSC,
                     bool buffered=true,
                     std::vector<int> polys={013,015},
                     int trellis_size = 8);
  ~turbo_encoder_impl() override;

  bool set_frame_size(unsigned int frame_size) override;
  double rate() override;
  int get_output_size() override;
  int get_input_size() override;
};

} // namespace fec_dev
} // namespace gr

#endif /* INCLUDED_FEC_DEV_TURBO_ENCODER_IMPL_H */
