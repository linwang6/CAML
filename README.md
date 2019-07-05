# ELSA
### *E*nsemble *L*earning for classifying *S*ingle-cell data and projection across reference *A*tlases

Single-cell atlases are being assembled at an accelerating pace. How best to project data across single-cell atlases is an open problem. We developed a boosted learner that overcomes the greatest challenge with status quo classifiers: low sensitivity, especially when dealing with rare cell types.


![alt text](https://github.com/linwang6/CAML/blob/master/inst/CAML.jpg)



## Contents
#### [Installation](https://github.com/linwang6/CAML#Installation)
#### [Tutorial](https://github.com/linwang6/CAML#Tutorial)
#### [Test Data](https://github.com/diazlab/ELSA/tree/master/Data)
#### [Contact](https://github.com/linwang6/CAML#Contact)
#### [Copyright and License Information](https://github.com/linwang6/CAML#Copyright-and-License-Information)
#### [Citation](https://github.com/linwang6/CAML#Citation)
#### [References](https://github.com/linwang6/CAML#References)



## Installation
    Requiements:
    1. Python 2.7 or greater version
    2. Packages:
       numpy (>=1.8.2)
       scipy (>=0.13.3)
       scikit-learn (>=0.20) 
       pycm
       imbalanced-learn (0.4)
      
    Package installation:
    1. Via pip:
    
    pip install -U numpy scipy scikit-learn pycm imbalanced-learn
    
    2. Via Anaconda:
    
    conda install -c https://conda.binstar.org/pymc numpy scipy scikit-learn pymc imbalanced-learn
     
     
## Tutorial
    For help, type: python elsa.py
    $ python elsa.py
    Usage: python elsa.py classification scell/snuc/bulk [-m] [-i] [-g] [-o] [-s]
           python elsa.py projection     scell/snuc/bulk [-t] [-p] [-c] [-g] [-o] [-s]

    classification arguments:
     -m, --cell_marker       	   file defining cell-type labels and marker genes
     -i, --input_file        	   file containing input data to be classified
     -g, --geneNum             	   number of top-scoring genes to retain for classification
     -o, --output            	   output file
     -s, --specify (optional)      specific cell type for extend, for example -s CD4:CD8

    projection arguments:
     -t, --traning           	   file containing the reference data, i.e. the traning data
     -p, --projection        	   file containing the data to be projected, i.e. classified 
     -c, --cell_type         	   cell type list
     -g, --geneNum           	   number of top-scoring genes to retain for classification
     -o, --output            	   output file
     -s, --specify (optional)      specific cell type for extend, for example -s CD4:CD8
     

### Classifing single-cell/nucei or bulk RNA-Seq datasets using a list of gene markers. 
Two input files are required: 1) a samples-by-gene expression table (e.g. log2 counts per 10K), 2) a list of cell-type labels and cell-type specific gene lists. 

The gene-expression data should be in a sample-by-gene tab-separated file:
    
        "RP11-34P13.3" "FAM138A" "OR4F5" "RP11-34P13.7" "RP11-34P13.8" "RP11-34P13.14" "RP11-34P13.9"
    "AAACCTGAGCATCATC" 0 0 0 0 0 0 0
    "AAACCTGAGCTAACTC" 0.758984278767459 0 0 0 0 0.758984278767459 0.758984278767459
    "AAACCTGAGCTAGTGG" 0 0 0 0 0 0 0
    "AAACCTGCACATTAGC" 0 0 0 0 0 0 1.34676065446578
    "AAACCTGCACTGTTAG" 0 0 0.731934085294069 0 0 0 0
    "AAACCTGCATAGTAAG" 0 0 0 0 0 0 0



The format for the cell-type labels/markers file is as follows:

    PBMC (peripheral blood mononuclear cell) data:
    Monocytes:"CD14";"FCGR1A";"CD68"
    B:"CD19";"MS4A1";"CD79A"
    DC:"IL3RA";"CD1C";"BATF3"
    CD34:"CD34"
    NK:"FCGR3A"
    ...
    
    ivyGAP data:
    Infiltrating_Tumor:"SNAP25";"UHRF1"
    Microvascular_proliferation:"KLF6";"ELTD1"
    Pseudopalisading_cells:"TREM
    Leading_Edge:"SNAP25"
    ...

