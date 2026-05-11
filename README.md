To properly test the application, you need to run both the frontend and the backend servers.

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the backend server:**
   ```bash
   python app.py
   ```

3. **Run the frontend server:**
   - Open the `index.html` file in a web browser.
   - It is recommended to use a local web server to serve the `index.html` file to avoid potential CORS issues. You can use Python's built-in HTTP server for this:
     ```bash
     python -m http.server 8000
     ```
   - Then, open your web browser and navigate to `http://localhost:8000`.