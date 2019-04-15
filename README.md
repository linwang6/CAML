# CAML/ELSA?
### **E**nsemble **L**earning for classifying **S**ingle-cell data and projection across reference **A**tlases

![alt text](https://github.com/linwang6/CAML/blob/master/inst/CAML.jpg)


## Contents
#### [Installation](https://github.com/linwang6/CAML#Installation)
#### [Tutorial](https://github.com/linwang6/CAML#Tutorial)
#### [Contact](https://github.com/linwang6/CAML#Contact)
#### [Copyright and License Information](https://github.com/linwang6/CAML#Copyright-and-License-Information)


## Installation
    Requiements:
    1. Python 2.7 or greater version
    2. Packages:
       numpy (>=1.8.2)
       scipy (>=0.13.3)
       scikit-learn (>=0.20) 
       pycm
       imbalanced-learn (0.4)
      
    How to install packages (Taking imbalanced-learn as example)?
    1. Imbalanced-learn is currently available on the PyPi’s reporitories and you can install it via pip. 
       It's easy to install packages using pip.
       For example, typing command: pip install -U imbalanced-learn to install 
       'imbalanced-learn' package.
    2. The package is release also in Anaconda Cloud platform.
       For example, typing command: conda install -c conda-forge imbalanced-learn to install 
       'imbalanced-learn' package.
    3. Or install using pip and GitHub.
       For example, typing command: pip install -U git+https://github.com/scikit-learn-contrib/imbalanced-learn.git 
       to install 'imbalanced-learn' package.
     
     
## Tutorial
    Please simply typing command: python caml.py
    It gives you help information for caml,
    $ python caml.py
    Usage: python caml.py classification scell/snuc/bulk [-m] [-i] [-c] [-g] [-o] [-s]
           python caml.py projection     scell/snuc/bulk [-t] [-p] [-c] [-g] [-o] [-s]

    classification arguments:
     -m, --cell_marker       	   list for cell marker
     -i, --input_file        	   input data for classification
     -c, --cell_type         	   cell type list
     -g, --geneNum             	   number of top importances
     -o, --output            	   output file for cell types
     -s, --specify (optional)          specific cell type for extend, for example -s CD4:CD8

    projection arguments:
     -t, --traning           	   traning prep data
     -p, --prediction        	   prediction prep data
     -c, --cell_type         	   cell type list
     -g, --geneNum           	   number of top importances
     -o, --output            	   output file for cell types
     -s, --specify (optional)          specific cell type for extend, for example -s CD4:CD8
     

### Classification of single-cell/single-nuc/bulk RNA-Seq data
For the classification of cell types, two input files are needed, one is the normalized gene expression data of single-cell/single-nuc/bulk RNA-Seq, another one file is the cell markers. The gene expression data file should be a matrix (cell by gene), the column is the gene expression and the row is the cell ID, for example,
    
        "RP11-34P13.3" "FAM138A" "OR4F5" "RP11-34P13.7" "RP11-34P13.8" "RP11-34P13.14" "RP11-34P13.9"
    "AAACCTGAGCATCATC" 0 0 0 0 0 0 0
    "AAACCTGAGCTAACTC" 0.758984278767459 0 0 0 0 0.758984278767459 0.758984278767459
    "AAACCTGAGCTAGTGG" 0 0 0 0 0 0 0
    "AAACCTGCACATTAGC" 0 0 0 0 0 0 1.34676065446578
    "AAACCTGCACTGTTAG" 0 0 0.731934085294069 0 0 0 0
    "AAACCTGCATAGTAAG" 0 0 0 0 0 0 0



And the format of the cell markers file should be like this:

    PBMC data:
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

When the files are ready, then we can run the Classification subprogram, 
    
    python caml.py classification -m markers.list -i gene_exxpression_data -g 50 -o classification_output -s subtypes extension (optional)

Please note that the parameter -g for the feature selection, setting the '-g 50' should work well for most of the cases (Please see our paper). Please note that when you want to classify more than 10 different classes or more, please fell free to increase the number to [number of desired classification] * 10, it works well for most cases. And the optional parameter -s, we suggest you include it when there are closely cell subtypes, for example CD4 and CD8 cell types.


The output file contains all the information including the cell/sample ID, the predicted class probabilities and predicted cell/sample types, here we show two examples, one is for single cell classification and another one is for bulk RNA-seq data (ivy GAP, [Ivy Glioblastoma Atlas Project](http://glioblastoma.alleninstitute.org/))


    
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
    

The following sankey plot of the predicted samples types compared to the anatomic structure annotation types  (http://glioblastoma.alleninstitute.org/).
![alt text](https://github.com/linwang6/CAML/blob/master/inst/IVY_classification_sankey.png)


The tSNE plot of predicted samples types and the anatomic structure annotation types
![alt text](https://github.com/linwang6/CAML/blob/master/inst/IVY_classification_tSNE.png)


### Projection of single-cell/single-nuc/bulk RNA-Seq data 
    
    /usr/local/bin/python2.7 /Users/wanglin/cell_classifier/garnett-master/caml/python/python/caml_classity_project.py projection scell -t SF11644T_SF11956T_SF11977T_SF11979T_PCA_PC16_new5_scale.data_share_tr -p 2018-03-29_Ivy_GAP_pheno_1_sortByAnn_Ex_head_tr_share_tr -c 2018-03-29_Ivy_GAP_pheno_1_sortByAnn_2_1_addHGG -g 10 -o Ivy_GAP2HGG_g10.2
    
    
## Contact

Lin Wang Lin.Wang2@ucsf.edu

Aaron Diaz Aaron.Diaz@ucsf.edu

Diaz Lab

https://github.com/diazlab

https://diazlab.ucsf.edu/
    
    
## Copyright and License Information


