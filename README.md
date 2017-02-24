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
    
Raghavan_human_tcell_halflives.tsv is a fourth dataset included in Intersection_list_MSR.tsv and Intersection_list_MSR.xlsx from:
  Raghavan, A., Ogilvie, R.L., Reilly, C., Abelson, M.L., Raghavan, S., Vasdewani, J., Krathwohl, M. and Bohjanen, P.R., 2002. Genome‐wide
  analysis of mRNA decay in resting and activated primary human T lymphocytes. Nucleic acids research, 30(24), pp.5529-5538.
This dataset did not correlate with either the Schwannhäusser or the Murakawa datasets and was therefore excluded from the analyses.

Intersection_list.tsv is the script's output of 1992 genes that appear in all three lists. This file was then converted to
Intersection_list_MS.xlsx and the difference between mRNA half-life measurements for each gene was calculated. Genes for qPCR were
selected by filtering genes for which the mRNA half-lives differed by less than 1.5 hours between the two datasets and had approximately
the desired half-life.
