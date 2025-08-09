# crew-ai-demo

## Setup

### 1. Create and Activate Virtual Environment

First, create a virtual environment in your project directory:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Initialize UV in your project
uv init
```

### 2. Install Jupyter and ipykernel

With your virtual environment activated, install Jupyter Notebook and ipykernel:

```bash
# Install Jupyter and ipykernel
pip install notebook ipykernel

# Or using UV (faster alternative)
uv pip install notebook ipykernel

# Register the kernel with Jupyter
python -m ipykernel install --user --name=crew-ai-demo --display-name="Python (crew-ai-demo)"
```

### 3. Install Project Dependencies

Install the required packages using either pip or UV:

```bash
# Option 1: Using UV (recommended for faster installation)
uv pip install -r requirements.txt

# Option 2: Using standard pip
pip install -r requirements.txt

# Or if you want to add specific packages with UV
uv add package_name
```

### 4. Launch Jupyter Notebook

Start Jupyter Notebook with:

```bash
jupyter notebook
```

### 5. Select the Correct Kernel

When working with notebooks:
1. Open your `.ipynb` file
2. Click on "Kernel" in the top menu
3. Select "Change kernel..."
4. Choose "Python (crew-ai-demo)" from the list

### 6. Stopping Jupyter

When you're done:
1. Save your notebook
2. Close the browser tab
3. In the terminal, press `Ctrl+C` twice to stop the Jupyter server
4. Deactivate the virtual environment when finished:
   ```bash
   deactivate
   ```

### 7. Clean Up

To remove the kernel registration:

```bash
jupyter kernelspec uninstall crew-ai-demo
```

To remove the virtual environment:

```bash
rm -rf .venv
```

### 8. Uninstall Jupyter and ipykernel

```bash
pip uninstall notebook ipykernel
```

### 9. Uninstall UV

```bash
uv remove
```

### Initialize UV in your project

```bash
uv init
```

### Add dependency using uv add requirements.txt

```bash
uv add -r requirements.txt
```

### Remove dependency using uv remove package_name

```bash
uv remove package_name
```

### Remove dependency using uv remove requirements.txt

```bash
uv remove requirements.txt
```

## Learning Resources

- [Google's Crash Course on CrewAI with Gemini API](https://ai.google.dev/gemini-api/docs/crewai-example) - Learn how to use CrewAI with Google's Gemini API