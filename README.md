# RNAseq

## Instructions for analysis

The goal of this analysis is to perform a differential expression analysis at gene level (mRNA isoforms are *not* taken into account).

The following instructions are short in purpose: additional information or tools can be deduced, or retrieve from public databases. 

1. Download 4 sequence datasets deposited to the EBI [ENA](http://www.ebi.ac.uk/ena):

 `ERR990557`
    
 `ERR990558`
    
 `ERR990559`
    
 `ERR990560`
 
These datasets have been generated in a work published in Embo Reports :

Molla-Herman A, Vallés AM, Ganem-Elbaz C, Antoniewski C, Huynh J-R. tRNA processing defects induce replication stress and Chk2-dependent disruption of piRNA transcription. EMBO J. 2015;34: 3009–3027. doi:10.15252/embj.201591006

2. Extract fastq files
3. for each file, select 8,000,000 (8 millions) of sequence reads and generate the following sample files:

 `ERR990557s.fastq`

`zcat ERR990557.fastq.gz | head -12000000 > ERR990557s.fastq`
    
 `ERR990558s.fastq`

`zcat ERR990558.fastq.gz | head -12000000 > ERR990558s.fastq`
    
 `ERR990559s.fastq`

`zcat ERR990559.fastq.gz | head -12000000 > ERR990559s.fastq`
    
 `ERR990560s.fastq`

`zcat ERR990560.fastq.gz | head -12000000 > ERR990560s.fastq`


4. Align these read datasets to the reference genome by any appropriate mean, and generate a sorted bam alignment file.


-Chargement des fichiers fastq dans galaxy  https://mississippi.snv.jussieu.fr
-groomer
-use of tophat, param : single-end,  genome de reference : D melanogaster genome release 6

`samtools sort ERR990557.bam -o ERR990557.sorted.bam`
`samtools sort ERR990558.bam -o ERR990558.sorted.bam`
`samtools sort ERR990559.bam -o ERR990559.sorted.bam`
`samtools sort ERR990560.bam -o ERR990560.sorted.bam`
 

5. Count reads aligning to genome's genes by any appropriate mean

use of HTSeq-count and Drosophila_melanogaster.BDGP6.90.gtf.gz 
(ftp://ftp.ensembl.org/pub/release-90/gtf/drosophila_melanogaster/)

`samtools view -h -o ERR990557.sam ERR990557.sorted.bam`
`python -m HTSeq.scripts.count ERR990557.sam Drosophila_melanogaster.BDGP6.90.gtf.gz >> ERR990557.count.txt`

`samtools view -h -o ERR990558.sam ERR990558.sorted.bam`
`python -m HTSeq.scripts.count ERR990558.sam Drosophila_melanogaster.BDGP6.90.gtf.gz >> ERR990558.count.txt`

`samtools view -h -o ERR990559.sam ERR990559.sorted.bam`
`python -m HTSeq.scripts.count ERR990559.sam Drosophila_melanogaster.BDGP6.90.gtf.gz >> ERR990559.count.txt`

`samtools view -h -o ERR990560.sam ERR990560.sorted.bam`
`python -m HTSeq.scripts.count ERR990560.sam Drosophila_melanogaster.BDGP6.90.gtf.gz >> ERR990560.count.txt`


6. Perform a statistical differential expression analysis and report using any appropriate figure(s)/graph(s)


Chargement des fichiers count dans Galaxy
Use of DESeq2. Factor name : unknown
	       4 factor level : 57, 58, 59, 60. 

7. select a list of genes likely to be differentially expressed with a p-adj value < 0.01

8. Code a simple script that parse the table of differential expressions (from *6.*) and return the genes with a p-adj value < 0.01 for rejection of H0 (non differential expression)

script parse.py in folder scripts

## Reporting

Each analyst will report her/is analysis by any mean s/he feels appropriate (pdf, text, markedown, jpg, URL, etc.).

Reports are in the folder analysis.05

The only constraint is that analysis outputs will be deposited in a personal [fork](https://help.github.com/articles/fork-a-repo/) of this repository in a *new* directory named analysis.01, analysis.02, etc. (see analysis.00 for an example). Keep track of the analysis.xx directories already existing and chose another name for your directory.

Final submission of the results will be made through a [pull request](https://help.github.com/articles/creating-a-pull-request/) from the analyst to the [original repo](https://github.com/drosofff/RNAseq.git).

Please do not neglect the reporting and follow the requested process, it is a part of the analysis.
