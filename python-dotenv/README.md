Here’s a simple example of how to use the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from a `.env` file in a Python project.

---

### 📦 Step 1: Install the package

```bash
pip install python-dotenv
```

---

### 📁 Step 2: Create a `.env` file

Create a `.env` file in the root of your project:

```env
# .env
API_KEY=your_api_key_here
DEBUG=True
PORT=5000
```

---

### 🐍 Step 3: Use it in your Python script

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
api_key = os.getenv('API_KEY')
debug = os.getenv('DEBUG') == 'True'
port = int(os.getenv('PORT', 8000))  # default to 8000 if PORT not set

print(f"API_KEY: {api_key}")
print(f"DEBUG: {debug}")
print(f"PORT: {port}")
```

---

### ✅ Output

If your `.env` file looks like this:

```env
API_KEY=abcd1234
DEBUG=True
PORT=5000
```

Your output will be:

```
API_KEY: abcd1234
DEBUG: True
PORT: 5000
```

---

Let me know if you want an example using `FastAPI`, `Flask`, or anything else!