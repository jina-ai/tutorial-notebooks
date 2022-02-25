# Learning Bootcamp Tutorials

## Content best practices

### Notebooks

We put a lot of stuff in notebooks to give users an interactive learning experience. Typically this redirects them to Google Colab.

- Store notebooks first and foremost in a Git repository (repo still tbc, since it needs to be a public repo for Colab access, and LP is currently closed)
- A good way to work with notebooks in a local Git repo is [Jupyter Lab](https://jupyter.org/). Remember to run in a venv!
- Create a new folder under `/src/tutorials` for your notebook. That way if it downloads stuff it won't mess up the directory tree.
- When you've pushed your notebook you can import it into Colab from GitHub. Any changes to the notebook in the repo will be synced automatically.

![](/assets/images/colab_import.png)

#### Why do it this way?

- We use Git for everything else
- This maintains a standardized URL scheme for any notebooks on Colab
- Google love to sunset things. If they sunset Colab we'll still have our notebooks
- If you don't, Alex will shout at you :wink:

#### Tips

- If you're mentioning Colab, remember it's "Google Colab" with one `l`. Not Collab, Colllllab or Colllllllllab.
- Before pushing, clear all outputs and save the notebook
- For a nicer notebook experience (more native progress bars, etc), `!pip install ipywidgets` (no need to import)
- Remember, Colab doesn't save state or get other files from the repo except your notebook. So you'll either need to `!wget <somewhere>/requirements.txt` or `!pip install <dependencies>` in the notebook itself.
- That said, we encourage you to treat the repo like a proper repo, not just a place to put your notebook. Put a README, `.gitignore`, other relevant files. That way when another dev needs to fix/update it, they have a consistent environment.
- First test locally, then on Colab. It's easy to forget things since Colab doesn't store state :angry:
- If you have a lot of helper functions, create a `helper.py` and `!wget` it
- Jupyter and Colab have some rare bugs where one notebook won't work on the other platform. There seems to be neither rhyme nor reason to this :shrug:
- To not overflow your notebook with terminal output (when using CLI) commands, tell them to [stfu](https://gist.github.com/alexcg1/6e6718c43761d68b7404ec4aa8a0ca59)
