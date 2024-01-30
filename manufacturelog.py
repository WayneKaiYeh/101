#Function separate the batches
def separate_batches(s):
    batches = []
    batch_start = 0

    for i in range(len(s) - 7):
        # Check for any alphabet character followed by four digits, and then 'P'/'p' followed by two alphanumeric characters
        if s[i].isalpha() and s[i+1:i+5].isdigit() and s[i+5].lower() == 'p' and s[i+6:i+8].isalnum():
            if i != batch_start:
                batches.append(s[batch_start:i])
            batch_start = i
    
    batches.append(s[batch_start:])  # Add the last batch
    return batches


def validate_and_extract_log(s):
    
    #create a list
    batches_info = []

    #Strep1: we separate the batches
    batches = separate_batches(s)

    
    #Loop through all the batches
    for batch in batches:
        dict = {}

        #get the prefix
        prefix = batch[0]


        #batch id
        batch_id = batch[1:5]

        #product code
        product_code = batch[6:8]

        #quantity
        q_index = batch.lower().find('q')
        d_index = batch.lower().find('d', q_index)
        if q_index != -1 and d_index != -1:
            quantity = batch[q_index+1:d_index]
        else:
            quantity = None

        #date
        if d_index != -1:
            date = batch[d_index+1:]
        else:
            date = None

        #now we check the validation
            

        if prefix != 'B':
            # If not 'B', return "Invalid" and skip to the next batch
            return "Invalid"
            #continue
        




            


    return batches


    #return batches_info or "invalid"



