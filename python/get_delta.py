#!/usr/bin/env python

import sys
import os
import math
import ROOT 
from array import array

args = sys.argv[1:]
if len(args) < 3:
    print 'input error'

infile = args[0]
outfile = args[1]
per = args[2]

if '0.2' in per:
    percent = 0.7
elif '0.5' in per:
    percent = 0.5
elif '0.7' in per:
    percent = 0.7
else:
    print 'input per error'

fin = ROOT.TFile(infile)
t = fin.Get('tree')
entries = t.GetEntriesFast()
print 'entries = ', entries

fout = ROOT.TFile(outfile, 'RECREATE')
t_out = ROOT.TTree('signal', 'signal')

C2_amp_i = -1
C3_amp_i = -1
C2_amp_per = -1
C3_amp_per = -1
n = array('i', [0])
C2_time = array('d', [0])
C2_amp = array('d', [0])
C3_time = array('d', [0])
C3_amp = array('d', [0])
delta_t = array('d', [0])
h_delta_t = ROOT.TH1D('h_delta_t', 'delta_t', 30, 2.5e-10, 4e-10)
# t_out.Branch("n", n, "n/I")
t_out.Branch("C2_time", C2_time, "C2_time[195]/D")
t_out.Branch("C2_amp", C2_amp, "C2_amp[195]/D")
t_out.Branch("C3_time", C3_time, "C3_time[195]/D")
t_out.Branch("C3_amp", C3_amp, "C3_amp[195]/D")
t_out.Branch('delta_t', delta_t, 'delta_t[195]/D')

for jentry in xrange(entries):
    nb = t.GetEntry(jentry)

    C2_amp_min = min(t.C2_amp)
    C2_amp_max =max(t.C2_amp)
    C2_amp_percent =C2_amp_min + (C2_amp_max - C2_amp_min)*percent

    C3_amp_min = min(t.C3_amp)
    C3_amp_max =max(t.C3_amp)
    C3_amp_percent = C3_amp_min + (C3_amp_max - C3_amp_min)*percent

    for i in range(0, 195):
        if (t.C2_amp[i]<=C2_amp_percent and t.C2_amp[i+1]>C2_amp_percent ):
            C2_amp_i = i
        if (t.C3_amp[i]<=C3_amp_percent and t.C3_amp[i+1]>C3_amp_percent ):
            C3_amp_i = i

    delta_t = t.C2_time[C2_amp_i] - t.C3_time[C3_amp_i]
    # print delta_t
    h_delta_t.Fill(delta_t)
    t_out.Fill()

t_out.Write()
h_delta_t.Write()
fout.Close()
