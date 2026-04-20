from FileReader import line2dict, slurp, parse_args
from collections import defaultdict

def print_high_low(sample_mutation_count):
    lowest     = float('inf')
    highest    = 0 
    lowest_id  =  highest_id =  ''
   
    ##Go over all the 
    for sample in sample_mutation_count:
        ##count how many unique mutations per sample_id
        count = len(sample_mutation_count[sample].keys())
        if count < lowest:
            lowest = count
            lowest_id = sample
        if count > highest:
            highest = count
            highest_id = sample
    
    ##Print out the sample ids with the most and least mutation counts
    print(f"icgc_sample_id with highest unique icgc_mutation_id is {highest_id} with {highest} mutation count")
    print(f"icgc_sample_id with lowest unique icgc_mutation_id is {lowest_id} with {lowest} mutation count")
   
def main():
    args = parse_args()
    
    sample_mutation_count = defaultdict(lambda: defaultdict(int))
    
    lines = slurp(args.file)
    headers = lines.pop(0)
    for l in lines:
        ##Create a dict from each line in input
        mutation = line2dict(headers, l)

        mutation_id = mutation.get('icgc_mutation_id') ##Also used for the patter count
        sample_id   = mutation.get('icgc_sample_id')
        sample_mutation_count[sample_id][mutation_id] += 1
        
    print_high_low(sample_mutation_count)
    

if __name__ == "__main__":
    main()
