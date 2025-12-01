import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import numpy as np

# --- VERIFICATION HEADER ---
# Student Email: 24f1002326@ds.study.iitm.ac.in

# 1. Data Generation
np.random.seed(42)
departments = ['Sales', 'HR', 'R&D', 'Marketing', 'Operations', 'Finance']
data = {
    'employee_id': [f'EMP{i:03d}' for i in range(1, 101)],
    'department': np.random.choice(departments, 100),
    'performance_score': np.random.uniform(60, 100, 100)
}
df = pd.DataFrame(data)

# 2. Analysis
ops_count = df[df['department'] == 'Operations'].shape[0]
print(f"Operations Department Count: {ops_count}")

# 3. Visualization
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.histplot(data=df, x='department', hue='department', legend=False, palette='viridis')
plt.title('Distribution of Employees by Department')
plt.tight_layout()

# Save Plot to Base64
buffer = BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
img_str = base64.b64encode(buffer.read()).decode('utf-8')
plt.close()

# 4. Generate HTML with Embedded Email
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Employee Performance - 24f1002326@ds.study.iitm.ac.in</title>
    <style>
        body {{ font-family: sans-serif; margin: 40px; color: #333; }}
        .header {{ background: #e3f2fd; padding: 20px; border-left: 5px solid #2196f3; margin-bottom: 20px; }}
        .code-box {{ background: #f5f5f5; padding: 15px; border-radius: 5px; font-family: monospace; overflow-x: auto; }}
        .footer {{ margin-top: 40px; font-size: 0.9em; color: #666; border-top: 1px solid #ddd; padding-top: 10px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Employee Performance Analysis</h1>
        <p><strong>Verified Author:</strong> 24f1002326@ds.study.iitm.ac.in</p>
    </div>

    <h2>1. Analysis Results</h2>
    <p>The frequency count for the <strong>Operations</strong> department is: <strong>{ops_count}</strong></p>

    <h2>2. Visualization</h2>
    <img src="data:image/png;base64,{img_str}" alt="Department Distribution Histogram" style="max-width:100%; border: 1px solid #ccc;">

    <h2>3. Source Code</h2>
    <p>This analysis was generated using the following Python code:</p>
    <div class="code-box">
<pre>
import pandas as pd
import seaborn as sns

# Email: 24f1002326@ds.study.iitm.ac.in
# Task: Employee Performance Analysis

# Load Data
df = pd.read_csv('data.csv')

# Calculate Operations Count
ops_count = df[df['department'] == 'Operations'].shape[0]
print(f"Operations Count: {{ops_count}}")

# Plot Histogram
sns.histplot(data=df, x='department')
</pre>
    </div>

    <div class="footer">
        <p>Submission ID: 24f1002326@ds.study.iitm.ac.in</p>
    </div>
</body>
</html>
'''

with open('analysis_report.html', 'w') as f:
    f.write(html_content)
print("HTML Report generated successfully.")
