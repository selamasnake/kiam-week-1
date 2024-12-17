# kiam-week-1
This project analyzes financial news headlines to gain insights into the structure and sentiment of the articles. And historical stock data, to analyze technical indicators and measure the correlation between sentiment and daily returns and other measures.

Key activities include:
    * Cleaning and preprocessing the data.
    * Sentiment Analysis and Topic Modelling.
    * Calculating Technical Indicators for stocks.
    * Correlation Analysis

### File Structure
The project is organized as follows:

* data/: Stores all data-related files.
* src/notebooks/: Contains Jupyter notebooks for interactive data analysis.
* scripts/: Python scripts for reusable code functions.
* results/figures: Contains visualizations generated through EDA.
* requirements.txt: Contains the necessary dependencies to run the project.

### Tools, Frameworks, and Libraries Used

#### Tools:
    * Jupyter Notebooks: Used for interactive analysis and visualization.
    * Git: Version control for managing changes.
    * Python: Primary programming language for data processing and analysis.

#### Frameworks & Libraries:
* Pandas: For data manipulation and cleaning (e.g., handling missing values, data transformation).
* NumPy: For numerical operations, especially when handling arrays and large datasets.
* Matplotlib: For creating static, animated, and interactive visualizations (e.g., bar charts, histograms).
* Seaborn: For statistical data visualization (e.g., heatmaps, box plots).
* Vader: For Sentiment Analysis.
* Gensim: Used for topic modelling.
  
### User Guide: How to Run the Project

1. Clone the repository and navigate to the project
    ```
    https://github.com/selamasnake/kiam-week-1.git
    cd kiam-week-0
    ```
Make sure a virtual environment is axtivated then,
2. Install dependencies : Install the required Python libraries by using the requirements.txt
    ```
    pip install -r requirements.txt

    ```
3. Run the notebooks
   Navigate to the src/notebooks directory, which are divided by stocks folder and basic data preparation and eda notebooks.
   Start with the `data_preparation.ipynb` notebook to load the data and clean it.
   The `eda.ipynb` notebook analyzes financial headline data.
   Under Stocks, go to each stocks and visualize its technical indicators and calculate its correlation matrix.
    Visualizations will be generated at each step to interpret the data. 

5. Running Python Scripts
    Navigate to the scripts directory,
    Run the Python scripts directly `utils.py` ,`eda.py`, `plotpy`, `text.analyzer.py` etc to execute parts of the data cleaning & analysis process.
