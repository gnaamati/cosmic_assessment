from FileReader import line2dict, slurp, parse_args
from collections import defaultdict

def display_patterns(patterns):
    ##Go over dict and print all the patterns and their unique mutation count
    for allele in patterns:
        print(f"Mutated from {allele}")
        for mut_allele in patterns[allele]:
            print(f"Mutated to allele {mut_allele}: {patterns[allele][mut_allele]}") 

def main():
    args = parse_args()
    
    patterns = defaultdict(lambda: defaultdict(int))
    uniq_counter = defaultdict(int)
    
    lines = slurp(args.file)
    headers = lines.pop(0)
    for l in lines:
        ##Create a dict from each line in input
        mutation = line2dict(headers, l)

        ##Collect data for the pattern count
        mut_from = mutation.get('mutated_from_allele')
        mut_to   = mutation.get('mutated_to_allele')
        mutation_id = mutation.get('icgc_mutation_id')

        ##Only count once for each mutation_id 
        if uniq_counter[mutation_id] == 0:
            patterns[mut_from][mut_to] +=1
            uniq_counter[mutation_id] = 1
    
    display_patterns(patterns)    
    

if __name__ == "__main__":
    main()
