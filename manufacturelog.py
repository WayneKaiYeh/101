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
            return "Invalid"

        # Find the index of 'P'
        p_index = batch.find('P')  

        #Quantity
        q_index = batch.lower().find('q',8)
        d_index = batch.lower().find('d', q_index)
        if q_index != -1 and d_index != -1:
            quantity = batch[q_index+1:d_index]
        else:
            quantity = None

        #Date
        if d_index != -1:
            date = batch[d_index+1:]
        else:
            date = None


        ### now we check the validation ###
        if ' ' in s:
            return "Invalid"
           
        # If not 'B', return "Invalid"
        # an invalid batch is detected, immediately exits the entire function and returns "Invalid" 
        elif prefix != 'B':

            return "Invalid"
            
        elif not (len(batch_id) == 4 and batch_id.isdigit() == True):
            return "Invalid"

        elif p_index == -1 or batch[p_index] != 'P':
            return "Invalid"

        elif not (product_code.isupper() == True and len(product_code) == 2 and product_code.isalpha()== True):
            return "Invalid"
        
        elif not(quantity.isdigit()):
            return "Invalid"
        
        # Validation for Quantity (check if 'Q' is uppercase)
        elif batch[q_index] != 'Q':
            return "Invalid"


        elif batch[d_index] != 'D':
            return "Invalid"


        elif not (date.isdigit() and len(date) == 8):
            return "Invalid"
        
        elif (date.isdigit() and len(date) == 8): 
            
            year, month, day = int(date[:4]), int(date[4:6]), int(date[6:8])
            if not (2000 <= year <= 2099) or not (1 <= month <= 12) or not (1 <= day <= 31):
                return "Invalid"
            
            else:
                #add the info
                batches_info.append({
                'Batch ID': batch_id,
                'Product Code': product_code,
                'Quantity': int(quantity),
                'Date': date
                })
 
        
    return batches_info
