# Author Name: Guoxing Zhu
# The student ID: 24308319.
# This is the code designed to solve the Tasks for the given project.

def Task1(CSVfile, category):
    # To open the given CSV file and read its content.
    with open(CSVfile,'r', encoding='utf-8') as file:
        lines=file.readlines() 
    
    # To extract the header and data rows.
    header = lines[0].strip().split(',')
    data_lines = lines[1:]
    
    # To determine the indices of the 'category', 'discounted_price $' and 'product_id' columns.
    category_index = header.index('category')
    price_index = header.index('discounted_price $')
    id_index = header.index('product_id')
    
    # To convert the strings in the 'category' to lowercase.
    category = category.lower()
    
    specific_products = []
    
    # To filter the specific products for the given category, and to extract the data from two columns  
    # "product_id" and "price" that meet the conditions and add them to the specific_products list.     
    for line in data_lines:
        rows = line.strip().split(',')
        if rows[category_index].lower() == category:
            product_id = rows[id_index].lower()
            price = float(rows[price_index])
            specific_products.append((product_id, price))
    
    # To set two variables to store the specific products with the highest and lowest prices, which may appear 
    # more than once.
    if not specific_products:
        return []
    highest_product = specific_products[0]
    lowest_product = specific_products[0]

    # To iterate all products to find the first specific with the highest and lowest prices.
    for specific_product in specific_products:
        if specific_product[1] > highest_product[1]:
            highest_product = specific_product
        if specific_product[1] < lowest_product[1]:
            lowest_product = specific_product
    
    # To get the product IDs with the highest and lowest prices
    product_ID1 = highest_product[0]
    product_ID2 = lowest_product[0]
    
    return [product_ID1, product_ID2]


