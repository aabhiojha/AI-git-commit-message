**gcommit: AI-Powered Git Commit Message Generator**
=====================================================

**Table of Contents**
-----------------

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Requirements](#requirements)
6. [Contributing](#contributing)
7. [License](#license)

**Introduction**
---------------

`gcommit` is a command-line tool that generates clear, conventional Git commit messages using an AI model (LLaMA3 via Groq API). It analyzes your staged changes (`git diff --cached`) and outputs a concise commit message following the [Conventional Commits](https://www.conventionalcommits.org/) standard.

**Features**
------------

* Generates commit messages automatically using AI
* Enforces **Conventional Commit** style (`feat:`, `fix:`, `docs:`, etc.)
* Uses staged changes as context
* Works from any Git repository directory

**Installation**
---------------

### Using `setup.sh` Script

1. Clone this repository: `git clone https://github.com/yourusername/AI-git-commit-message.git`
2. Navigate to the repository: `cd AI-git-commit-message`
3. Make the script executable: `chmod +x setup.sh`
4. Run the script: `./setup.sh`

### Using `pip install`

1. Clone this repository: `git clone https://github.com/yourusername/AI-git-commit-message.git`
2. Navigate to the repository: `cd AI-git-commit-message`
3. Install dependencies: `pip install .`

**Usage**
-----

1. Stage your changes: `git add .`
2. Run `gcommit`: `gcommit`
3. The script will:
	* Detect the Git repository
	* Read staged changes
	* Generate an AI-powered commit message
	* Print the suggested message

**Requirements**
------------

* Python 3.8+
* Groq API key
* Dependencies listed in `requirements.txt`

**Contributing**
------------

Pull requests are welcome! For major changes, open an issue first to discuss your ideas.

**License**
-------

MIT License. See `LICENSE` for details.

**Example Use Case**
-----------------

```bash
$ git add .
$ gcommit
Using git repo path: /home/user/myrepo
fix: install generate_commit script as gcommit
```

Copy the output and use it in your commit:

```bash
git commit -m "fix: install generate_commit script as gcommit"
```

**Known Issues**
--------------

* None reported yet

**Future Development**
-------------------

* Add support for multiple AI models
* Improve commit message generation accuracy
* Integrate with popular Git tools and workflows

**Acknowledgments**
----------------

* Groq API for providing AI model access
* Conventional Commits for defining commit message standards