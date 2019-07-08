import ROOT

c = ROOT.TCanvas('c', 'c',800, 600)
li = []*10
li2 = []*10
for i in range(10):
    li.append(i)
    li2.append(10*i)

    cut = ROOT.TCutG('cut',i, li, li2)
cut.Draw()
c.SaveAs(li.pdf)
