#include<fstream>
#include"TGraph.h"
#include"TCanvas.h"
#include"TAxis.h"
#include"TH1.h"
#include"TLegend.h"
#include"TF1.h"
#include"TMultiGraph.h"

using namespace std;

void hist20_100mV()
{
  gStyle->SetOptStat(1);
  gStyle->SetOptFit(1111);
  gStyle->SetTitleX(0.5);
  gStyle->SetPadGridX(kTRUE);
  gStyle->SetPadGridY(kTRUE);

  const Int_t n=8192;
  int data[n]={0};

   TCanvas *C=new TCanvas("C","C",600,500);
   TH1F *hist=new TH1F("hist","hist",n,0,n);    

   TString outputfilename="20mV_100mV.png";
   TString inputfilename="20_100mV1kHz1Vrange.txt";
   ifstream inputfile;

   ofstream output0("mean.txt",ios::app);
//   ofstream output1("peakchannel.txt",ios::app);
   ofstream output2("sigma.txt",ios::app);
//   ofstream output3("FWHM.txt",ios::app);

   Double_t par20[3],par30[3],par40[3],par50[3],par60[3],par70[3],par80[3],par90[3],par100[3];
   int i=-40;
        

//TF1 *f1=new TF1("Pedestal","gaus",1040,lowdown+5);
//     f1->SetLineColor(kCyan+1);
TF1 *f20=new TF1("peak20mV","gaus",1640+i,1715);
//     f1->SetLineColor(kCyan+1);
TF1 *f30=new TF1("peak30mV","gaus",1790+i,1875);
TF1 *f40=new TF1("peak40mV","gaus",1930+i,2015);
TF1 *f50=new TF1("peak50mV","gaus",2087+i,2163);
TF1 *f60=new TF1("peak60mV","gaus",2227+i,2307);
TF1 *f70=new TF1("peak70mV","gaus",2381+i,2464);
TF1 *f80=new TF1("peak80mV","gaus",2518+i,2605);
TF1 *f90=new TF1("peak90mV","gaus",2667+i,2755);
TF1 *f100=new TF1("peak100mV","gaus",2793+i,3074);
	
	hist->GetXaxis()->SetTitle("channel");
	hist->GetYaxis()->SetTitle("counts");
	hist->SetLineWidth(2);
	hist->SetMarkerSize(2);
	hist->SetLineColor(kBlack);
//	hist->SetTitle("squar=20mV_100mV");

   inputfile.open(inputfilename);

		for(int k=0;k<n;k++)
		{
			inputfile>>data[k];
		//	if(k%1000==0)cout<<k<<"  "<<data[k]<<endl;
                        hist->SetBinContent(k,data[k]);
		}
        cout<<"Hello!"<<endl;
   inputfile.close();
 	C->cd();
	hist->Draw();
	hist->Fit(f20,"R");
	hist->Fit(f30,"R+");
	hist->Fit(f40,"R+");
	hist->Fit(f50,"R+");
	hist->Fit(f60,"R+");
	hist->Fit(f70,"R+");
	hist->Fit(f80,"R+");
	hist->Fit(f90,"R+");
	hist->Fit(f100,"R+");
	f20->GetParameters(&par20[0]);
//	f20->SetParameters(&par[0]);
//	hist->Fit(f20,"R");
	f30->GetParameters(&par30[0]);
	f40->GetParameters(&par40[0]);
	f50->GetParameters(&par50[0]);
	f60->GetParameters(&par60[0]);
	f70->GetParameters(&par70[0]);
	f80->GetParameters(&par80[0]);
	f90->GetParameters(&par90[0]);
	f100->GetParameters(&par100[0]);


	output0 << par20[1] <<endl;
	output0 << par30[1] <<endl;
	output0 << par40[1] <<endl;
	output0 << par50[1] <<endl;
	output0 << par60[1] <<endl;
	output0 << par70[1] <<endl;
	output0 << par80[1] <<endl;
	output0 << par90[1] <<endl;
	output0 << par100[1] <<endl;

	output2 << par20[2] <<endl;
	output2 << par30[2] <<endl;
	output2 << par40[2] <<endl;
	output2 << par50[2] <<endl;
	output2 << par60[2] <<endl;
	output2 << par70[2] <<endl;
	output2 << par80[2] <<endl;
	output2 << par90[2] <<endl;
	output2 << par100[2] <<endl;
	hist->GetXaxis()->SetRangeUser(1600,2900);
C->SaveAs(outputfilename);	
	output0.close();
	output2.close();
	
	return;
}