First, run the Classification subprogram: 
    
    python elsa.py classification scell -m markers.list -i gene_exxpression_data -g 50 -o classification_output -s subtypes extension (optional)

Note: setting '-g 50' should work well for most cases. If classifying more than 10 different cell types then increase the number to [number of cell types] * 10. Include the optional parameter -s when classifying cell types with correlated gene expression. For example, when classifying closely related cellular subtypes, such as T-cell subtypes.


The output file contains the cell/sample ID, the predicted class probabilities and predicted cell/sample types. 

We now demonstrate examples of single-cell and bulk-extraction RNA-seq classification using a scRNA-seq PBMC dataset available [from 10X Genomics](https://support.10xgenomics.com/single-cell-gene-expression/datasets), and bulk RNA-seq of GBMs available at the [Ivy Glioblastoma Atlas Project](http://glioblastoma.alleninstitute.org/).


#### scRNA-Seq Classification (PBMC dataset)

We apply ELSA to the PBMC data set, which has several different cell types including B cells, CD4 and CD8 T-cells, dendritic cells, Natural Killer cells, and myeloid cell types. We find that classifying T-cell subtypes is more accurate when the parameter -s is used, e.g. '-s CD4:CD8'.

The following the head of the output file:
    
    Cell_ID Probability_of_CD34   Probability_of_B  Probability_of_CD4    Probability_of_CD8  Probability_of_DC    Probability_of_Monocytes    Probability_of_NK   Predicted_types
    "AAACCTGAGCTAACTC"      0.00037265905209929966  0.00019461235341044442  0.018780001757902304    0.0069075896125628325   0.002850644369198496    0.9516413165740238      0.01925317628080269     Monocytes       
    "AAACCTGAGCTAGTGG"      0.00023363917579888161  0.0002758384408950353   0.9170060548204749      0.07060034544087794     0.0005234122503909771   0.0010333612928155509   0.010327348578746714    CD4
    "AAACCTGTCTACCAGA"      0.0001331752815381497   0.0003692780495988838   0.2049931328836318      0.785481988392962       0.0006134695859992477   0.0024904196761684158   0.005918536130101295    CD8     
    "AAACCTGTCTGCGGCA"      0.0011942266787620323   0.006175772485781797    0.0070025049357011395   0.9803464785767921      0.0013936372872175604   0.0006816808625693592   0.00320569917317607     CD8     
    "AAACGGGCAGTAAGAT"      0.9700732379485719      0.0008380287152539023   0.0008924723753801042   0.013193123791861163    0.0036978727367686544   0.005918092489852546    0.005387171942311561    B       
    "AAACGGGGTACAGTTC"      0.00495654893338553     0.05811010482321016     0.045442150300020905    0.38851522558955265     0.01334805425287245     0.013542117897749199    0.47608579820320923     NK      
    "AGTGAGGCACAGGTTT"	0.02612355295139755	0.6591159513286947	0.05461515122492262	0.06661120030271617	0.15399315778783473	0.007438692657104565	0.032102293747329654	CD34	
    "ACACCCTCACGCCAGT"      0.01002801133138485     0.013450302818802504    0.0033840503479810285   0.004874948704661606    0.8704569593427326      0.08031400874446516     0.017491718709972397    DC      
    "ACACCCTCATGCCTAA"      0.007684983027881935    0.03605432535601024     0.6642055706181322      0.26008323999520694     0.008766747625962046    0.004490175653011966    0.01871495772379467     CD4     
    "ACGATACAGCTACCTA"      0.004612004038623754    0.0012087032246744483   0.00226395749582816     0.009699679746039132    0.24396917832147094     0.7118817116671998      0.02636476550616375     Monocytes       
    "ACGATACAGCTCTCGG"      0.7683682467453246      0.04978819822557202     0.018926906070520316    0.0969378244574078      0.024458850103481297    0.008219664615566556    0.03330030978212728     B       

A tSNE plot of gene-marker based cell types (left) and predicted cell types (right):

![alt text](https://github.com/linwang6/CAML/blob/master/inst/PBMC_tSNE.png)



#### Bulk RNA-Seq Classification ([ivy GAP](http://glioblastoma.alleninstitute.org/))

ELSA can also can be used for classifying bulk RNA-Seq samples. Here we classify data from the ivyGAP data, which has detailed anatomic structure annotations.

The following is the head of the output file:
    
    Cell_ID Probability_of_Cellular_Tumor   Probability_Infiltrating_Tumor   Probability_Leading_Edge Probability_Microvascular_proliferation    Probability_Pseudopalisading_cells Predicted_types
    "304950296"     2.6800024884849247e-14  1.8189894035424017e-12  2.6800024884849247e-14  0.9999999999981006      2.6800024884849247e-14  Microvascular_proliferation 
    "304357559"     1.987101672593777e-08   1.490116037632912e-08   2.1954579181221763e-10  0.9999999451372603      1.9871016725937764e-08  Microvascular_proliferation 
    "300173642"     1.646359585919862e-10   1.0113806499514636e-06  1.646359585919862e-10   1.1174283061586529e-08  0.999998977115795       Pseudopalisading_cells 
    "300629346"     0.00012205516448045012  1.0112561795191147e-06  1.4899312070367482e-08  1.0112561795191142e-06  0.9998759074238485      Pseudopalisading_cells 
    "301626601"     1.818989403090102e-12   1.234596782500497e-10   0.9999999997494426      1.2345967825004966e-10  1.818989403090102e-12   Leading_Edge 
    "301626695"     1.646359585919862e-10   1.0113806499514636e-06  0.999998977115795       1.1174283061586529e-08  1.646359585919862e-10   Leading_Edge 
    "300173646"     2.6800024884849247e-14  1.8189894035424017e-12  2.6800024884849247e-14  0.9999999999981006      2.6800024884849247e-14  Microvascular_proliferation 
    "300629309"     2.6800024884849247e-14  1.8189894035424017e-12  2.6800024884849247e-14  0.9999999999981006      2.6800024884849247e-14  Microvascular_proliferation 
    "302264000"     0.5713929269045216      5.2305205949612394e-05  7.70637156174121e-07    0.4284842471392252      6.975011314752466e-05   Cellular_Tumor 
    "303748328"     0.00012205513697496831  1.2366088240428581e-06  1.489930871276471e-08   1.0112559516296298e-06  0.9998756820989407      Pseudopalisading_cells 
    "301626689"     0.9917818182116735      0.008217149160959135    1.4778700742299505e-08  1.0030699659373927e-06  1.4778700742299505e-08  Cellular_Tumor 
    "301287582"     0.9999999997219304      1.5097199407061566e-10  1.8189894030400575e-12  1.2345967824665307e-10  1.8189894030400575e-12  Cellular_Tumor 
    "300629356"     2.4256613183435653e-12  0.999999985091562       2.4256613183435653e-12  1.4901160971694644e-08  2.4256613183435653e-12  Infiltrating_Tumor 
    "301626609"     2.4256613183435653e-12  0.999999985091562       2.4256613183435653e-12  1.4901160971694644e-08  2.4256613183435653e-12  Infiltrating_Tumor 
    
A Sankey plot of predicted sample types compared to Ivy GAP (http://glioblastoma.alleninstitute.org/) anatomic-structure annotations:

![alt text](https://github.com/linwang6/CAML/blob/master/inst/IVY_classification_sankey.png)



A tSNE plot of predicted sample types and their anatomic structure annotations:

![alt text](https://github.com/linwang6/CAML/blob/master/inst/IVY_classification_tSNE.png)



### Projection of single-cell/single-nuc/bulk RNA-Seq data 
    
    python elsa.py projection scell -t reference_expression_matrix -p projection_expression_matrix -c reference_cell_types -g 50 -o projection_to_reference_output
    
#### Projection of different scRNA-Seq platforms


Projection of the Smart-seq2 platform (human pancreas data sets, [Segerstolpe et al](https://www.sciencedirect.com/science/article/pii/S1550413116304363?via%3Dihub).) to inDrop platform ([Baron et al](https://www.sciencedirect.com/science/article/pii/S2405471216302666?via%3Dihub).)


A tSNE plot comparing reference cell-type labels (left) to the labels of their projections (right):
![alt text](https://github.com/linwang6/CAML/blob/master/inst/Pancreas_tSNE.png)


A Sankey plot comparing reference and projection cell-type labels:
![alt text](https://github.com/linwang6/CAML/blob/master/inst/Pancreas_sankey.png)


#### Projection of snRNA-Seq to scRNA-Seq.

Next we use human cortex sc/snRNA-seq data, available from [Lake et al.](https://www.nature.com/articles/s41598-017-04426-w).

A Sankey plot of the projection of single-cell to single-nuclei RNA-seq data.

![alt text](https://github.com/linwang6/CAML/blob/master/inst/snRNA-Seq2scRNA-Seq.png)



#### Projection of bulk RNA-Seq to scRNA-Seq.

A Sankey plot of the projection of bulk RNA-Seq data from the [ivy GAP](http://glioblastoma.alleninstitute.org/) to scRNA-seq from human glioblastomas. 

![alt text](https://github.com/linwang6/CAML/blob/master/inst/ivyGAP2GBM.png)

(CT: Cellular Tumor IT: Infiltrating Tumor MVP: Microvascular proliferation LE: Leading Edge PAN: Pseudopalisading cells)

We found that mGSCs are enriched in hypoxic regions, while the pGSCs are enriched in the tumor’s leading edge.


## Contact

Lin Wang Lin.Wang2@ucsf.edu

Aaron Diaz Aaron.Diaz@ucsf.edu

Diaz Lab

https://github.com/diazlab

https://diazlab.ucsf.edu/
    
    


## Copyright and License Information

GNU GENERAL PUBLIC LICENSE

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>  Everyone is permitted to copy and distribute verbatim copies  of this license document, but changing it is not allowed.




## Citation

Please cite our paper if our paper or code helped you.

Our manuscript is available on [here]().


## References

1. Seiffert, C., Khoshgoftaar, T., Hulse, J. & Napolitano, A. RUSBoost: Improving clasification performance when training data is skewed. in 19th International Conference on Pattern Recognition 1–4 (2008).
2. Haghighi, S., Jasemi, M., Hessabi, S. and Zolanvari, A. (2018). PyCM: Multiclass confusion matrix library in Python. Journal of Open Source Software, 3(25), p.729.
3. Baron, M. et al. A Single-Cell Transcriptomic Map of the Human and Mouse Pancreas Reveals Interand Intra-cell Population Structure. Cell Syst 3, 346–360.e4 (2016).
4. Segerstolpe, Å. et al. Single-Cell Transcriptome Profiling of Human Pancreatic Islets in Health and Type 2 Diabetes. Cell Metab. 24, 593–607 (2016).
5. Puchalski RB, Shah N, Miller J, Dalley R, Nomura SR, Yoon JG, Smith KA, Lankerovich M, Bertagnolli D, Bickley K, Boe AF, Brouner K, Butler S, Caldejon S, Chapin M, Datta S, Dee N, Desta T, Dolbeare T, Dotson N, Ebbert A, Feng D, Feng X, Fisher M, Gee G, Goldy J, Gorley L, Gregor BW, Gu G, Hejazinia N, Hohmann J, Hothi P, Howard R, Joines K, Kriedberg A, Kuan L, Lau C, Lee F, Lee H, Lemon T, Long F, Mastan N, Mott E, Murthy C, Ngo K, Olson E, Reding M, Riley Z, Rosen D, Sandman D, Shapovalova N, Slaughterbeck CR, Sodt A, Stockdale G, Szafer A, Wakeman W, Wohnoutka PE, White SJ, Marsh D, Rostomily RC, Lydia Ng L, Dang C, Jones AJ, Keogh B, Gittleman HR, Barnholtz-Sloan JS, Cimino PJ, Uppin MS, Keene CD, Farrokhi FR, Lathia JD, Berens ME, Iavarone I, Bernard A, Lein E, Phillips JW, Rostad SW, Cobbs C, Hawrylycz MJ, and Foltz GD. An anatomic transcriptional atlas of human glioblastoma.Science360, 660-663 (2018).







