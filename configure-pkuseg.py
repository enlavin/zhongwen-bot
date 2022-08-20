import spacy_pkuseg


for m in ['news', 'web', 'medicine', 'tourism']:
    spacy_pkuseg.pkuseg(m)
