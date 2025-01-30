import random
import pandas as pd
import os

# Load entity and relation mappings as dictionaries
entity2text = pd.read_csv("data/FB15k237/entity2text.txt", sep="\t", header=None, names=["entity", "text"]).set_index("entity")["text"].to_dict()
relation2text = pd.read_csv("data/FB15k237/relation2text.txt", sep="\t", header=None, names=["relation", "text"]).set_index("relation")["text"].to_dict()

# Load the test.tsv file
test_data = pd.read_csv("data/FB15k237/test.tsv", sep="\t", header=None, names=["head", "relation", "tail"])

def generate_negative_samples(df, entities, num_samples=1):
    """
    Generate negative samples by corrupting head or tail entities.
    Args:
        df (DataFrame): Original triples.
        entities (list): List of all unique entities.
        num_samples (int): Number of negative samples per positive triple.
    Returns:
        DataFrame: DataFrame with positive and negative triples.
    """
    negative_samples = []
    for _, row in df.iterrows():
        for _ in range(num_samples):
            corrupt_head = random.choice([True, False])
            corrupted_entity = random.choice(entities)
            if corrupt_head:
                negative_samples.append((corrupted_entity, row['relation'], row['tail']))
            else:
                negative_samples.append((row['head'], row['relation'], corrupted_entity))
    return pd.DataFrame(negative_samples, columns=['head', 'relation', 'tail'])

# Example: Generate negative samples
entities = pd.read_csv("data/wn18rr/entities.txt", header=None).squeeze().tolist()  # Load entity list
negative_samples = generate_negative_samples(test_data, entities, num_samples=1)

# Save the negative samples to a file
negative_samples_file = os.path.join("data/FB15k237/test_negative_samples.tsv")
negative_samples.to_csv(negative_samples_file, sep="\t", index=False, header=False)

print(f"Generated negative samples saved to: {negative_samples_file}")