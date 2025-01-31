# CT-421 AI - Assignment 1

### 1. Clone the Repository

```sh
git clone https://github.com/FionnMcA/ct-421-ai.git
cd ct-421-ai/assignment-1
```

### 2. Create and Activate a Virtual Environment

```sh
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

For Windows, use:
```sh
.venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install matplotlib
```

### 4. Adjust the Code

- Uncomment the `#1` section to run the `vary_parameters` method and comment out the `#2` section.
- At the top of main modify parameters such as:
  - GENERATIONS
  - POPULATION_SIZE
  - MUTATION_RATE
  - CROSSOVER_RATE

### 5. Run the Script

```sh
python main.py
```

### 6. Running in Jupyter Notebook (Alternative)

If you prefer running the code in Jupyter Notebook, install Jupyter if you haven't already:

```sh
pip install jupyter
```

Start Jupyter Notebook:

```sh
jupyter notebook main.ipynb
```

