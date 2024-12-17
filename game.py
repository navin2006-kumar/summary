import streamlit as st
import json
st.title("Sales Summary Report")

st.sidebar.title("Upload Sales Data")
file = st.sidebar.file_uploader("Upload the sales data JSON file", type=["json"])

if file is not None:
    try:
        sales_data = json.load(file)
        total_sold = 0
        total_discounts = 0
        total_taxes = 0
        total_amount = 0

        for item in sales_data:
        
            gross = item['quantity'] * item['price_per_unit']
            discount = gross * item['discount']
            net = gross - discount
            tax = net * item['tax_rate']
            final = net + tax
            
            st.write("***Item:***",item['item'])
            st.write("***Quantity Sold:***", item['quantity'])
            st.write("***Gross Amount***: $",gross)
            st.write("***Discount Amount***:$",discount)
            st.write("**Net Amount***: $",net)
            st.write("***Tax Amount***: $",tax)
            st.write("***Final Amount***: $",final)
            st.write("#" * 40)
        
            total_sold += item['quantity']
            total_discounts += discount
            total_taxes += tax
            total_amount += final
        st.write("**Total Number of Items Sold**:",total_sold)
        st.write("**Total Discounts Given**: $",total_discounts)
        st.write("**Total Taxes Collected**: $",total_taxes)
        st.write("**Total Sales Amount**: $",total_amount)
    except json.JSONDecodeError:
        st.error("Error: The file is not a valid JSON file or is corrupted.")
else:
    st.info("Upload a correct json file")