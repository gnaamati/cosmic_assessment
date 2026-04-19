from FileReader import line2dict, slurp, parse_args

from collections import defaultdict

def display_patterns(patterns):
    for allele in patterns:
        print(f"Mutated from {allele}")
        for mut_allele in patterns[allele]:
            print(f"Mutatetd to allele {mut_allele}: {patterns[allele][mut_allele]}") 

def print_high_low(sample_mutation_count):
    lowest     = 1000_000
    lowest_id  = ''
    highest    = 0 
    highest_id = ''

    for sample in sample_mutation_count:
        #print(f"Sample: {sample}")
        #print (sample_mutation_count[sample])
        count = len(list(sample_mutation_count[sample].keys()))

        #print(f"count = {mutation_count}")  
        if count < lowest:
            lowest = count
            lowest_id = sample
        if count > highest:
            highest = count
            highest_id = sample
    print(f"highest = {highest}, highest_id = {highest_id}\n lowest = {lowest}, lowest_id = {lowest_id}")

def main():
    args = parse_args()
    print (args)
    
    patterns = defaultdict(lambda: defaultdict(int))
    sample_mutation_count = defaultdict(lambda: defaultdict(int))
    icgc_counter = defaultdict(int)
    
    lines = slurp(args.file)
    headers = lines.pop(0)
    for l in lines:
        mutation = line2dict(headers, l)

        mut_from = mutation.get('mutated_from_allele')
        mut_to   = mutation.get('mutated_to_allele')

        ##Collect data for sample count
        mutation_id = mutation.get('icgc_mutation_id')
        sample_id   = mutation.get('icgc_sample_id')
        sample_mutation_count[sample_id][mutation_id] += 1

        ##Only count one pattern for each icgc_mutation_id
        icgc_id = mutation.get('icgc_mutation_id')
        if icgc_counter[icgc_id] == 0:
            patterns[mut_from][mut_to] +=1
            icgc_counter[icgc_id] = 1
    
    display_patterns(patterns)    
    print_high_low(sample_mutation_count)
    

if __name__ == "__main__":
    main()
