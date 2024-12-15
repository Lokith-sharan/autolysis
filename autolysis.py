import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tenacity import retry, stop_after_attempt, wait_fixed
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # Load environment variables from .env file

# Configure OpenAI API
def configure_openai():
    openai.api_key = os.environ.get("AIPROXY_TOKEN")
    openai.api_base = "https://api.openai.com/v1"  # Proxy or OpenAI API base URL
    if not openai.api_key:
        raise ValueError("API key not set. Please ensure AIPROXY_TOKEN is in your .env file.")

# Retry logic for OpenAI calls
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def query_llm(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            request_timeout=10
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return None

# Generate visualizations
def generate_visualizations(df, output_dir):
    numeric_df = df.select_dtypes(include=['number'])
    heatmap_path, pairplot_path = None, None

    # Correlation matrix
    if not numeric_df.empty:
        plt.figure(figsize=(6, 6))
        sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation Matrix")
        heatmap_path = os.path.join(output_dir, "correlation_matrix.png")
        plt.savefig(heatmap_path, dpi=100)
        plt.close()

    # Pairplot
    if len(numeric_df.columns) > 1:
        sns.pairplot(numeric_df)
        pairplot_path = os.path.join(output_dir, "pairplot.png")
        plt.savefig(pairplot_path, dpi=100)
        plt.close()

    return [heatmap_path, pairplot_path]

# Analyze data from CSV
def analyze_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        summary = df.describe(include='all').transpose()
        missing_values = df.isnull().sum()
        return df, summary, missing_values
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

# Create markdown report
def create_markdown_story(file_path, summary, missing_values, charts, output_dir):
    dataset_name = os.path.basename(file_path)
    markdown_content = f"""# Analysis of {dataset_name}

## Dataset Overview
This dataset has the following key characteristics:

### Summary Statistics
```plaintext
{summary.to_string()}

### Missing Values
```plaintext
{missing_values.to_string()}

## Visualizations

### Correlation Matrix
"""
    if charts[0]:
        markdown_content += f"![Correlation Matrix](correlation_matrix.png)\n"
    else:
        markdown_content += "No correlation matrix available (no numeric data).\n"

    markdown_content += """### Pairplot
"""
    if charts[1]:
        markdown_content += f"![Pairplot](pairplot.png)\n"
    else:
        markdown_content += "No pairplot available (insufficient numeric data).\n"

    markdown_content += """
## Narrative Insights
The analysis reveals significant trends and patterns in the dataset. Correlation matrix and pairplot provide insights into relationships among variables.

More detailed findings are generated below.
"""

    insights_prompt = (
        f"You are an AI assistant. Please provide a detailed analysis of the dataset based on these statistics and visualizations."
        f"\n\nSummary:\n{summary.to_string()}\n\nMissing Values:\n{missing_values.to_string()}"
    )
    insights = query_llm(insights_prompt)
    markdown_content += f"\n\n{insights}"

    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write(markdown_content)

    return readme_path

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    # Check if OpenAI API key is configured
    try:
        configure_openai()
        print("OpenAI API configured successfully.")
    except Exception as e:
        print(f"Error configuring OpenAI: {e}")
        sys.exit(1)

    # Extract directory name from file path to save visualizations and README
    output_dir = os.path.splitext(file_path)[0]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Starting analysis for {file_path}...")

    try:
        df, summary, missing_values = analyze_data(file_path)
        print("Data analysis complete.")
    except Exception as e:
        print(f"Error analyzing data: {e}")
        sys.exit(1)

    print("Generating visualizations...")
    charts = generate_visualizations(df, output_dir)
    print(f"Visualizations saved: {charts}")

    print("Creating markdown story...")
    try:
        readme_path = create_markdown_story(file_path, summary, missing_values, charts, output_dir)
        print(f"Markdown story created: {readme_path}")
    except Exception as e:
        print(f"Error creating markdown: {e}")
        sys.exit(1)

    print("Analysis completed successfully.")
    print(f"Results are saved in: {output_dir}/")

if __name__ == "__main__":
    main()
