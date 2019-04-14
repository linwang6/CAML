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
     

#### Classification of single-cell/single-nuc/bulk RNA-Seq data
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

please note that the parameter -g for the feature selection, setting the '-g 50' should work well for most of the cases (Please see our paper). Please note that when you want to classify more than 10 different classes or more, please fell free to increase the number to [number of desired classification] * 10, it works well for most cases. And the optional parameter -s, we suggest you include it when there are closely cell subtypes, for example CD4 and CD8 cell types.

The output 
The sankey plot
The tSNE plot


#### Projection of single-cell/single-nuc/bulk RNA-Seq data 
    
    /usr/local/bin/python2.7 /Users/wanglin/cell_classifier/garnett-master/caml/python/python/caml_classity_project.py projection scell -t SF11644T_SF11956T_SF11977T_SF11979T_PCA_PC16_new5_scale.data_share_tr -p 2018-03-29_Ivy_GAP_pheno_1_sortByAnn_Ex_head_tr_share_tr -c 2018-03-29_Ivy_GAP_pheno_1_sortByAnn_2_1_addHGG -g 10 -o Ivy_GAP2HGG_g10.2
    
    
## Contact

Lin Wang Lin.Wang2@ucsf.edu

Aaron Diaz Aaron.Diaz@ucsf.edu

Diaz Lab

https://github.com/diazlab

https://diazlab.ucsf.edu/
    
    
## Copyright and License Information


