from graphs import *

def build_graph(word_list):
    buckets = {}
    the_graph = Graph()
    
    # Create buckets of words that differ by 1 letter
    for word in word_list:
        for i, _ in enumerate(word):
            bucket = f"{word[:i]}_{word[i + 1 :]}"
            if buckets.get(bucket, None) == None:
                buckets[bucket] = {word}
            else:
                buckets[bucket].add(word)

    # Create edges between all values in each bucket
    for similar_words in buckets.values():
        for word_1 in similar_words:
            for word_2 in (similar_words - {word_1}):
                the_graph.add_edge(word_1, word_2)

    return the_graph
    


def main():
    word_list = ['dog', 'cat', 'rat']
    the_graph = build_graph(word_list)
    for vertex in the_graph:
        print(vertex)

if __name__ == '__main__':
    main()