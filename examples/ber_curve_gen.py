#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Ber Curve Gen
# GNU Radio version: gac2244fa1

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import fec
import numpy
from gnuradio import fec_dev
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class ber_curve_gen(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ber Curve Gen", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ber Curve Gen")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ber_curve_gen")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.rate = rate = 2
        self.polys = polys = [79, 109]
        self.k = k = 7
        self.framebits = framebits = 4096
        self.esno_0 = esno_0 = numpy.arange(0, 8, .5)
        self.samp_rate_0 = samp_rate_0 = 35000000
        self.num_curves = num_curves = 5
        self.esno = esno = esno_0
        self.enc_turbo = enc_turbo = list(map((lambda b:list(map((lambda a: fec_dev.turbo_encoder_make(framebits)),range(0,1)))), range(0,len(esno_0))))
        self.enc_tpc = enc_tpc = list(map( (lambda b: list(map( ( lambda a: fec.tpc_encoder_make([3], [43], 26, 6, 9, 3)), range(0,1) ) ) ), range(0,len(esno_0))))
        self.enc_rep = enc_rep = list(map((lambda b: list(map((lambda a: fec.repetition_encoder_make(framebits, 3)), range(0,1)))),range(0,len(esno_0))))
        self.enc_ldpc = enc_ldpc = list(map( (lambda b: list( map( ( lambda a: fec.ldpc_encoder_make(gr.prefix() + "/share/gnuradio/fec/ldpc/271.127.3.112")), range(0,1) ) ) ), range(0,len(esno_0))))
        self.enc_dummy = enc_dummy = list(map((lambda b:list(map((lambda a: fec.dummy_encoder_make(framebits)),range(0,1)))), range(0,len(esno_0))))
        self.enc_cc = enc_cc = list(map( (lambda b:list(map( ( lambda a:fec.cc_encoder_make(framebits, k, rate, polys, 0, fec.CC_STREAMING, False)), range(0,1)))), range(0,len(esno_0))))
        self.dec_turbo = dec_turbo = list(map((lambda b: list(map((lambda a: fec_dev.turbo_decoder.make(framebits)), range(0,1)))), range(0,len(esno_0))))
        self.dec_tpc = dec_tpc = list(map( (lambda b: list(map( ( lambda a: fec.tpc_decoder_make([3], [43], 26, 6, 9, 3, 6, 1)), range(0,1)))), range(0,len(esno_0))))
        self.dec_rep = dec_rep = list(map( (lambda b: list( map( ( lambda a: fec.repetition_decoder.make(framebits,3, 0.5)), range(0,1) ) ) ), range(0,len(esno_0))))
        self.dec_ldpc = dec_ldpc = list(map( (lambda b: list( map( ( lambda a: fec.ldpc_decoder.make(gr.prefix() + "/share/gnuradio/fec/ldpc/271.127.3.112", 50)), range(0,1) ) ) ), range(0,len(esno_0))))
        self.dec_dummy = dec_dummy = list(map((lambda b: list(map((lambda a: fec.dummy_decoder.make(framebits)), range(0,1)))), range(0,len(esno_0))))
        self.dec_cc = dec_cc = list(map( (lambda b: list(map(( lambda a: fec.cc_decoder.make(framebits, k, rate, polys, 0,(-1), fec.CC_STREAMING, False)), range(0,1) ) ) ), range(0,len(esno_0))))

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_bercurve_sink_0 = qtgui.ber_sink_b(
            esno_0, #range of esnos
            1, #number of curves
            1000, #ensure at least
            (-10), #cutoff
            [], #indiv. curve names
            None # parent
        )
        self.qtgui_bercurve_sink_0.set_update_time(0.10)
        self.qtgui_bercurve_sink_0.set_y_axis((-10), 0)
        self.qtgui_bercurve_sink_0.set_x_axis(esno_0[0], esno_0[-1])

        labels = ['None', 'Rep. (Rate=3)', 'CC (K=7, Rate=2)', 'LDPC', 'TPC',
            '', '', '', '', '']
        widths = [2, 2, 2, 2, 2,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "magenta", "dark red", "Dark Blue",
            "red", "red", "red", "red", "red"]
        alphas = [1, 1, 1, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 2, 5, 5, 4,
            0, 0, 0, 0, 0]
        markers = [0, 1, 0, 0, 0,
            0, 0, 0, 0, 0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_bercurve_sink_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_bercurve_sink_0.set_line_label(i, labels[i])
            self.qtgui_bercurve_sink_0.set_line_width(i, widths[i])
            self.qtgui_bercurve_sink_0.set_line_color(i, colors[i])
            self.qtgui_bercurve_sink_0.set_line_style(i, styles[i])
            self.qtgui_bercurve_sink_0.set_line_marker(i, markers[i])
            self.qtgui_bercurve_sink_0.set_line_alpha(i, alphas[i])

        self._qtgui_bercurve_sink_0_win = sip.wrapinstance(self.qtgui_bercurve_sink_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_bercurve_sink_0_win)
        self.fec_bercurve_generator_0_0_0 = fec.bercurve_generator(
            enc_turbo, #size
            dec_turbo, #name
            esno_0, #range of esnos
            samp_rate_0, #throttle
            "capillary", #threading mode
            '11', #puncture pattern
            (-100)) # noise gen. seed


        ##################################################
        # Connections
        ##################################################
        self.connect((self.fec_bercurve_generator_0_0_0, 0), (self.qtgui_bercurve_sink_0, 0))
        self.connect((self.fec_bercurve_generator_0_0_0, 1), (self.qtgui_bercurve_sink_0, 1))
        self.connect((self.fec_bercurve_generator_0_0_0, 2), (self.qtgui_bercurve_sink_0, 2))
        self.connect((self.fec_bercurve_generator_0_0_0, 3), (self.qtgui_bercurve_sink_0, 3))
        self.connect((self.fec_bercurve_generator_0_0_0, 4), (self.qtgui_bercurve_sink_0, 4))
        self.connect((self.fec_bercurve_generator_0_0_0, 5), (self.qtgui_bercurve_sink_0, 5))
        self.connect((self.fec_bercurve_generator_0_0_0, 6), (self.qtgui_bercurve_sink_0, 6))
        self.connect((self.fec_bercurve_generator_0_0_0, 7), (self.qtgui_bercurve_sink_0, 7))
        self.connect((self.fec_bercurve_generator_0_0_0, 8), (self.qtgui_bercurve_sink_0, 8))
        self.connect((self.fec_bercurve_generator_0_0_0, 9), (self.qtgui_bercurve_sink_0, 9))
        self.connect((self.fec_bercurve_generator_0_0_0, 10), (self.qtgui_bercurve_sink_0, 10))
        self.connect((self.fec_bercurve_generator_0_0_0, 11), (self.qtgui_bercurve_sink_0, 11))
        self.connect((self.fec_bercurve_generator_0_0_0, 12), (self.qtgui_bercurve_sink_0, 12))
        self.connect((self.fec_bercurve_generator_0_0_0, 13), (self.qtgui_bercurve_sink_0, 13))
        self.connect((self.fec_bercurve_generator_0_0_0, 14), (self.qtgui_bercurve_sink_0, 14))
        self.connect((self.fec_bercurve_generator_0_0_0, 15), (self.qtgui_bercurve_sink_0, 15))
        self.connect((self.fec_bercurve_generator_0_0_0, 16), (self.qtgui_bercurve_sink_0, 16))
        self.connect((self.fec_bercurve_generator_0_0_0, 17), (self.qtgui_bercurve_sink_0, 17))
        self.connect((self.fec_bercurve_generator_0_0_0, 18), (self.qtgui_bercurve_sink_0, 18))
        self.connect((self.fec_bercurve_generator_0_0_0, 19), (self.qtgui_bercurve_sink_0, 19))
        self.connect((self.fec_bercurve_generator_0_0_0, 20), (self.qtgui_bercurve_sink_0, 20))
        self.connect((self.fec_bercurve_generator_0_0_0, 21), (self.qtgui_bercurve_sink_0, 21))
        self.connect((self.fec_bercurve_generator_0_0_0, 22), (self.qtgui_bercurve_sink_0, 22))
        self.connect((self.fec_bercurve_generator_0_0_0, 23), (self.qtgui_bercurve_sink_0, 23))
        self.connect((self.fec_bercurve_generator_0_0_0, 24), (self.qtgui_bercurve_sink_0, 24))
        self.connect((self.fec_bercurve_generator_0_0_0, 25), (self.qtgui_bercurve_sink_0, 25))
        self.connect((self.fec_bercurve_generator_0_0_0, 26), (self.qtgui_bercurve_sink_0, 26))
        self.connect((self.fec_bercurve_generator_0_0_0, 27), (self.qtgui_bercurve_sink_0, 27))
        self.connect((self.fec_bercurve_generator_0_0_0, 28), (self.qtgui_bercurve_sink_0, 28))
        self.connect((self.fec_bercurve_generator_0_0_0, 29), (self.qtgui_bercurve_sink_0, 29))
        self.connect((self.fec_bercurve_generator_0_0_0, 30), (self.qtgui_bercurve_sink_0, 30))
        self.connect((self.fec_bercurve_generator_0_0_0, 31), (self.qtgui_bercurve_sink_0, 31))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ber_curve_gen")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_framebits(self):
        return self.framebits

    def set_framebits(self, framebits):
        self.framebits = framebits

    def get_esno_0(self):
        return self.esno_0

    def set_esno_0(self, esno_0):
        self.esno_0 = esno_0
        self.set_esno(self.esno_0)

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_num_curves(self):
        return self.num_curves

    def set_num_curves(self, num_curves):
        self.num_curves = num_curves

    def get_esno(self):
        return self.esno

    def set_esno(self, esno):
        self.esno = esno

    def get_enc_turbo(self):
        return self.enc_turbo

    def set_enc_turbo(self, enc_turbo):
        self.enc_turbo = enc_turbo

    def get_enc_tpc(self):
        return self.enc_tpc

    def set_enc_tpc(self, enc_tpc):
        self.enc_tpc = enc_tpc

    def get_enc_rep(self):
        return self.enc_rep

    def set_enc_rep(self, enc_rep):
        self.enc_rep = enc_rep

    def get_enc_ldpc(self):
        return self.enc_ldpc

    def set_enc_ldpc(self, enc_ldpc):
        self.enc_ldpc = enc_ldpc

    def get_enc_dummy(self):
        return self.enc_dummy

    def set_enc_dummy(self, enc_dummy):
        self.enc_dummy = enc_dummy

    def get_enc_cc(self):
        return self.enc_cc

    def set_enc_cc(self, enc_cc):
        self.enc_cc = enc_cc

    def get_dec_turbo(self):
        return self.dec_turbo

    def set_dec_turbo(self, dec_turbo):
        self.dec_turbo = dec_turbo

    def get_dec_tpc(self):
        return self.dec_tpc

    def set_dec_tpc(self, dec_tpc):
        self.dec_tpc = dec_tpc

    def get_dec_rep(self):
        return self.dec_rep

    def set_dec_rep(self, dec_rep):
        self.dec_rep = dec_rep

    def get_dec_ldpc(self):
        return self.dec_ldpc

    def set_dec_ldpc(self, dec_ldpc):
        self.dec_ldpc = dec_ldpc

    def get_dec_dummy(self):
        return self.dec_dummy

    def set_dec_dummy(self, dec_dummy):
        self.dec_dummy = dec_dummy

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc




def main(top_block_cls=ber_curve_gen, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
