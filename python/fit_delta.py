#!/usr/bin/env python

import sys
import os
import math
import ROOT 
from array import array

args = sys.argv[1:]
if len(args) < 4:
    print len(args)
    print 'input error'

infile = args[0]
outfile = args[1]
per = args[2:]

# percent_trig = 0.5
if   '10' in per :
    percent = 0.1
elif '5' in per :
    percent = 0.05
elif '20' in per :
    percent = 0.2
elif '30' in per :
    percent = 0.3
elif '40' in per :
    percent = 0.4
elif '50' in per :
    percent = 0.5
elif '60' in per :
    percent = 0.6
elif '70' in per :
    percent = 0.7
elif '80' in per :
    percent = 0.8
elif '90' in per :
    percent = 0.9

if   '10t' in per :
    percent_trig = 0.1
elif '20t' in per :
    percent_trig = 0.2
elif '30t' in per :
    percent_trig = 0.3
elif '40t' in per :
    percent_trig = 0.4
elif '50t' in per :
    percent_trig = 0.5
elif '60t' in per :
    percent_trig = 0.6
elif '70t' in per :
    percent_trig = 0.7
elif '80t' in per :
    percent_trig = 0.8
elif '90t' in per :
    percent_trig = 0.9

t_min = 0.5e-10
t_max = 11.5e-10

fin = ROOT.TFile(infile)
t = fin.Get('tree')
entries = t.GetEntriesFast()
print 'entries = ', entries

C2 = array('d', [0.])
C3 = array('d', [0.])
time_C2 = array('d')
amp_C2 = array('d')
time_C3 = array('d')
amp_C3 = array('d')
# FWHM = array('d', [])
fout = ROOT.TFile(outfile, 'RECREATE')
t_out = ROOT.TTree('signal', 'signal')
# t_out.Branch('FWHM', FWHM, 'FWHM/D')
# t_out.Branch('C2', C2, 'C2/D')
# t_out.Branch('C3', C3, 'C3/D')

t_min_fit = t_min + 0.1e-10
t_max_fit = t_max - 0.1e-10
h_delta_t = ROOT.TH1D('h_delta_t', 'delta_t', 396, t_min, t_max)
h_time_amp2 = ROOT.TH2D('h_time_amp2', 'h_time_amp2', 100,-2e-9, 4e-9, 100, -1e-2, 8e-2 )
h_time_amp3 = ROOT.TH2D('h_time_amp3', 'h_time_amp3', 100,-2e-9, 4e-9, 100, -0.1, 0.6 )
h_gaus = ROOT.TF1('h_gaus', 'gaus', 3e-10, 4e-10)

h_pol_00 = ROOT.TF1('h_pol_00', '[0]', 2e-10, 6e-10)
h_pol_0 = ROOT.TF1('h_pol_0', '[0]', 2e-10, 6e-10)
h_pol_11 = ROOT.TF1('h_pol_11', '[2]*x*x+[1]*x+[0]', 2e-10, 6e-10)
h_pol_1 = ROOT.TF1('h_pol_1', '[2]*x*x+[1]*x+[0]', 2e-10, 6e-10)

for jentry in xrange(entries):
    nb = t.GetEntry(jentry)

    ientry = t.LoadTree(jentry)
    # if ientry > 10:
    #     break

    # if (t.n < 14500 or t.n > 14510): 
    if (t.n < 14500): 
        continue

