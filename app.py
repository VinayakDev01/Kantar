# Import necessary libraries
from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Mainpage.html')
def main():
    excel_file_path = r'C:\Users\Admin\Downloads\AA\VS_Urban_Climate_BC_Data_variance_Label.xls'
#Main Page
    if os.path.exists(excel_file_path):
        df_raw = pd.read_excel(excel_file_path,sheet_name=0)  # Assuming headers are in the first row

        # Get total count of Total Raw data
        total_raw = len(df_raw)

        df_audit = pd.read_excel(excel_file_path,sheet_name=1, header=0)


        # Get total count of auditr data
        total_audit = len(df_audit)
        
         # Calculate the non-audited data
        total_Naudit = total_raw - total_audit
        labels = ['Audit', 'Non-Audit']

        # Variance Count
        selected_labels = ['MM_AGE', 'MM_EDUCATION', 'MM_HH_MEMBERS','MM_OWNED_RENTED','MM_INTER_PLACE_SP','MM_C8','BC variance']# Replace with your desired labels

        # Filter the DataFrame based on selected labels
        df_selected = df_audit[df_audit.columns.intersection(selected_labels)]

        data_variance = df_selected.iloc[0, :].tolist()  # Assuming the first row contains data for the pie chart

         # Calculate the sum of variance data
        total_variance_count = sum(data_variance)

        return render_template('Mainpage.html',total_raw=total_raw, total_audit=total_audit, total_Naudit=total_Naudit, total_variance_count=total_variance_count,labels=labels)
    else:
        return 'Excel file not found!'
    
#Audit Page
@app.route('/Audit.html')
def audit():
    excel_file_path = r'C:\Users\Admin\Downloads\AA\VS_Urban_Climate_BC_Data_variance_Label.xls'
    if os.path.exists(excel_file_path):
        df_audit = pd.read_excel(excel_file_path,sheet_name=1, header=0)  # Assuming headers are in the first row

        # Specify the labels you want to include in the pie chart
        selected_labels = ['MM_AGE','MM_EDUCATION']  # Replace with your desired labels # Replace with your desired labels

        # Filter the DataFrame based on selected labels
        df_selected = df_audit[df_audit.columns.intersection(selected_labels)]

        # Extract data for the pie chart
        labels = df_selected.columns.tolist()  # Use column headers as labels
        data = df_selected.iloc[0, :].tolist()  # Assuming the first row contains data for the pie chart

        # Get total count of rows
        total_Arows = len(df_audit)
    
    #Variance Report
        # Variance Count
        selected_variance = ['MM_AGE', 'MM_EDUCATION', 'MM_HH_MEMBERS','MM_OWNED_RENTED','MM_INTER_PLACE_SP','MM_C8','BC variance']# Replace with your desired labels

        # Filter the DataFrame based on selected labels
        df_var = df_audit[df_audit.columns.intersection(selected_variance)]

        data_var = df_var.iloc[0, :].tolist()  # Assuming the first row contains data for the pie chart

         # Calculate the sum of variance data
        total_variance = sum(data_var)
         # Calculate the sum of data

        return render_template('Audit.html', labels=labels, data=data, total_Arows=total_Arows,total_variance=total_variance)
    else:
        return 'Excel file not found!'

#Variance Report
@app.route('/Variance.html')
def variance():
    excel_file_path = r'C:\Users\Admin\Downloads\AA\VS_Urban_Climate_BC_Data_variance_Label.xls'
    if os.path.exists(excel_file_path):
        df_variance = pd.read_excel(excel_file_path,sheet_name=1, header=0)  # Assuming headers are in the first row

        # Specify the labels you want to include in the pie chart
        selected_Varlabels = ['MM_AGE', 'MM_EDUCATION', 'MM_HH_MEMBERS','MM_OWNED_RENTED','MM_INTER_PLACE_SP','MM_C8','BC variance']  # Replace with your desired labels # Replace with your desired labels

        # Filter the DataFrame based on selected labels
        df_Varselect = df_variance[df_variance.columns.intersection(selected_Varlabels)]

        # Extract data for the pie chart
        Varlabels = df_Varselect.columns.tolist()  # Use column headers as labels
        Vardata = df_Varselect.iloc[0, :].tolist()  # Assuming the first row contains data for the pie chart

        # Get total count of rows
        total_Varrows = len(df_variance)
         # Calculate the sum of data
        total_variance = sum(Vardata)

        return render_template('Variance.html', Varlabels=Varlabels, Vardata=Vardata, total_Varrows=total_Varrows,total_variance_count=total_variance)
    else:
        return 'Excel file not found!'
    
@app.route('/Nav.html')
def Nav():
    return render_template('Nav.html')
@app.route('/logo.jpeg')
def logo():
    return render_template('logo.jpeg')
@app.route('/audited_data.html')
def audited_data():
    excel_file_path = r'C:\Users\Admin\Downloads\AA\VS_Urban_Climate_BC_Data_variance_Label.xls'
    
    try:
        # Read the Excel file
        df_audited = pd.read_excel(excel_file_path,sheet_name=1)

        # Convert DataFrame to HTML
        table_html = df_audited.to_html(classes='table table-striped')

        return render_template('audited_data.html', table_html=table_html)

    except Exception as e:
        return f"Error reading Excel file: {str(e)}"
    
@app.route('/raw_data.html')
def raw_data():
    excel_file_path = r'C:\Users\Admin\Downloads\AA\VS_Urban_Climate_BC_Data_variance_Label.xls'
    
    try:
        # Read the Excel file
        df_raw = pd.read_excel(excel_file_path,sheet_name=0)

        # Convert DataFrame to HTML
        table_html = df_raw.to_html(classes='table table-striped')

        return render_template('raw_data.html', table_html=table_html)

    except Exception as e:
        return f"Error reading Excel file: {str(e)}"    

@app.route('/variance_data.html')
def variance_data():
    excel_file_path = r'C:\Users\Admin\Downloads\AA\VS_Urban_Climate_BC_Data_variance_Label.xls'
    
    try:
        # Read the Excel file
        df_variance = pd.read_excel(excel_file_path,sheet_name=1,header=0)

        # Specify the labels you want to include in the pie chart
        selected_Varlabels = ['AOLVAR_8','MM_AGE', 'MM_EDUCATION', 'MM_HH_MEMBERS','MM_OWNED_RENTED','MM_INTER_PLACE_SP','MM_C8','BC variance']  # Replace with your desired labels # Replace with your desired labels

        # Filter the DataFrame based on selected labels
        df_Varselect = df_variance[df_variance.columns.intersection(selected_Varlabels)]

        # Convert DataFrame to HTML
        table_html = df_Varselect.to_html(classes='table table-striped')

        return render_template('variance_data.html', table_html=table_html)

    except Exception as e:
        return f"Error reading Excel file: {str(e)}"   

@app.route('/login.html')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
