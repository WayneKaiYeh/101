#Function separate the batches
def separate_batches(s):
    batches = []
    batch_start = 0 #set to 0 to mark the beginning of each batch.

    for i in range(len(s) - 7): #-7 cuz prefix + 4digits
        # Check for any alphabet character followed by four digits, and then 'P'/'p' followed by two alphanumeric characters
        if s[i].isalpha() and s[i+1:i+5].isdigit() and s[i+5].lower() == 'p' and s[i+6:i+8].isalnum():
             #if the pattern is recognnised
            if i != batch_start: 
                #if the current i is different from the batch_start, meaning it is a new batch start
                batches.append(s[batch_start:i]) #we append a new batch inn the list
            batch_start = i #updates batch_start to the current index i. This marks the beginning of the new batch.
    
    batches.append(s[batch_start:])  # Add the last batch
    return batches


def validate_and_extract_log(s):
    
    #create a list
    batches_info = []

    #Step1: we separate the batches
    batches = separate_batches(s)

    #Loop through all the batches
    for batch in batches:
        dict = {}

        #Bet the Brefix
        prefix = batch[0]

        #Batch id
        batch_id = batch[1:5]

        #Product code
        product_code = batch[6:8]
        if not (product_code.isupper() and len(product_code) == 2 and product_code.isalpha()):
            return "invalid"

        # Find the index of 'P'
        p_index = batch.find('P')  
        if p_index == -1 or not batch[p_index+1:p_index+3].isalpha() or not batch[p_index+1:p_index+3].isupper():
            return "invalid"

        # Ensure 'P' is followed by two uppercase letters, then 'Q'
        if batch[p_index+3] != 'Q':
            return "invalid"



        #Quantity
        q_index = batch.lower().find('q', p_index)
        d_index = batch.lower().find('d', q_index)

        if q_index == -1 or d_index == -1:
            return "invalid"  # Correctly handle missing Q or D
        
        quantity = batch[q_index+1:d_index]
        if not quantity.isdigit():  # Ensure quantity is not None and is digits
            return "invalid"


        #Date
        date = batch[d_index+1:]
        if not (date.isdigit() and len(date) == 8):
            return "invalid"



        ### now we check the validation ###
        if ' ' in s:
            return "invalid"
           
        # If not 'B', return "invalid"
        # an invalid batch is detected, immediately exits the entire function and returns "invalid" 
        elif prefix != 'B':

            return "invalid"
            
        elif not (len(batch_id) == 4 and batch_id.isdigit() == True):
            return "invalid"

        elif p_index == -1 or batch[p_index] != 'P':
            return "invalid"

        elif not (product_code.isupper() == True and len(product_code) == 2 and product_code.isalpha()== True):
            return "invalid"
        
        elif not(quantity.isdigit()):
            return "invalid"
        

        # Validation for Quantity (check if 'Q' is uppercase)
        elif batch[q_index] != 'Q':
            return "invalid"

        elif batch[d_index] != 'D':
            return "invalid"

        elif not (date.isdigit() and len(date) == 8):
            return "invalid"
        
        elif (date.isdigit() and len(date) == 8): 
            
            year, month, day = int(date[:4]), int(date[4:6]), int(date[6:8])
            if not (2000 <= year <= 2099) or not (1 <= month <= 12) or not (1 <= day <= 31):
                return "invalid"
            
            else:
                #add the info
                batches_info.append({
                'Batch ID': batch_id,
                'Product Code': product_code,
                'Quantity': int(quantity),
                'Date': date
                })
 
        
    return batches_info
