//M=1467392,n=1433
#include<exception>
void Qcharge(){
	
	    gStyle->SetOptStat(0);
        gStyle->SetOptFit(0000);
		gStyle->SetOptTitle(0);
        gStyle->SetStatX(0.9);
        gStyle->SetStatY(0.9);
        gStyle->SetStatH(0.15);
        gStyle->SetStatW(0.2);
        gStyle->SetStatStyle(0);
        gStyle->SetPadGridX(1);
        gStyle->SetPadGridY(1);
        //gStyle->SetTitleFont(132,"XYZ");
        //gStyle->SetTitleFont(132,"T");
        //gStyle->SetLabelFont(132,"XYZ");
        //gStyle->SetLabelSize(0.05,"XYZ");
        gStyle->SetTitleSize(0.05,"XYZ");
		gStyle->SetTitleSize(0.08,"T");
        //gStyle->SetTitleX(0.55);
        //gStyle->SetFillColor(kGreen);
        //gStyle->SetLabelColor(kRed,"XYZ");
        //gStyle->SetTitleColor(kRed,"XYZ");
       // gStyle->SetTitleColor(kRed,"T");
        //gStyle->SetAxisColor(kRed,"XYZ");
        //gStyle->SetFrameLineColor(kRed);
        gStyle->SetFuncWidth(2);
        gStyle->SetHistLineWidth(1);
		gStyle->SetFuncWidth(3);
        gStyle->SetFrameFillStyle(3003);
        //gStyle->SetFrameFillColor(kGreen);
        //gStyle->SetFuncColor(kBlue);
	//gStyle->SetTitleSize(0.07,"xyz");
        gStyle->SetTitleOffset(0.95,"xyz");
		gStyle->SetLabelOffset(0.01,"xyz");


	TFile *file=new TFile("tr.root","RECREATE");
	TTree *wf=new TTree("wf","wave form from Rigol");
	wf->SetMarkerStyle(7);
	wf->SetMarkerSize(70);
	const int wfn=1.3e4, pn=592;
	ifstream inputfile;
	ofstream output("charge spectrum.txt",ios::trunc);


 	float amp[591],mean,charge,Q,dt=0;
	//int f;
	//wf->Branch("f",&f,"f/I");
	wf->Branch("mean",&mean,"mean/F");
	wf->Branch("amp",amp,"amp[591]/F");
	wf->Branch("Q",&Q,"Q/F");
//	wf->Branch("wfID",&wfID,"wfID/I");

//	wf->Branch("Q",Q,"Q/F");
   	for(int f=0;f<wfn;f++)
       {

	      
	       char filename[50];
	       sprintf(filename,"PMT-LED-3.650V-Rigol-QDC-2016-3-15-%d.txt",f);
	       inputfile.open(filename);
	       if(inputfile){

	       //每一个文件求Q
	       charge=0;
	       for(int i=0;i<pn;i++)
	         {
		         inputfile>>amp[i-1];
		       if(i>160 && i<360){
			       charge1=charge+amp[i-1];
		       }
		 }

	       //The Unit of Q is pC
		Q=charge/50*(-1)*dt*1e12;
	        output<<Q<<endl;	
			       
		       
		       wf->Fill();
		       //The unit of Q is pC;
		       //Q[f][i]=charge/50*1000*(-1);
		      // printf("charge of waveform is %f\n",Q[f][i]);
		      
		      
	         }
	       //	wf->Fill();
	        
	       
	      
	       inputfile.close();
	  
       }
        //wf->Fill();
	wf->Write();



}







