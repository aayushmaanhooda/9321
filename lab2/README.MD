
# 🚀 Lab 2 Setup Instructions

To get started with **Lab 2** activities, it's a **good practice** (though not mandatory) to create a **virtual environment**. A virtual environment isolates all your dependencies, keeping your workspace clean and preventing conflicts with global packages.

---

## ✅ **1. Setting Up a Virtual Environment**

1. **Navigate to your `lab2` folder** in the terminal.

2. **Run the following command to create a virtual environment:**
   ```bash
   python3 -m venv <your_env_name>
   ```
   **Example:**
   ```bash
   python3 -m venv env
   ```

3. **Activate the virtual environment:**

   - **On MacOS/Linux:**
     ```bash
     source env/bin/activate
     ```

   - **On Windows:**
     ```bash
     .\env\Scripts\activate
     ```

4. ✅ Once activated, your terminal prompt should change to reflect the active environment (e.g., `(env)`).

---

## ✅ **2. Installing Dependencies**

You have **two options** to install the required dependencies:

### **Option 1: Using `requirements.txt` (Recommended)**
1. **Place the `requirements.txt` file** into your `lab2` folder.
2. **Run:**
   ```bash
   pip install -r requirements.txt
   ```

---

### **Option 2: Install Packages Manually**
If you don’t have a `requirements.txt` file, install the required packages individually:

```bash
pip install pandas requests flask "fastapi[all]" pymongo 
```

- **`pandas`** → For data manipulation.
- **`requests`** → To make HTTP requests.
- **`flask`** → To build lightweight web applications.
- **`fastapi`** → For modern, high-performance APIs.
- **`uvicorn`** → ASGI server for running FastAPI.

---

## ✅ **3. Setting Up MongoDB for Activity 3**

In **Activity 3**, we will use **MongoDB**. Follow the steps below to install and run MongoDB:

### 📥 **Step 1: Install MongoDB**

- **Go to the official MongoDB installation guide**:  
  👉 [MongoDB Installation Docs](https://www.mongodb.com/docs/manual/installation/)

### 💡 **For Mac Users (Using Homebrew):**
```bash
brew install mongodb-community
```

---

### ⚡ **Step 2: Managing MongoDB Services**

- **Start MongoDB:**
  ```bash
  brew services start mongodb-community
  ```

- **Stop MongoDB:**
  ```bash
  brew services stop mongodb-community
  ```

If you're on **Windows** or **Linux**, follow the official documentation for your specific OS.

---

### 📡 **Step 3: Verify MongoDB is Running**
To confirm MongoDB is running, execute:

```bash
mongo
```
Or, for newer installations:
```bash
mongosh
```

If it connects to the MongoDB shell, you're good to go! ✅

---

## ✅ **4. Moving on to Lab Activities**

Now that everything is set up:

- 🚀 Start with **Activities 1-4** as outlined in your lab instructions.
- 🔄 Ensure you use the virtual environment for all activities to maintain consistency.

---

## 🎁 **BONUS: Flask & FastAPI Versions of Activity 4**

As an added bonus, I've provided **two additional activities** that replicate **Activity 4** using both:

- **Flask** → For building simple REST APIs.
- **FastAPI** → For high-performance APIs with built-in docs (Swagger at `/docs`).

Feel free to explore both to understand the differences and benefits of each framework!

---

💡 **Pro Tip:**  
- **Deactivate the virtual environment** when done:
  ```bash
  deactivate
  ```
- **Re-activate** whenever you return to work on **Lab 2**.

---

🎉 **That's it for the setup! Now, dive into the activities and have fun coding! 🚀**
