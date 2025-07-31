**Git Commit Message Generator**
=====================================

A Python script that uses the LangChain library and Groq's LLaMA model to generate conventional Git commit messages based on the staged changes in a repository.

**Table of Contents**
-----------------

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Troubleshooting](#troubleshooting)

**Introduction**
---------------

This script uses the LangChain library to interact with Groq's LLaMA model, which generates commit messages based on the staged changes in a Git repository. The script follows the Conventional Commit style and writes in the imperative mood.

**Usage**
-----

1. Clone this repository or copy the script to your local machine.
2. Install the required dependencies (see [Installation](#installation) section).
3. Run the script with the path to your Git repository as an argument:

```bash
python commit_message_generator.py /path/to/your/repo
```

If no path is provided, the script will use the current working directory.

**Requirements**
------------

* Python 3.8+
* LangChain library (`pip install langchain`)
* Groq API key (sign up for a free API key on the Groq website)
* Git repository with staged changes

**Installation**
------------

1. Install the LangChain library:

```bash
pip install langchain
```

2. Install the required dependencies:

```bash
pip install python-dotenv
```

**Configuration**
--------------

1. Create a `.env` file in the root of your repository with your Groq API key:

```makefile
GROQ_API_KEY=your_api_key_here
```

Alternatively, you can run the script and enter your API key when prompted.

**Troubleshooting**
-----------------

* If you encounter issues with the script, check the error messages and ensure that:
	+ Your Groq API key is valid and correctly configured.
	+ Your Git repository has staged changes.
	+ The script has the necessary permissions to access your repository.

**Contributing**
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

**License**
-------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.