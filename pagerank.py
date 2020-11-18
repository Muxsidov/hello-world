import os
import random
import re
import sys
from copy import deepcopy
import random
from collections import Counter

DAMPING = 0.85
SAMPLES = 10000

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Number of page's values(links)
    links_on_page = len(corpus.get(page))
    #print(links_on_page)

    # Number of pages on corpus
    links_on_corpus = len(corpus)
    #print(links_on_corpus)

    # If page has no links then return probability distribution that chooses randomly among all pages
    if len(page) == 0:
        return_dict = dict.fromkeys(deepcopy(corpus), (1 / links_on_corpus))

    # Otherwise act "normal"
    else:
        probability_of_page = (damping_factor / links_on_page)

        random_choose_probability = (1 - damping_factor) / links_on_corpus

        # Copying and giving each key probability of being choosen on corpus        
        return_dict = dict.fromkeys(deepcopy(corpus), random_choose_probability)

        # Iterate over dict and add probability_of_page if this page on value of page
        for key in return_dict:
            if (key in corpus.get(page)):
                return_dict[key] += probability_of_page
    
    return return_dict
       

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Another list for choosing random from it
    anot_list = []

    # Numbers of elements in anot_list
    h = 1000

    # List for containing samlpes
    sample = []

    # Choose first page randomly
    first_page = random.choice(list(corpus))
    
    # Add first page to list of samples
    sample.append(first_page)
    
    # Append page to sample n times
    for i in range(n):
        trans_of_previous = transition_model(corpus, sample[-1], damping_factor)

        for key, value in trans_of_previous.items():
            anot_list.extend([key] * round(value * h))

        sample.append(random.choice(anot_list))

    return_d = (Counter(sample))
    print(return_d)
    for k, v in return_d.items():
        return_d[k] = (value / n)
    print(return_d)


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Number of pages on corpus
    links_on_corpus = len(corpus)
    #print(links_on_corpus)

    dict_ite_page = dict.fromkeys(deepcopy(corpus), (1 / links_on_corpus))

    #while
    # If Page has no links it "has" link for every page
    #if len(page) == 0:

    
 #   else:
#        for i in range(len(#pageni dict da nechta value si bo'lsa)):
#            sum += PR(i) / NumLinks(i)

    #    PR(p) = ((1 - d) / links_on_corpus)
    

if __name__ == "__main__":
    main()
