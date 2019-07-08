 #!/usr/bin/env python
import sys
import os
import math
import ROOT
from array import array

logdir = sys.argv[1:]
print logdir

c = ROOT.TCanvas('c', '', 800, 600)
c.SetFillColor(0)
c.SetFrameFillColor(0)
ROOT.gStyle.SetPadColor(0)
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetOptStat(0)
c.SetLeftMargin(0.15)
c.SetRightMargin(0.15)
c.SetTopMargin(0.1)
c.SetBottomMargin(0.15)

mg = ROOT.TMultiGraph("mg","")

x17 = array('d')
x6 = array('d')
y17_30 = array('d')
y17_50 = array('d')
y17_70 = array('d')
y6_30  = array('d')
y6_50  = array('d')
y6_70  = array('d')

xv = array('d')
xt = array('d')
y6_60v = array('d')
y6t_70v = array('d')
y6_80v = array('d')
y17_70v = array('d')
y17_90v = array('d')
y17_110v = array('d')
y17_130v = array('d')
y17t_130v = array('d')

path17 = 'root/lgad2_delta/txt/'
files17 = os.listdir(path17)
files17.sort()
# print files17
li17 =[]
for i in [50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 130.0, 140.0]:
    x17.append(i)
n17 = len(x17)
for file in files17:
    name = path17+file
    f = open(name)
    for i in f.readlines():
        li17.append(float(i))
y17_30_num = [0, 3, 9, 17, 23, 31, 37, 47, 55]
y17_50_num = [1, 4, 11, 18, 25, 32, 39, 49, 56]
y17_70_num = [2, 5, 13, 19, 27, 33, 41, 51, 57]

