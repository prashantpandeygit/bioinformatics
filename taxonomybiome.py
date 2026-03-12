from trapiche.api import TextToBiome, Community2vec, TaxonomyToBiome, TrapicheWorkflowFromSequence
from trapiche.config import TrapicheWorkflowParams

tax_files = [
    "SRR1524511_MERGED_FASTQ_SSU_OTU.tsv",
    "SRR1524511_MERGED_FASTQ_LSU_OTU.tsv",
]

vectors = Community2vec().transform([tax_files])
tax_results = TaxonomyToBiome().predict(vectors, constrain=text_preds)
print("taxonomy:", tax_results)