def Task2(CSVfile, category):
    # To open the given CSV file and read its content.
    with open(CSVfile,'r', encoding='utf-8') as file:
        lines=file.readlines()
    
    # To extract the header and data rows.
    header = lines[0].strip().split(',')
    data_lines = lines[1:]
     
    # To determine the indices of the 'category', 'actual_price $' and 'rating_count' columns. 
    category_index = header.index('category')
    price_index = header.index('actual_price $')
    rating_index = header.index('rating_count')
    
    # To filter the specific products for the given category, and to extract the data from the column "price" 
    # that meet the conditions and add them to the specific_products list.   
    specific_products = []
    for line in data_lines:
        rows = line.strip().split(',')
        if rows[category_index] == category:
            rating_count = int(rows[rating_index])  # To convert the data from the rating count to integer type.
            if rating_count > 1000:  # To filter the products which rating count is greater than 1000.
                price = float(rows[price_index])  # To convert the actual price to float type.
                specific_products.append(price)
    
    price_sum = sum(specific_products)
    price_count = len(specific_products)
    mean = price_sum / price_count #To calculate the mean of actual price.
        
    specific_products_sorted = sorted(specific_products)
    
    # To calculate the median of the actual price.
    if price_count % 2 == 0:
        median = (specific_products_sorted[price_count//2-1]+specific_products_sorted[price_count//2])/2
    else:
        median = specific_products_sorted[(price_count+1)//2-1]
      
    # To calculate the mean absolute deviation.
    absolute_deviation = 0.0
    for i in range(price_count):
        absolute_deviation += abs(specific_products[i]-mean)
    MD = absolute_deviation/price_count
    
    #To return the values rounded to four decimal places
    return [round(mean,4), round(median,4), round(MD,4)]

def Task3(CSVfile):
    # To open the given CSV file and read its content.
    with open(CSVfile,'r', encoding='utf-8') as file:
        lines=file.readlines()
    
    # To extract the header and data rows.
    header = lines[0].strip().split(',')
    data_lines = lines[1:]
    
    # To determine the indices of the 'category', 'discount_percentage %' and 'rating' columns.
    category_index = header.index('category')
    discount_index = header.index('discount_percentage %')
    rating_index = header.index('rating')
        
    categories = [] # To initialize the list called 'categories'.
    
    for line in data_lines:
        rows = line.strip().split(',')
        discount_percentage = float(rows[discount_index])
        rating = float(rows[rating_index])
        category = rows[category_index]

        # To filter the products which rarting is in the range 3.3 <= rating <= 4.3.
        if 3.3 <= rating <= 4.3:

        
            # Check if the current 'category' already exists. If it does, add the 'discount_percentage' for
            # the specific 'category' to the sublist 'cat' in the 'categories' list.
            # The list categories and its sublist cat look like this:
            # categories = [cat, ...]
            # cat = [category, [discount_percentage, ...]]
            found = False
            for cat in categories:
                if cat[0] == category:
                    cat[1].append(discount_percentage)
                    found = True
                    break
            
            # If the current 'category' does not exist, create a new cat sublist.
            if not found:
                categories.append([category, [discount_percentage]])
            
    STD_list = [] # To initialize the list of standard deviation.
    for cat in categories: 
        discounts = cat[1]
        # To ensure that the discounts list has elements to avoid ZeroDivisionError.
        if discounts: 
            mean = sum(discounts) / len(discounts)
            square = 0
        
            for i in range(len(discounts)):
                square += (discounts[i]-mean)**2
            Variance = square / (len(discounts)-1) # To get the variance.
            STD = Variance ** 0.5 #To get the value of the standard deviation.
            STD = round(STD, 4) # To save the STD values rounded to four decimal places.
            STD_list.append(STD) # To append the STD values into the STD_list.
            
    STD_list.sort(reverse = True)# To sort the output in the descending order.
    
    return STD_list

def Task4(CSVfile, TXTfile, category):
    ID = Task1(CSVfile, category) # to call the Task1 function and assign its returned result to the variable 'ID'.
    
    with open(TXTfile, 'r', encoding='utf-8') as file:# To open the given TXT file and read its content.
        lines = file.readlines()
    
    outer_list = []
    current_year = 0
    product_list = []
    
    # To initialize the lists. And the expected structure of the lists looks like this:
    #outer_list = [[current_year, [[product_id, sales], [product_id, sales]...]],current_year, [[product_id, sales], [product_id, sales]...]...]
    #year_data = [current_year, [[product_id, sales], [product_id, sales]...]]
    #product_list = [[product_id, sales], [product_id, sales]...]
    #product = [product_id, sales]  
    for line in lines:
        line = line.strip()#Iterate through each line, extract a line, and remove leading and trailing spaces as well as newline characters.
        if line.startswith("Year:"):
            # If encounter with "Year:", save the previous product list and start a list.
            outer_list.append([current_year, product_list])
            year_data = line.split(',')
            current_year = int(year_data[0].strip().split(':')[1].strip())  # Extract and convert the year part to an integer
            product_list = []  # Initialize the list product_list
            for product in year_data[1:]:
                product_id = product.split(':')[0]
                sales = product.split(':')[1]
                product_list.append([product_id.strip().lower(), float(sales.strip())])
    
    outer_list.append([current_year, product_list])
    del outer_list[0]     
    
    sales_data_highest = []  # To initialize and to store the highest discount sales data for each year.
    sales_data_lowest = []  # To initialize and to store the lowest discount sales data for each year.
    for year_data in outer_list:
        
        product_list = year_data[1]  # To obtain the product data list for the current year.
        highest_sales = 0.0 # Initialize the highest and lowest sales as 0.0
        lowest_sales = 0.0  
        
        for product in product_list:
            product_id = product[0]
            sales = product[1]
            
            if product_id == ID[0]:
                highest_sales = sales
            elif product_id == ID[1]:
                lowest_sales = sales
        
        #To respectively add the highest and lowest sales data to the sales_data_highest and sales_data_lowest lists.
        sales_data_highest.append(highest_sales)
        sales_data_lowest.append(lowest_sales)
        
    x = sales_data_highest
    x_mean = sum(x) / len(x)
    y = sales_data_lowest
    y_mean = sum(y) / len(y)
    numerator = 0.0 
    denominator_xpart = 0.0 
    denominator_ypart = 0.0 
    r = 0.0
   
    # To calculate the correlation coefficient
    for i in range(len(x)):
        numerator += (x[i]-x_mean)*(y[i]-y_mean) # To calculate the value of the numerator
        denominator_xpart += (x[i]-x_mean)**2 # To calculate the value of the x part in the denominator.
        denominator_ypart += (y[i]-y_mean)**2 # To calculate the value of the y part in the denominator.
    denominator = (denominator_xpart * denominator_ypart)**0.5
    r = numerator / denominator
    
    return round(r,4)

def main(CSVfile, TXTfile, category):
    
    OP1 = Task1(CSVfile, category)
    if not OP1: # Check if the input category parameter exists
        return "Please enter the right category name"
    
    OP2 = Task2(CSVfile, category)
    OP3 = Task3(CSVfile)
    OP4 = Task4(CSVfile, TXTfile, category)
    
    return OP1, OP2, OP3, OP4