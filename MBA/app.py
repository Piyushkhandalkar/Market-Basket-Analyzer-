import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg'
import matplotlib.pyplot as plt
from flask import Flask, request, render_template
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

app = Flask(__name__)

# Function to perform market basket analysis and generate visualizations
def perform_market_basket_analysis(df):
    # Clean the data (convert non-numeric values to 0 or 1)
    df = df.applymap(lambda x: 1 if x == 'Yes' else 0)
    # Preprocess the data for Apriori algorithm
    transactions = df.values.tolist()
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

    # Perform Apriori analysis
    min_support = 0.01
    frequent_itemsets = apriori(df_encoded, min_support=min_support, use_colnames=True)

    # Generate association rules
    min_confidence = 0.1
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

    # Visualization: Pie chart for the distribution of items in transactions
    item_counts = df_encoded.sum(axis=0).sort_values(ascending=False)
    labels = item_counts.index
    sizes = item_counts.values
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Distribution of Items in Transactions")
    plt.tight_layout()
    item_distribution_plot = "static/item_distribution_plot.png"  # Save the pie chart as an image
    plt.savefig(item_distribution_plot)
    plt.close()

    # Visualization: Bar chart for support of frequent itemsets
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(frequent_itemsets)), frequent_itemsets['support'], tick_label=frequent_itemsets['itemsets'])
    plt.xticks(rotation=90)
    plt.xlabel("Frequent Itemsets")
    plt.ylabel("Support")
    plt.title("Support of Frequent Itemsets")
    plt.tight_layout()
    support_plot = "static/support_plot.png"  # Save the plot as an image
    plt.savefig(support_plot)
    plt.close()

    # Visualization: Bar chart for confidence of association rules
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(rules)), rules['confidence'], tick_label=rules['antecedents'].astype(str) + " => " + rules['consequents'].astype(str))
    plt.xticks(rotation=90)
    plt.xlabel("Association Rules")
    plt.ylabel("Confidence")
    plt.title("Confidence of Association Rules")
    plt.tight_layout()
    confidence_plot = "static/confidence_plot.png"  # Save the plot as an image
    plt.savefig(confidence_plot)
    plt.close()

    # Prepare analysis result with HTML image tags for embedding plots
    analysis_result = "Market Basket Analysis Results:\n\n"
    analysis_result += "Total number of transactions: {}\n".format(len(df))
    analysis_result += "Total number of unique items: {}\n".format(len(df.columns) - 1)  # Exclude the 'Item(s)' column
    analysis_result += "\nAssociation Rules:\n"
    analysis_result += rules.to_string(index=False)

    return analysis_result, item_distribution_plot, support_plot, confidence_plot

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Flask route that handles the form submission for a web application.
    Reads an uploaded CSV file, performs market basket analysis on the data, and returns the analysis result
    to be displayed on a result.html template.

    :return: The analysis result, which is a string containing the market basket analysis results and association rules.
    """
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file and uploaded_file.filename:
            df = pd.read_csv(uploaded_file)
            analysis_result, item_distribution_plot, support_plot, confidence_plot = perform_market_basket_analysis(df)
            return render_template('result.html', analysis_result=analysis_result, item_distribution_plot=item_distribution_plot, support_plot=support_plot, confidence_plot=confidence_plot)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
