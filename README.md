# Prophet - AI-Powered Python Bug Finding Tool (Alpha Demo)

**Discover potential bugs in your Python code with Prophet, an AI-driven tool leveraging cutting-edge language models. This repository showcases a demo of Prophet's capabilities.**

**Important Note:** Prophet is currently in its alpha stage. While DeepSeek and Gemini models are readily available, the "Prophet" model requires active server operation for bug detection.

**[Visit Our Website](https://prophet.pythonanywhere.com/)**

## Getting Started

**1. Installation (VS Code Extension):**

   - Open Visual Studio Code.
   - Navigate to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X).
   - Search for "Prophet".
   - Click "Install" from the [Prophet Extension Marketplace Page](https://marketplace.visualstudio.com/items?itemName=Prophet.prophet-test-tool).

**2. Login:**

   - Upon activation, the extension will prompt you for login credentials.
   - Enter your provided username and password.

**3. Running Prophet Analysis:**

   - Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).
   - Type "Run Prophet" and select it.
   - **Choose a Model:** Select the AI model you want to use for analysis (Prophet, DeepSeek, or Gemini).
   - **Select a File:** Choose the Python file you wish to analyze for bugs.

**4. Viewing Results:**

   - **Notifications:**
     - A success notification will appear if no bugs are found.
     - An error notification will appear if potential bugs are detected.
   - **Output Channels:**
     - **"Prophet Analysis"**: Provides a concise summary of the analysis results.
     - **"Prophet Analysis Detailed"**: Displays the full, detailed response from the chosen AI model.

## Key Features
* **AI-Driven Bug Detection:** Leverages powerful language models to identify potential issues in your Python code.
* **Multi-Model Support:** Choose between Prophet, DeepSeek, and Gemini models for varied analysis perspectives.
* **Clear Output Integration:** Delivers analysis results directly within VS Code, with both summary and detailed views.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