y17_70v_num  = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y17_90v_num  = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
y17_110v_num = [34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
y17_130v_num = [44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
for i in y17_30_num:
    # print files17[i]
    y17_30.append(li17[i])
for i in y17_50_num:
    # print files17[i]
    y17_50.append(li17[i])
for i in y17_70_num:
    # print files17[i]
    y17_70.append(li17[i])
for i in y17_70v_num:
    # print files17[i]
    y17_70v.append(li17[i])
for i in y17_90v_num:
    # print files17[i]
    y17_90v.append(li17[i])
for i in y17_110v_num:
    # print files17[i]
    y17_110v.append(li17[i])
for i in y17_130v_num:
    # print files17[i]
    y17_130v.append(li17[i])
###########
path17trigger = 'root/lgad2_delta/txt_trigger/'
files17trigger = os.listdir(path17trigger)
files17trigger.sort()
li17trigger =[]
for file in files17trigger:
    name = path17trigger+file
    f = open(name)
    for i in f.readlines():
        li17trigger.append(float(i))
y17t_130_num = [0, 1, 2, 3 ,4, 5, 6, 7, 8]

for i in y17t_130_num:
    # print files17[i]
    y17t_130v.append(li17trigger[i])
# print y17t_130v

path6trigger = 'root/lgad1_delta/txt_trigger/'
files6trigger = os.listdir(path6trigger)
files6trigger.sort()
li6trigger =[]
for file in files6trigger:
    name = path6trigger+file
    f = open(name)
    for i in f.readlines():
        li6trigger.append(float(i))
y6t_70_num = [0, 1, 2, 3 ,4, 5, 6, 7, 8]

for i in y6t_70_num:
    # print files6[i]
    y6t_70v.append(li6trigger[i])
# print y6t_70v

#############
path6 = 'root/lgad1_delta/txt/'
files6 = os.listdir(path6)
files6.sort()
# print files6
li6 =[]
for i in [30, 40, 50, 60, 70, 80, 90]:
    x6.append(i)
n6 = len(x6)
for file in files6:
    name = path6+file
    f = open(name)
    for i in f.readlines():
        li6.append(float(i))
y6_30_num = [0, 4, 8, 14, 22, 28, 36]
y6_50_num = [1, 5, 9, 16, 23, 30, 37]
y6_70_num = [2, 6, 10, 18, 24, 32, 38]

for i in [5, 10, 20, 30, 40, 50, 60, 70, 80, 90]:
    xv.append(i)
nv = len(xv)

for i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
    xt.append(i)
nt = len(xt)

y6_60v_num = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y6_80v_num = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
for i in y6_30_num:
    # print files6[i]
    y6_30.append(li6[i])
for i in y6_50_num:
    # print files6[i]
    y6_50.append(li6[i])
for i in y6_70_num:
    # print files6[i]
    y6_70.append(li6[i])
for i in y6_60v_num:
    # print files6[i]
    y6_60v.append(li6[i])
for i in y6_80v_num:
    # print files6[i]
    y6_80v.append(li6[i])

if logdir in [['vol']]:
    gr17_30p = ROOT.TGraph(n17, x17, y17_30)
    gr17_50p = ROOT.TGraph(n17, x17, y17_50)
    gr17_70p = ROOT.TGraph(n17, x17, y17_70)
    gr6_30p  = ROOT.TGraph(n6, x6, y6_30)
    gr6_50p  = ROOT.TGraph(n6, x6, y6_50)
    gr6_70p  = ROOT.TGraph(n6, x6, y6_70)
elif logdir in [['per']]:
    gr17_30p  = ROOT.TGraph(nv, xv, y17_70v)
    gr17_50p  = ROOT.TGraph(nv, xv, y17_90v)
    gr17_70p  = ROOT.TGraph(nv, xv, y17_110v)
    gr6_30p   = ROOT.TGraph(nv, xv, y17_130v)
    gr6_50p   = ROOT.TGraph(nv, xv, y6_60v)
    gr6_70p   = ROOT.TGraph(nv, xv, y6_80v)
elif logdir in [['trig']]:
    gr17_30p  = ROOT.TGraph(nt, xt, y17t_130v)
    gr17_50p  = ROOT.TGraph(nt, xt, y6t_70v)
else:
    print 'input error'

mg.Add(gr17_30p)
mg.Add(gr17_50p)
if logdir in [['vol'], ['per']]:
    mg.Add(gr17_70p)
    mg.Add(gr6_30p)
    mg.Add(gr6_50p)
    mg.Add(gr6_70p)
mg.Draw('alp')
gr17_30p.SetLineWidth(2)
gr17_30p.SetMarkerSize(1)
gr17_50p.SetLineWidth(2)
gr17_50p.SetMarkerSize(1)
if logdir in [['vol'], ['per']]:
    gr17_70p.SetLineWidth(2)
    gr17_70p.SetMarkerSize(1)
    gr6_30p.SetLineWidth(2)
    gr6_30p.SetMarkerSize(1)
    gr6_50p.SetLineWidth(2)
    gr6_50p.SetMarkerSize(1)
    gr6_70p.SetLineWidth(2)
    gr6_70p.SetMarkerSize(1)

# mg.GetXaxis().CenterTitle()
# mg.GetYaxis().CenterTitle()
mg.GetYaxis().SetTitle('Time resolution/s')
mg.GetXaxis().SetTitleOffset(1.0)
mg.GetYaxis().SetTitleOffset(1.0)
mg.GetXaxis().SetTitleSize(0.05)
mg.GetYaxis().SetTitleSize(0.05)
mg.GetXaxis().SetLabelSize(0.05)
mg.GetYaxis().SetLabelSize(0.05)
mg.GetYaxis().SetNdivisions(505)
mg.GetYaxis().SetNdivisions(505)

if logdir in [['vol']]:
    mg.GetYaxis().SetRangeUser(0, 7e-11)
    mg.GetXaxis().SetTitle('Voltage/V')
    legend = ROOT.TLegend(0.5, 0.5, 0.83, 0.88)
    gr17_50p.SetMarkerColor(ROOT.kCyan+3)
    gr17_50p.SetLineColor(ROOT.kCyan+3)
    gr17_50p.SetMarkerStyle(21)
    gr17_30p.SetMarkerColor(ROOT.kViolet+6)
    gr17_30p.SetLineColor(ROOT.kViolet+6)
    gr17_30p.SetMarkerStyle(20)
    gr17_70p.SetMarkerColor(ROOT.kOrange+7)
    gr17_70p.SetLineColor(ROOT.kOrange+7)
    gr17_70p.SetMarkerStyle(22)
    gr6_30p.SetMarkerColor(ROOT.kViolet+6)
    gr6_30p.SetLineColor(ROOT.kViolet+6)
    gr6_30p.SetMarkerStyle(20)
    gr6_70p.SetMarkerColor(ROOT.kOrange+7)
    gr6_70p.SetLineColor(ROOT.kOrange+7)
    gr6_70p.SetMarkerStyle(22)
    gr6_50p.SetMarkerColor(ROOT.kCyan+3)
    gr6_50p.SetLineColor(ROOT.kCyan+3)
    gr6_50p.SetMarkerStyle(21)
    gr6_30p.SetLineStyle(7)
    gr6_50p.SetLineStyle(7)
    gr6_70p.SetLineStyle(7)
    legend.AddEntry(gr17_30p, "CFD30 for BV170", "lp")
    legend.AddEntry(gr17_50p, "CFD50 for BV170", "lp")
    legend.AddEntry(gr17_70p, "CFD70 for BV170", "lp")
    legend.AddEntry(gr6_30p,  "CFD30 for BV60", "lp")
    legend.AddEntry(gr6_50p,  "CFD50 for BV60", "lp")
    legend.AddEntry(gr6_70p,  "CFD70 for BV60", "lp")
elif logdir in [['per']]:
    mg.GetYaxis().SetRangeUser(0, 5e-11)
    mg.GetXaxis().SetTitle('CFD for signal')
    gr17_50p.SetMarkerColor(ROOT.kCyan+3)
    gr17_50p.SetLineColor(ROOT.kCyan+3)
    gr17_50p.SetMarkerStyle(21)
    gr6_30p.SetMarkerColor(ROOT.kViolet+6)
    gr6_30p.SetLineColor(ROOT.kViolet+6)
    gr6_30p.SetMarkerStyle(20)
    gr6_70p.SetMarkerColor(ROOT.kOrange+7)
    gr6_70p.SetLineColor(ROOT.kOrange+7)
    gr6_70p.SetMarkerStyle(22)
    gr6_50p.SetLineStyle(7)
    gr6_70p.SetLineStyle(7)
    gr17_30p.SetMarkerColor(ROOT.kGreen+1)
    gr17_30p.SetLineColor(ROOT.kGreen+1)
    gr17_30p.SetMarkerStyle(24)
    gr17_70p.SetMarkerColor(ROOT.kBlue)
    gr17_70p.SetLineColor(ROOT.kBlue)
    gr17_70p.SetMarkerStyle(26)
    gr6_50p.SetMarkerColor(ROOT.kPink+10)
    gr6_50p.SetLineColor(ROOT.kPink+10)
    gr6_50p.SetMarkerStyle(25)
    legend = ROOT.TLegend(0.2, 0.7, 0.84, 0.89)
    legend.SetNColumns(2)
    legend.AddEntry(gr17_30p, "BV170 70V", "lp")
    legend.AddEntry(gr17_50p, "BV170 90V", "lp")
    legend.AddEntry(gr17_70p, "BV170 110V", "lp")
    legend.AddEntry(gr6_30p,  "BV170 130V", "lp")
    legend.AddEntry(gr6_50p,  "BV60 60V", "lp")
    legend.AddEntry(gr6_70p,  "BV60 80V", "lp")
elif logdir in [['trig']]:
    mg.GetYaxis().SetRangeUser(0, 4e-11)
    mg.GetXaxis().SetTitle('CFD for trig')
    gr17_30p.SetMarkerColor(ROOT.kGreen+1)
    gr17_30p.SetLineColor(ROOT.kGreen+1)
    gr17_30p.SetMarkerStyle(24)
    gr17_50p.SetMarkerColor(ROOT.kPink+10)
    gr17_50p.SetLineColor(ROOT.kPink+10)
    gr17_50p.SetMarkerStyle(22)
    gr17_50p.SetLineStyle(7)
    legend = ROOT.TLegend(0.5, 0.7, 0.78, 0.89)
    legend.AddEntry(gr17_30p, "BV170 130V", "lp")
    legend.AddEntry(gr17_50p, "BV60 70V", "lp")

legend.SetBorderSize(0)
legend.SetFillColor(0)
# legend.SetFillsStyle(303)
legend.Draw()

if logdir in [['vol']]:
    figfile = 'python/plots/graph_vol.pdf'
elif logdir in [['per']]:
    figfile = 'python/plots/graph_per.pdf'
elif logdir in [['trig']]:
    figfile = 'python/plots/graph_trig.pdf'
c.SaveAs(figfile)
