import sys
import os
import ROOT
from ROOT import gPad,gStyle
from ROOT import TGraph,TCanvas,TPad,TMultiGraph

# name = "DNL-Bonding-Laser-BV170-BV60-IV_190507"
# fname = []
# fname.append('bonding_BV60_IV_LaserOn_190506')
# mg = TMultiGraph("mg","")

infile = sys.argv[1:]
print infile

for i in infile:
   x = i
   print x

# for iFile in fname:
#    g = TGraph(iFile+".csv","-%lf,%*lf,-%lf")
#    g.SetMarkerStyle(8)
#    g.SetMarkerSize(0.8)
#    mg.Add(g)
#    print g,iFile

# c = TCanvas("c", "canvas", 800, 600)
# c.cd()
# gPad.SetLogy()
# mg.SetTitle(name+";Bias Voltage [V];Measured Current [A]")
# mg.Draw("APL PMC PLC")
# mg.GetHistogram().GetYaxis().SetRangeUser(1E-10,0.001)
# mg.GetHistogram().GetXaxis().SetRangeUser(0,500);
# c.BuildLegend(0.5,0.4,0.7,0.8,"PL")

# c.Print(name+".pdf")
