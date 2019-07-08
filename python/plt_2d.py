 #!/usr/bin/env python
import sys
import os
import math
import ROOT

logdir = sys.argv[1:]
print logdir

x = 0
y = 0
i = 0
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

time_res = [[50, 17.0606, 25.8994, 22.5078], [60, 9.9838, 15.8277, 22.1209], [70, 7.8538, 12.6262, 17.3104], [80, 10.8186, 17.2163, 21.7210], [90, 5.2731, 7.9824, 10.2016], [100, 4.1745, 5.6455, 8.8109], [110, 3.6977, 5.3895, 6.8795], [130, 2.7201, 4.6389, 5.7128], [140, 2.5229, 4.0905, 5.3936]]
gr_60p = ROOT.TH2F('h_30p', '', 100, 40, 150, 100, 0, 75)
gr_70p = ROOT.TH2F('h_30p', '', 100, 40, 150, 100, 0, 75)
gr_80p = ROOT.TH2F('h_30p', '', 100, 40, 150, 100, 0, 75)
gr_90p = ROOT.TH2F('h_30p', '', 100, 40, 150, 100, 0, 75)
# h_50p = ROOT.TH2F('h_50p', '', 100, 40, 150, 100, 0, 75)
# h_70p = ROOT.TH2F('h_70p', '', 100, 40, 150, 100, 0, 75)
# h_90p = ROOT.TH2F('h_70p', '', 100, 40, 150, 100, 0, 75)
# for i in range(len(time_res)):
#     x = time_res[i][0]
#     y_30p = time_res[i][1] * 2.355
#     y_50p = time_res[i][2] * 2.355
#     y_70p = time_res[i][3] * 2.355
#     h_30p.Fill(x, y_30p)
#     h_50p.Fill(x, y_50p)
#     h_70p.Fill(x, y_70p)

# gr = ROOT.TGraph(h_30p)
# gr.Draw('alp')

# h_30p.SetTitle("")
# h_30p.SetMarkerColor(4)
# h_30p.SetLineColor(4)
# h_30p.SetMarkerSize(1)
# h_30p.SetMarkerStyle(20)
# h_50p.SetMarkerColor(6)
# h_50p.SetLineColor(6)
# h_50p.SetMarkerSize(1)
# h_50p.SetMarkerStyle(22)
# h_70p.SetMarkerColor(4)
# h_70p.SetLineColor(4)
# h_70p.SetMarkerSize(1)
# h_70p.SetMarkerStyle(26)

gr_60p.SetMarkerColor(2)
gr_60p.SetLineColor(2)
gr_60p.SetLineWidth(2)
gr_60p.SetMarkerSize(1)
gr_60p.SetMarkerStyle(21)
gr_70p.SetMarkerColor(4)
gr_70p.SetLineColor(4)
gr_70p.SetLineWidth(2)
gr_70p.SetMarkerSize(1)
gr_70p.SetMarkerStyle(33)
gr_80p.SetMarkerColor(8)
gr_80p.SetLineColor(8)
gr_80p.SetLineWidth(2)
gr_80p.SetMarkerSize(1)
gr_80p.SetMarkerStyle(20)
gr_90p.SetMarkerColor(6)
gr_90p.SetLineColor(6)
gr_90p.SetLineWidth(2)
gr_90p.SetMarkerSize(1)
gr_90p.SetMarkerStyle(22)


# h_30p.Draw('al')
# h_50p.Draw('same')
# h_70p.Draw('same')

# h_30p.GetYaxis().SetTitle()
# h_30p.GetYaxis().SetTitleOffset(1.5)
# # h_30p.GetXaxis().CenterTitle()
# # h_30p.GetYaxis().CenterTitle()
# h_30p.GetXaxis().SetTitle('time/ps')
# h_30p.GetYaxis().SetTitle('Event')
# h_30p.GetXaxis().SetTitleOffset(1.0)
# h_30p.GetYaxis().SetTitleOffset(1.0)
# h_30p.GetXaxis().SetTitleSize(0.05)
# h_30p.GetYaxis().SetTitleSize(0.05)
# h_30p.GetXaxis().SetLabelSize(0.05)
# h_30p.GetYaxis().SetLabelSize(0.05)
# h_30p.GetYaxis().SetNdivisions(505)
# h_30p.GetYaxis().SetNdivisions(505)

# legend = ROOT.TLegend(0.5, 0.68, 0.83, 0.88)

# legend.AddEntry(h_30p, "30% rising edge")
# legend.AddEntry(h_50p, "50% rising edge")
# legend = ROOT.TLegend(0.2, 0.72, 0.43, 0.88)
# legend.AddEntry(h_30p, "70V")
# legend.AddEntry(h_50p, "90V")

legend = ROOT.TLegend(0.2, 0.58, 0.43, 0.88)
# legend = ROOT.TLegend(0.2, 0.58, 0.43, 0.88)
legend.AddEntry(gr_60p, "70V")
legend.AddEntry(gr_70p, "90V")
legend.AddEntry(gr_80p, "110V")
legend.AddEntry(gr_90p, "130V")

legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.Draw()

figfile = 'python/plots/time_res.pdf'
c.SaveAs(figfile)
