import ROOT

c = ROOT.TCanvas('c', 'fit')
h_gaus = ROOT.TH1D('h_gaus', '', 100, -10, 10)
h_gaus.FillRandom('gaus', 2000)
h_gaus_f = ROOT.TF1('h_gaus_f', 'gaus', -1, 1)

h_gaus.Fit(h_gaus_f, 'R+', '', -1, 1)
mean = h_gaus_f.GetParameter(1)
sigma = h_gaus_f.GetParameter(2)
x_min = mean-6*sigma
x_max = mean+6*sigma
h_gaus.Fit(h_gaus_f, 'R+', '', x_min, x_max)

# h_gaus.SetAxisRange(x_min, x_max, "X")

c.SaveAs('python/test.pdf')
