import spacy
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Load scispaCy model
nlp_scispacy = spacy.load("en_ner_bc5cdr_md")

# Load BioBERT tokenizer and model
tokenizer_biobert = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
model_biobert = AutoModelForTokenClassification.from_pretrained(
    "dmis-lab/biobert-v1.1")
biobert_pipeline = pipeline(
    "ner", model=model_biobert, tokenizer=tokenizer_biobert)


def extract_entities_scispacy(text):

    doc = nlp_scispacy(text)
    diseases = set()
    drugs = set()

    for ent in doc.ents:
        if ent.label_ == "DISEASE":
            diseases.add(ent.text)
        elif ent.label_ == "CHEMICAL":
            drugs.add(ent.text)

    return diseases, drugs


def extract_entities_biobert(text):

    entities = biobert_pipeline(text)
    diseases = set()
    drugs = set()

    # BioBERT does not label entities as "DISEASE" or "CHEMICAL" specifically,
    # you may need to look into token classifications for those specific entities.
    for ent in entities:
        if 'disease' in ent['entity'].lower():  # Hypothetical check for diseases
            diseases.add(ent['word'])
        # Hypothetical check for chemicals/drugs
        if 'chemical' in ent['entity'].lower():
            drugs.add(ent['word'])

    return diseases, drugs


def compare_ner_results(scispacy_diseases, scispacy_drugs, biobert_diseases, biobert_drugs):

    print("\nComparison of Disease Entities:")
    print(
        f"scispaCy found: {len(scispacy_diseases)} diseases: {scispacy_diseases}")
    print(
        f"BioBERT found: {len(biobert_diseases)} diseases: {biobert_diseases}")
    print(
        f"Common Diseases: {scispacy_diseases.intersection(biobert_diseases)}")
    print(
        f"Differences (scispaCy - BioBERT): {scispacy_diseases.difference(biobert_diseases)}")
    print(
        f"Differences (BioBERT - scispaCy): {biobert_diseases.difference(scispacy_diseases)}")

    print("\nComparison of Drug Entities:")
    print(f"scispaCy found: {len(scispacy_drugs)} drugs: {scispacy_drugs}")
    print(f"BioBERT found: {len(biobert_drugs)} drugs: {biobert_drugs}")
    print(f"Common Drugs: {scispacy_drugs.intersection(biobert_drugs)}")
    print(
        f"Differences (scispaCy - BioBERT): {scispacy_drugs.difference(biobert_drugs)}")
    print(
        f"Differences (BioBERT - scispaCy): {biobert_drugs.difference(scispacy_drugs)}")


# Main function
if __name__ == "__main__":
    # Read the merged text file
    with open("./data/task_1_merged_txt.txt", "r", encoding="utf-8") as file:
        text_data = file.read()

    # Extract entities using scispaCy
    scispacy_diseases, scispacy_drugs = extract_entities_scispacy(text_data)

    # Extract entities using BioBERT
    biobert_diseases, biobert_drugs = extract_entities_biobert(text_data)

    # Compare results
    compare_ner_results(scispacy_diseases, scispacy_drugs,
                        biobert_diseases, biobert_drugs)
