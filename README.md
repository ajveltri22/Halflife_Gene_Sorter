# Halflife_Gene_Sorter

The script GeneSorter.py aims to identify human housekeeping genes in existing mammalian mRNA half-life measurements and
output a table of genes, which can be sorted by half-life for use in RT-qPCR.

GeneSorter.py finds the intersection of three datasets based on gene name:
  
  Human housekeeping genes are identified in:
    Eisenberg, E. and Levanon, E.Y., 2013. Human housekeeping genes, revisited. Trends in Genetics, 29(10), pp.569-574.
  
  Human mRNA half-life measurements based on 4sU labeling and microarray analysis:
    Murakawa, Y., Hinz, M., Mothes, J., Schuetz, A., Uhl, M., Wyler, E., Yasuda, T., Mastrobuoni, G., Friedel, C.C., Dölken,
    L. and Kempa, S., 2015. RC3H1 post-transcriptionally regulates A20 mRNA and modulates the activity of the IKK/NF-[kappa]
    B pathway. Nature communications, 6.
    
  Mouse mRNA half-life measurements based on 4sU labeling and RNA-seq:
    Schwanhäusser, B., Busse, D., Li, N., Dittmar, G., Schuchhardt, J., Wolf, J., Chen, W. and Selbach, M., 2011. Global
    quantification of mammalian gene expression control. Nature, 473(7347), pp.337-342.
