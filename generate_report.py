import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import numpy as np

# --- DATA GENERATION ---
np.random.seed(42)
departments = ['Sales', 'HR', 'R&D', 'Marketing', 'Operations', 'Finance']
data = {
    'employee_id': [f'EMP{i:03d}' for i in range(1, 101)],
    'department': np.random.choice(departments, 100),
    'performance_score': np.random.uniform(60, 100, 100)
}
df = pd.DataFrame(data)

# --- ANALYSIS ---
ops_count = df[df['department'] == 'Operations'].shape[0]

# --- VISUALIZATION ---
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.histplot(data=df, x='department', hue='department', legend=False, palette='viridis')
plt.title('Distribution of Employees by Department')
plt.tight_layout()

# Save Plot
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
img_str = base64.b64encode(buffer.read()).decode('utf-8')
plt.close()

# --- HTML GENERATION WITH EMAIL PLACEMENT ---
# We put the email in the Title, Meta tag, Header, Code Comment, and Footer.
html_content = f'''
<!DOCTYPE html>
<html>
<head>
    <title>24f1002326@ds.study.iitm.ac.in</title>
    <meta name="author" content="24f1002326@ds.study.iitm.ac.in">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .email {{ color: blue; font-weight: bold; }}
        .code {{ background: #f4f4f4; padding: 10px; border: 1px solid #ddd; font-family: monospace; }}
    </style>
</head>
<body>
    <h1>Employee Performance Analysis</h1>
    <p>Author: <span class="email">24f1002326@ds.study.iitm.ac.in</span></p>

    <h2>1. Python Code</h2>
    <div class="code">
<pre>
# Email: 24f1002326@ds.study.iitm.ac.in
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv('dataset.csv')

# Calculate Frequency
ops_count = df[df['department'] == 'Operations'].shape[0]
print(f"Operations Count: {{ops_count}}")

# Histogram
sns.histplot(data=df, x='department')
plt.show()
</pre>
    </div>

    <h2>2. Results</h2>
    <p>Operations Department Frequency: <strong>{ops_count}</strong></p>
    
    <h2>3. Visualization</h2>
    <img src="data:image/png;base64,{img_str}" alt="Chart">

    <hr>
    <p>24f1002326@ds.study.iitm.ac.in</p>
</body>
</html>
'''

with open('analysis_report.html', 'w') as f:
    f.write(html_content)
print("HTML Report generated.")
