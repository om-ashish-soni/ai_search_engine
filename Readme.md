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

2. **Environment Setup**:
   - Create .env file in /ai_search_ui directory of project
   - Replace .env content with 
   ```
   HF_TOKEN=YOUR_HF_API_TOKEN
   ```
   - [How to get your hf token for free](https://huggingface.co/docs/hub/en/security-tokens)
      * Log in to [huggingface](https://huggingface.co/)
      * Go to Profie > then go to Setttings > then go to Access Tokens tab
      * [Access Tokens Page](https://huggingface.co/settings/tokens)
      * If there exists Access Token then copy it and paste it as HF_TOKEN in .env file of project
      * If Access Token does not exist then click on new token Write the "Name of Token" and Select the "Type of Token" (Read / Write) Access.
      * After creating copy the token and paste it as HF_TOKEN in .env file of project.


3. **Running the UI**:
   - Navigate to the `ai_search_ui` directory:
     ```sh
     cd ai_search_ui
     ```
   - Create Virtual Enviornment & Install Dependencies
   * For windows ( git bash )
        ```sh
        python -m venv .venv
        source .venv/Scripts/activate
        pip install -r requirements.txt
        ```
    * For windows ( cmd )
        ```sh
        python -m venv .venv
        .venv\Scripts\activate
        pip install -r requirements.txt
        ```
    * For Linux & Mac
        ```sh
        python -m venv .venv
        souce .venv/bin/activate
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
     npx playwright install
     ```
3. **Environment Setup**:
   - Create .env file in root directory of project
   - Replace .env content with 
   ```
   PAGE_POOL_SIZE=5
   WEB_STORE='https://www.google.com'
   ```

4. **Starting the Backend**:
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

---

Feel free to modify and expand upon this README as needed to provide more detailed instructions, information about APIs, deployment steps, or any other relevant details for users and contributors.
