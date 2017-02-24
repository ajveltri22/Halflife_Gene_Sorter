hk_genes = open("HK_genes.tsv", "r")
m_hek = open("mhek.tsv", "r")
s_t3t = open("smouse.tsv", "r")
r_tc = open("Raghavan_tcell.tsv","r")

hk_dict = {} # gene_name:NIH_ID
m_dict = {} # gene_name:[gene_name, halflife]
s_dict = {} # gene_names:[ensembles, halflife]
r_dict = {} # gene_name:halflife

for line in hk_genes.readlines():
    NIH_ID = line.split("\t")[1]
    gene_name = line.split("\t")[0].strip().casefold()
    hk_dict[gene_name] = NIH_ID

for line in m_hek.readlines():
    try:
        ensemble = line.split("\t")[0]
        gene_name = line.split("\t")[1].casefold().strip()
        halflife = line.split("\t")[3].strip()
        m_dict[gene_name] = [gene_name, halflife, ensemble]
    except:
        pass

for line in s_t3t.readlines():
        NIH_ID = line.split("\t")[6].strip()
        gene_names = line.split("\t")[2].split(";")
        ensembles = line.split("\t")[7].split(";")
        halflife = line.split("\t")[22].strip()
        s_dict[NIH_ID] = [gene_names, halflife]

for line in r_tc.readlines():
    try:
        gene_name = line.split("\t")[1].strip().casefold()
        halflife = line.split("\t")[0]
        r_dict[gene_name] = halflife
    except:
        pass

count = 0

overlap = {} # gene_name:[m_halflife, s_halflife, r_halflife, hum_ensemble]

for entry in s_dict:
    for gene_name in s_dict[entry][0]:
        gene = gene_name.casefold().strip()
        if gene in m_dict and gene in hk_dict and gene in r_dict:
            overlap[gene] = [str(float(m_dict[gene][1])/60),s_dict[entry][1],str(float(r_dict[gene])/60),m_dict[gene][2]]

outfile = open("overlap_list_MSR.tsv", "w")
outfile.write("Gene name\tMurakawa halflife (Human)\tSchwannhausser halflife (Mouse)\tRaghavan halflife (Human T-cells)\tHuman ENSEMBL ID\n")
for gene in overlap:
      outfile.write(gene+"\t"+overlap[gene][0]+"\t"+overlap[gene][1]+"\t"+overlap[gene][2]+"\t"+overlap[gene][3]+"\n")

outfile.close()