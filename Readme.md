# AI Search Engine - Anusandhan

Anusandhan is an AI-powered search engine designed to provide real-time search capabilities with concise answers and reference sources. It features a frontend UI written in Streamlit for easy interaction and a backend API developed using Node.js.

## Directory Structure

* ai_search_ui

    * app.py
    * LLM.py
    * requirements.txt
    * search.py
    * searching.gif
    * trans.py
    * util.py

* package-lock.json
* playwright.config.ts
* app.js
* package.json
* page_pool.js
* search_engine.js


## Setup and Usage

### Frontend (UI)

1. **Streamlit Setup**:
   - Ensure you have Python installed with Streamlit (`pip install streamlit`).

2. **Running the UI**:
   - Navigate to the `ai_search_ui` directory:
     ```sh
     cd ai_search_ui
     ```
   - Create Virtual Enviornment & Install Dependencies
        ```sh
        python -m venv venv
        venv/Scripts/activate
        pip install -r requirements.txt
        ```
   - Run the Streamlit app:
     ```sh
     streamlit run app.py
     ```
   - Access the UI in your browser at `localhost:8501` (default Streamlit address).

### Backend (API)

1. **Node.js Setup**:
   - Verify Node.js installation (`node --version`).

2. **Installing Dependencies**:
   - Install required Node.js packages:
     ```sh
     npm install
     ```

3. **Starting the Backend**:
   - From the project root, start the backend server using `nodemon`:
     ```sh
     nodemon app.js
     ```
   - The backend server will run and listen for requests.

### Additional Notes

- **Frontend (UI)**:
  - The main Streamlit app file is `app.py` in the `ai_search_ui` directory.
  - Explore the UI to interact with the search interface.

- **Backend (API)**:
  - The backend server script is `app.js` in the project root.
  - Ensure all required packages from `package.json` are installed (`npm install`).
  - Use `nodemon` to run the server for automatic restarts on file changes.

### Contributions and Feedback

This project was developed independently without external funding. Contributions and feedback are welcome through GitHub issues and pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and expand upon this README as needed to provide more detailed instructions, information about APIs, deployment steps, or any other relevant details for users and contributors.
