import re
from collections import Counter

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

def levenshtein_distance(s1, s2):
    # Lengths of each string
    m, n = len(s1), len(s2)
    
    # Create DP table (m+1) x (n+1)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    # Initialisation
    for i in range(m+1):
        dp[i][0] = i  # cost of deleting all chars in s1[:i]
    for j in range(n+1):
        dp[0][j] = j  # cost of inserting all chars in s2[:j]
    
    # Fill the table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cost_sub = 0  # no cost if same character
            else:
                cost_sub = 1
            
            dp[i][j] = min(
                dp[i-1][j] + 1,      # deletion
                dp[i][j-1] + 1,      # insertion
                dp[i-1][j-1] + cost_sub  # substitution
            )
    return dp[m][n]



# Example usage
if __name__ == "__main__":
    # test_corpus = ["lower", "lowest", "wider"]
    test_corpus = read_shakespeare_text()[:50].split()
    print("\n==== Byte Pair Encoding Demo ====\n")
    result = build_bpe_vocab(test_corpus, num_merges=5)

    print("\n==== Minimum Edit Distance Demo ====\n")
    # Example checks:
    print("leda -> deal =", levenshtein_distance("leda", "deal"))      # Expect 3
    print("drive -> brief =", levenshtein_distance("drive", "brief"))  # Expect 3
    print("drive -> divers =", levenshtein_distance("drive", "divers"))# Expect 3