#     if (t.n != 10000 ): # 13.92
  #       continue
    h_time_amp2.Reset()
    h_time_amp3.Reset()
    h_pol_1.SetParameters(0.0, 0.0, 0.0)
    h_pol_11.SetParameters(0.0, 0.0, 0.0)
    for i in range(195):
        time_C2.append(t.C2_time[i])
        amp_C2.append(t.C2_amp[i])
        time_C3.append(t.C3_time[i])
        amp_C3.append(t.C3_amp[i])
    # h_time_amp2 = ROOT.TGraph(195, time_C2, amp_C2)
    # h_time_amp3 = ROOT.TGraph(195, time_C3, amp_C3)
        h_time_amp2.Fill(t.C2_time[i], t.C2_amp[i])
        h_time_amp3.Fill(t.C3_time[i], t.C3_amp[i])

    h_time_amp2.Fit(h_pol_0, "R+", "", -1.2e-9, -0.2e-9)
    C2_amp_min = h_pol_0.GetParameter(0)
    # C2_amp_min = 0.0
    C2_amp_max =max(t.C2_amp)
    half2 = C2_amp_min + (C2_amp_max - C2_amp_min)*percent
    pol_1_min = C2_amp_min + (C2_amp_max - C2_amp_min)*0.1
    pol_1_max = C2_amp_min + (C2_amp_max - C2_amp_min)*0.9
    # h_time_amp2.Fit(h_pol_1, "R+", "", 1.0e-10, 5.3e-10) #BV170
    # C2[0] = h_pol_1.GetX(half2, 0, 5.3e-10)
    h_time_amp2.Fit(h_pol_1, "R+", "", 0.9e-10, 8e-10) 
    pol_1_xmin = h_pol_1.GetX(pol_1_min, 0, 8e-10)
    pol_1_xmax = h_pol_1.GetX(pol_1_max, 0, 8e-10)
    h_time_amp2.Fit(h_pol_1, "R+", "", pol_1_xmin, pol_1_xmax) 
    C2[0] = h_pol_1.GetX(half2, 0, 8e-10)
    
    h_time_amp3.Fit(h_pol_00, "R+", "", -1.3e-9, -0.3e-9)
    C3_amp_min = h_pol_00.GetParameter(0)
    # C3_amp_min = 0.0
    C3_amp_max = max(t.C3_amp)
    half3 = C3_amp_min + (C3_amp_max - C3_amp_min)*percent_trig
    pol_11_min = C3_amp_min + (C3_amp_max - C3_amp_min)*0.1
    pol_11_max = C3_amp_min + (C3_amp_max - C3_amp_min)*0.9
    h_time_amp3.Fit(h_pol_11, "R+", "", -1e-10, 1.6e-10)
    pol_11_xmin = h_pol_11.GetX(pol_11_min, -1e-10, 1.6e-10)
    pol_11_xmax = h_pol_11.GetX(pol_11_max, -1e-10, 1.6e-10)
    h_time_amp3.Fit(h_pol_11, "R+", "",pol_11_xmin, pol_11_xmax)
    C3[0] = h_pol_11.GetX(half3, -1e-10, 1.5e-10)
    # t_out.Fill() 
    FWHM = C2[0] - C3[0] 

#     h_delta_t = ROOT.TGraph(195, C2[0], C3[0])
#     FWHM = h_pol_1.GetX(half2, 0, 5.3e-10, 1.0e-12) - h_pol_11.GetX(half3, -1e-10, 1.5e-10, 1.0e-12) 
    # FWHM = C2[0] 
#     print 'C2 = ', h_pol_1.GetX(half2, 0, 5.0e-10)
#     print 'C3 = ', h_pol_11.GetX(half3, 0, 1.5e-10)
#     print 'FWHM = ', FWHM
    h_delta_t.Fill(FWHM)
 
h_delta_t.Fit(h_gaus, "R", "", t_min_fit, t_max_fit)
mean = h_gaus.GetParameter(1)
sigma = h_gaus.GetParameter(2)
t_min_update = mean - 10*sigma
t_max_update = mean + 10*sigma
h_delta_t.Fit(h_gaus, "R", "", t_min_update, t_max_update)
h_delta_t.SetAxisRange(t_min_update, t_max_update, 'X')

txt_name = outfile+".txt"
txt_out = open(txt_name, 'w')
# txt_out.writelines(time)
out_list = []
out_list.append('%r' % sigma)
txt_out.writelines('\n'.join(out_list))
txt_out.close()

h_delta_t.Write()
# t_out.Write()
# h_time_amp2.Write()
# h_time_amp3.Write()
fout.Close()

