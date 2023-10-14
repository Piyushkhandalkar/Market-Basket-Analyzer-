# Market-Basket-Analyzer-
This Is A Market Basket Analyzer Made In Python the project is a web application built using the Flask framework. It's designed to analyze transaction data, often from a retail or e-commerce context, and extract insights using Market Basket Analysis techniques. Users can upload a CSV file containing transaction data, and the application performs the following tasks:

   - Cleans and preprocesses the data by converting non-numeric values ('Yes' and 'No') to binary values (1 and 0).
   - Applies the Apriori algorithm to find frequent itemsets (combinations of items that appear together frequently).
   - Generates association rules based on these frequent itemsets.
   - Produces visualizations, including pie charts for item distribution in transactions, and bar charts for the support of frequent itemsets and the confidence of association rules.
   - Presents the results, including the total number of transactions and unique items, and a list of association rules, on a web page.

This web application can be used for market basket analysis in various contexts, such as understanding purchasing patterns in a retail store, suggesting related products to customers, and optimizing product placement on e-commerce websites.

PREREQUISITES

1. Python 3.6 or higher

2. Flask Framework : Flask is used to build the web application. You can install it using pip, the Python package manager:

    ```bash
    pip install Flask
    ```

3. **Pandas**: The Pandas library is used for data manipulation:

    ```bash
    pip install pandas
    ```

4. **Matplotlib**: Matplotlib is used for data visualization:

    ```bash
    pip install matplotlib
    ```

5. **mlxtend Library**: The mlxtend library is used for implementing the Apriori algorithm and association rule mining:

    ```bash
    pip install mlxtend
    ```

**Installation:**

After you have the prerequisites installed, you can set up and run the application using the following steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

   Make sure that the `requirements.txt` file in your project directory includes the necessary dependencies, which you can list as shown above.

3. **Run the Application:**

    ```bash
    python app.py
    ```

   This command starts the Flask development server, and your application will be accessible at `http://localhost:5000/` in your web browser.

