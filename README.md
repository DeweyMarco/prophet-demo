# Prophet - AI-Powered Python Bug Finding Tool (Alpha Demo)

**Discover potential bugs in your Python code with Prophet, an AI-driven tool leveraging cutting-edge language models. This repository showcases a demo of Prophet's capabilities.**

**Important Note:** Prophet is currently in its alpha stage. While DeepSeek and Gemini models are readily available, the "Prophet" model requires active server operation for bug detection.

**[Visit Our Website](https://prophet.pythonanywhere.com/)**

## Getting Started
1.  **Installation:**
    * Open VS Code.
    * Go to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X).
    * Search for "Prophet".
    * Click "Install".
    * [Prophet Extension](https://marketplace.visualstudio.com/items?itemName=Prophet.prophet-test-tool)
2.  **Login:**
    * Upon activation, the extension will prompt you to log in.
    * Use your password.
3.  **Testing a Python File:**
    * Open the Toggle Panel (Ctrl+J or Cmd+J).
    * Select the "Prophet AI Debugger" tab. 
    * Click "Run Prophet" on the top right of the Toggle Panel.
    * Select the file you wish to have evaluated.
4.  **Viewing Test Results:**
    * An error popup will appear if the model found a bug.
    * A success popup will appear if the model found no bugs.
    * The full response will be displayed in the Toggle Panel.

## Features

* **Automated Test Generation:** Uses an AI API to test files based on your Python code.
* **Output Integration:** Provides a curated response from the an LLM explaining the bugs. 
* **Simple Login:** Requires a basic password login to access the testing features.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
