#Function separate the batches
def separate_batches(s):
    batches = []

    #set to 0 to mark the beginning of each batch.
    batch_start = 0 

    #-7 cuz prefix + 4digits
    for i in range(len(s) - 7): 
        # Check for any alphabet character followed by four digits, and then 'P'/'p' followed by two alphanumeric characters
        if s[i].isalpha() and s[i+1:i+5].isdigit() and s[i+5].lower() == 'p' and s[i+6:i+8].isalnum():

            #if the pattern is recognnised
            if i != batch_start: 
                #if the current i is different from the batch_start, meaning it is a new batch start

                #we append a new batch inn the list
                batches.append(s[batch_start:i]) 
                
            #updates batch_start to the current index i. This marks the beginning of the new batch.
            batch_start = i 
    
    batches.append(s[batch_start:])  # Add the last batch
    return batches



def validate_and_extract_log(s):
    
    if not s:
        return "invalid"
    
    batches_info = []  

    batches = separate_batches(s)  #we separate the batches

    for batch in batches:
        # B the prefix
        prefix = batch[0]

        # Batch id
        batch_id = batch[1:5]

        # Product code validation
        product_code = batch[6:8]
        if not (product_code.isupper() and len(product_code) == 2 and product_code.isalpha()):
            return "invalid"

        # Find the index of 'P'
        p_index = batch.find('P')
        if p_index == -1 or not batch[p_index+1:p_index+3].isalpha() or not batch[p_index+1:p_index+3].isupper():
            return "invalid"
        

        # Adjusted to ensure 'P' is followed by two uppercase letters, which we've validated as the product code
        # and then directly finding 'Q' after the product code without assuming its immediate position
        q_index = batch.find('Q', p_index + 3)
        d_index = batch.find('D', q_index)

        # Correctly handle missing 'Q' or 'D'
        if q_index == -1 or d_index == -1:
            return "invalid"  
        
        # Ensure quantity is digits
        quantity = batch[q_index+1:d_index]
        if not quantity.isdigit():  
            return "invalid"

        # Date validation
        date = batch[d_index+1:]
        if not (date.isdigit() and len(date) == 8):
            return "invalid"

        # Additional validations
        if ' ' in s or prefix != 'B' or not batch_id.isdigit() or not (len(batch_id) == 4) or batch[q_index] != 'Q' or batch[d_index] != 'D':
            return "invalid"


        # Validate date format
        year, month, day = int(date[:4]), int(date[4:6]), int(date[6:8])
        if not (2000 <= year <= 2099) or not (1 <= month <= 12) or not (1 <= day <= 31):
            return "invalid"
        else:
            batches_info.append({
                'Batch ID': batch_id,
                'Product Code': product_code,
                'Quantity': int(quantity),
                'Date': date
            })

    return batches_info