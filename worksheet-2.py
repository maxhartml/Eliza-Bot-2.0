import re
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

def read_shakespeare_text(file_path="shakes.txt"):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text  # For demonstration, we'll only show the first 10000 characters

def build_bpe_vocab(corpus, num_merges=5):
    """
    A simple Byte Pair Encoding algorithm with educational print statements.
    corpus: list of words, e.g. ['lower', 'lowest', 'wider']
    num_merges: how many pair merges to perform
    """
    print("Initial Corpus:", corpus)
    print(f"Number of merges to perform: {num_merges}")
    print("-" * 50)
    
    # Step 1) Split each word into a list of characters, optionally adding an end-of-word symbol
    tokenised = [list(word) for word in corpus]
    print("1) Splitting each word into characters:\n", tokenised)
    
    # Step 2) Convert each list of characters into a single string with spaces, 
    # then append a special token (here '</w>') to mark the end of each word
    tokenised = [" ".join(chars) + " </w>" for chars in tokenised]
    print("\n2) Converting characters to spaced strings and appending '</w>':")
    for t in tokenised:
        print("   ", t)
    
    # Main loop for the specified number of merges
    for merge_index in range(num_merges):
        print(f"\n--- Merge Iteration {merge_index + 1} ---")
        
        # 3) Count all adjacent symbol pairs across all tokenised words
        pairs = Counter()
        for line in tokenised:
            symbols = line.split()
            for i in range(len(symbols) - 1):
                pairs[(symbols[i], symbols[i+1])] += 1
        
        # If no pairs are found (perhaps corpus is empty or no further merges possible), stop
        if not pairs:
            print("No more pairs found. Stopping early.")
            break
        
        # Identify the most frequent pair
        best_pair = max(pairs, key=pairs.get)
        print("Most frequent pair:", best_pair, "(Frequency:", pairs[best_pair], ")")
        
        # 4) Merge that pair in all tokenised words by replacing the space between them
        pattern = re.escape(" ".join(best_pair))
        replace_str = "".join(best_pair)
        
        print(f"Replacing pattern '{pattern}' with merged token '{replace_str}' in each line.")
        
        new_tokenised = []
        for line in tokenised:
            merged_line = re.sub(pattern, replace_str, line)
            new_tokenised.append(merged_line)
            
            # Optionally show each transformation
            print("  Before:", line)
            print("  After: ", merged_line)
            print("  -")
        
        tokenised = new_tokenised
    
    print("\nFinal tokenised result after all merges:")
    for t in tokenised:
        print(t)
    
    return tokenised

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def levenshtein_distance_with_heatmap(s1, s2, save_image=True):
    """
    Computes Levenshtein distance between s1 and s2 and saves a DP heatmap
    so that '#' is at the bottom row, and the last character of s1 is at the top.
    """
    # 1) Create DP table
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    # Initialise
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    # Fill DP
    for i in range(1, m+1):
        for j in range(1, n+1):
            cost_sub = 0 if s1[i-1] == s2[j-1] else 1
            dp[i][j] = min(
                dp[i-1][j] + 1,         # deletion
                dp[i][j-1] + 1,         # insertion
                dp[i-1][j-1] + cost_sub # substitution
            )
    
    distance = dp[m][n]

    # 2) Convert to DataFrame (no reversing)
    df_dp = pd.DataFrame(dp)

    # Row labels go from # (row 0) to last char of s1 (row m).
    # That means row_labels[0] = '#', row_labels[m] = s1[m-1].
    row_labels = ["#"] + list(s1)  
    col_labels = ["#"] + list(s2)
    
    # 3) Plot the heatmap
    plt.figure(figsize=(7,6))
    ax = sns.heatmap(
        df_dp,
        annot=True,
        fmt="d",
        cmap="Blues",
        cbar=True,
        xticklabels=col_labels,
        yticklabels=row_labels
    )
    
    # Invert the Y axis so row 0 is visually at the bottom
    ax.invert_yaxis()
    
    ax.set_title(f"Levenshtein DP Table:\n'{s1}' → '{s2}' (Distance = {distance})")
    ax.set_xlabel("Characters of s2")
    ax.set_ylabel("Characters of s1")
    
    plt.tight_layout()
    
    # 4) Save the figure, then close it. No pop-up window occurs.
    if save_image:
        filename = f"levenshtein_{s1}_TO_{s2}.png".replace(" ", "_")
        plt.savefig(filename, dpi=150)
        print(f"Saved heatmap as: {os.path.abspath(filename)}")

    plt.close()
    return distance

# Example usage
if __name__ == "__main__":

    test_corpus = read_shakespeare_text()[:50].split()
    print("\n==== Byte Pair Encoding Demo ====\n")
    result = build_bpe_vocab(test_corpus, num_merges=5)

    print("\n==== Minimum Edit Distance Demo ====\n")
    print("leda -> deal =", levenshtein_distance_with_heatmap("leda", "deal"))      
    print("drive -> brief =", levenshtein_distance_with_heatmap("drive", "brief"))  
    print("drive -> divers =", levenshtein_distance_with_heatmap("drive", "divers"))
    print("maxhart -> ilovepizza =", levenshtein_distance_with_heatmap("maxhart", "ilovepizza"))