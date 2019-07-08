#include<fstream>
#include"TTree.h"
#include"TFile.h"

using namespace std;

void filltree()
{
    // TString in_c2;
    // TString in_c3;
	char inputfilename_c2[5];
	char inputfilename_c3[5];
	int n;
	double C2_time[195] = {0};
	double C2_amp[195] = {0};
	double C3_time[195] = {0};
	double C3_amp[195] = {0};

	TFile* m_fout;
	TTree* m_tree;
// 	m_fout = new TFile("test.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/50.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/60.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/70.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/80.root", "RECREATE");
	m_fout = new TFile("root/lgad2/80_q5000.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/80_h5000.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/90.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/100.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/110.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/130.root", "RECREATE");
	// m_fout = new TFile("root/lgad2/140.root", "RECREATE");

	// m_fout = new TFile("root/lgad1/30.root", "RECREATE");
	// m_fout = new TFile("root/lgad1/40.root", "RECREATE");
	// m_fout = new TFile("root/lgad1/50.root", "RECREATE");
	// m_fout = new TFile("root/lgad1/60.root", "RECREATE");
	// m_fout = new TFile("root/lgad1/70.root", "RECREATE");
	// m_fout = new TFile("root/lgad1/80.root", "RECREATE");
	// m_fout = new TFile("root/lgad1/90.root", "RECREATE");
	m_tree = new TTree("tree", "tree");
	m_tree->Branch("n", &n, "n/I");
	m_tree->Branch("C2_time", C2_time, "C2_time[195]/D");
	m_tree->Branch("C2_amp", C2_amp, "C2_amp[195]/D");
	m_tree->Branch("C3_time", C3_time, "C3_time[195]/D");
	m_tree->Branch("C3_amp", C3_amp, "C3_amp[195]/D");

	for(n=0; n<10; n++){
	// for(n=0; n<20000; n++){
		// cout<<"enter loop"<<endl;

		ifstream inputfile_c2;
		ifstream inputfile_c3;
		//sprintf(inputfilename_c2, "data/LGAD2/100/C2_00000.txt");
		//sprintf(inputfilename_c3, "data/LGAD2/100/C3_00000.txt");
		 //sprintf(inputfilename_c2, "data/LGAD1/60/C2_00000.txt");
		 //sprintf(inputfilename_c3, "data/LGAD1/60/C3_00000.txt");
        //  in_c2 = Form("data/LGAD1/60/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD2/50/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD2/50/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD2/60/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD2/60/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD2/70/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD2/70/C3_%05d.txt",n);
		sprintf(inputfilename_c2, "data/LGAD2/80/C2_%05d.txt",n);
		sprintf(inputfilename_c3, "data/LGAD2/80/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD2/90/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD2/90/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD2/100/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD2/100/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD2/110/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD2/110/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD2/130/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD2/130/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD2/140/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD2/140/C3_%05d.txt",n);

		// sprintf(inputfilename_c2, "data/LGAD1/30/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD1/30/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD1/40/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD1/40/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD1/50/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD1/50/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD1/60/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD1/60/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD1/70/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD1/70/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD1/80/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD1/80/C3_%05d.txt",n);
		// sprintf(inputfilename_c2, "data/LGAD1/90/C2_%05d.txt",n);
		// sprintf(inputfilename_c3, "data/LGAD1/90/C3_%05d.txt",n);

	// 	cout<<inputfilename_c2<<endl;
	// 	cout<<inputfilename_c3<<endl;
		cout<<"n = "<<n<<endl;
		// if(n%1000==0){cout<<"n = "<<n<<endl;}

		inputfile_c2.open(inputfilename_c2);
        // inputfile_c2.open(in_c2);
		for(int i=0; i<195; i++){
			inputfile_c2>>C2_time[i];
			inputfile_c2>>C2_amp[i];
			// cout<<"C2 = "<<C2_time[i]<<endl;
		}
		inputfile_c2.close();

		inputfile_c3.open(inputfilename_c3);
		for(int ii=0; ii<195; ii++){
			inputfile_c3>>C3_time[ii];
			inputfile_c3>>C3_amp[ii];
			// cout<<"C3 = "<<C3[ii]<<endl;		
		}
		inputfile_c3.close();
		m_tree->Fill();
	}
	m_tree->Write();
	m_fout->cd();
	m_fout->Close();

}

