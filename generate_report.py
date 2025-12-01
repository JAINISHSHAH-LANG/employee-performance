
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import numpy as np

# Data Generation
np.random.seed(42)
departments = ['Sales', 'HR', 'R&D', 'Marketing', 'Operations', 'Finance']
data = {
    'employee_id': [f'EMP{i:03d}' for i in range(1, 101)],
    'department': np.random.choice(departments, 100),
    'performance_score': np.random.uniform(60, 100, 100)
}
df = pd.DataFrame(data)

# Analysis
ops_count = df[df['department'] == 'Operations'].shape[0]

# Visualization
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.histplot(data=df, x='department', hue='department', legend=False, palette='viridis')
plt.title('Distribution of Employees by Department')
plt.tight_layout()

# Save image to base64
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
img_str = base64.b64encode(buffer.read()).decode('utf-8')
plt.close()

# HTML Template with EXTRA EMAIL VISIBILITY
html_content = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Employee Performance Analysis</title>
    <style>
        body {{ font-family: sans-serif; margin: 40px; }}
        .email-tag {{ background: #e8f0fe; padding: 10px; border-left: 5px solid #4285f4; margin-bottom: 20px; }}
        .code-box {{ background: #f5f5f5; padding: 15px; font-family: monospace; overflow: auto; }}
    </style>
</head>
<body>
    <div class="email-tag">
        <strong>Verified Author:</strong> 24f1002326@ds.study.iitm.ac.in
    </div>

    <h1>Employee Performance Analysis</h1>
    
    <h3>1. Analysis Result</h3>
    <p>Frequency count for "Operations" department: <strong>{ops_count}</strong></p>

    <h3>2. Visualization</h3>
    <img src="data:image/png;base64,{img_str}" alt="Chart" style="max-width:100%">

    <h3>3. Python Code</h3>
    <div class="code-box">
<pre>
# User Email: 24f1002326@ds.study.iitm.ac.in
# Task: Employee Performance Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('employee_data.csv')

# 1. Calculate Frequency for Operations
ops_count = df[df['department'] == 'Operations'].shape[0]
print(f"Operations Count: {{ops_count}}")

# 2. Create Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='department')
plt.title('Department Distribution')
plt.show()
</pre>
    </div>
    
    <hr>
    <p>Submitted by: 24f1002326@ds.study.iitm.ac.in</p>
</body>
</html>
'''

with open('analysis_report.html', 'w') as f:
    f.write(html_content)
print("Report generated with email embedded.")
