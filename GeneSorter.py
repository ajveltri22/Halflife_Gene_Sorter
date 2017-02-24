#!/usr/bin/env python3

hk_genes = open("Eisenberg_housekeeping_genes.tsv", "r")
m_hek = open("Murakawa_human_halflives.tsv", "r")
s_t3t = open("Schwannhaeusser_mouse_halflives.tsv", "r")
#r_tc = open("Raghavan_human_tcell_halflives.tsv","r")

hk_dict = {} # gene_name:RefSeq_ID
m_dict = {} # gene_name:[gene_name, halflife]
s_dict = {} # RefSeq_ID:[[gene_names], halflife]
r_dict = {} # gene_name:halflife

for line in hk_genes.readlines():
    RefSeq_ID = line.split("\t")[1]
    gene_name = line.split("\t")[0].strip().casefold()
    hk_dict[gene_name] = RefSeq_ID

for line in m_hek.readlines():
    try:
        ensemble = line.split("\t")[0]
        gene_name = line.split("\t")[1].casefold().strip()
        halflife = line.split("\t")[3].strip()
        m_dict[gene_name] = [gene_name, halflife, ensemble]
    except:
        pass

for line in s_t3t.readlines():
        RefSeq_ID = line.split("\t")[6].strip()
        gene_names = line.split("\t")[2].split(";")
        ensembles = line.split("\t")[7].split(";")
        halflife = line.split("\t")[22].strip()
        s_dict[RefSeq_ID] = [gene_names, halflife]

'''
for line in r_tc.readlines():
    try:
        gene_name = line.split("\t")[1].strip().casefold()
        halflife = line.split("\t")[0]
        r_dict[gene_name] = halflife
    except:
        pass
'''

overlap = {} # gene_name:[m_halflife, s_halflife, hum_ensemble]

for entry in s_dict:
    for gene_name in s_dict[entry][0]:
        gene = gene_name.casefold().strip()
        if gene in m_dict and gene in hk_dict:
            overlap[gene] = [str(float(m_dict[gene][1])/60),s_dict[entry][1],m_dict[gene][2]]
            #overlap[gene] = [str(float(m_dict[gene][1]) / 60), s_dict[entry][1], str(float(r_dict[gene]) / 60),
            #                 m_dict[gene][2]]

outfile = open("Intersection_list.tsv", "w")
#outfile.write("Gene name\tMurakawa halflife (Human)\tSchwannhausser halflife (Mouse)\tRaghavan halflife (Human T-cells)\tHuman ENSEMBL ID\n")
outfile.write("Gene name\tMurakawa halflife (Human, min)\tSchwannhausser halflife (Mouse, min)\tHuman ENSEMBL ID\n")
for gene in overlap:
      outfile.write(gene+"\t"+overlap[gene][0]+"\t"+overlap[gene][1]+"\t"+overlap[gene][2]+"\n")

outfile.close()