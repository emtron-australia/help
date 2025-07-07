# Emtron Resource Centre

## Basics
The Emtron Resource Centre website runs on [Hugo](https://gohugo.io/), a website framework that displays content using the mardown file format. Markdown is a simple syntax for formatting text and displaying content.

Refer here for a good [Markdown Guide](https://www.markdownguide.org/cheat-sheet/).

All documentation lives in the `content` directory. The website will automatically display pages and lay them out into categories based on the directory structure.
Each directory (category) needs a file called `_index.md` which tells the site what the title is, and what to show when the category itself is clicked on, for example: showing a list of child topics.
![_index.md example](/img/readme/index_md.png)

### Weight
The `Weight: x` property controls the ordering of categories. The lowest weight will float to the top while the highest weight will sink to the bottom. When the property is opmited, the highest weight is set by default. The number can be any integer value. 

### Images
Images live in the `img` directory. You can put images in there then reference them in any content file.

### Shortcodes
The theme we're using allows the use of `Shortcodes` to further extend the markdown syntax. Refer the the [Relearn Theme Shortcode Guide](https://mcshelby.github.io/hugo-theme-relearn/shortcodes/index.html) for details. 

## Editing on Github
The whole repo can be edited on GitHub. Once the changes are committed the website will update in a couple of minutes. Github lets you preview the files to see the rendered result but it won't show everything, in particular the shortcodes.

## Editing in Visual Studio Code
A much more feature rich editing experience involves using VS Code the edit the files and running the website locally to see instant changes. Once you're satisfied, you can commit your changes.

1. **Install Visual Studio Code:** [Visual Studio Code Downloads](https://code.visualstudio.com/).
2. **Install a git client** such as:
   - [GitHub Desktop](https://desktop.github.com/download/): Free, fairly simple to use.
   - [Fork](https://git-fork.com/): Once off $50 purchase, but extrememly good UI for tracking changes and branches.
3. **Clone the repository.** GitHub Desktop example:
   1. File > Clone Repository.
   2. Choose emtron-australia/help, give it a local location and click `Clone`.
   ![Clone Repo](/img/readme/clone.png)
   3. Click `Fetch` to sync the remote repo with your local one. This does not download changes.
   4. If there are changes on the remote repository, the button will show `Pull origin`. Click `Pull origin` to download the remote updates. You need to make sure you don't have any uncommited changes to do this.
  ![Pull Remote](/img/readme/pull.png)
5. **Install Hugo:** Open an command prompt and enter:
    ```
    winget install Hugo.Hugo.Extended
    ```
    enter `yes` to install it.
6. **Set up VS Code:**
   1. Install a mardown preview extension such as this one:
   ![Markdown Preview](/img/readme/markdown_preview.png)
   2. Open the folder: File > Open Folder. Choose the cloned help repository folder.
   ![Open Folder](/img/readme/open_folder.png)
7. **Edit with Preview:** Open a markdown file and click the open preview button at the top.
   ![Preview Button](/img/readme/md_preview.png)
8. **Edit with full live website preview:**
   1. In VS Code goto Terminal > New Terminal. The current working directory should be the repository folder.
   2. In the terminal window enter:
   ```
   hugo serve 
   ```
   *If you want to render content marked as draft enter:*
   ```
   hugo serve --buildDrafts
   ```
   ![hugo serve](/img/readme/hugo_serve.png)

   3. Open your browser and navigate to http://localhost:1313/ to view the live site. Whenever you save a file, the site will instantly rebuild and update with your changes.
   ![localhost:1313](/img/readme/localhost.png)
9. **Commit and Push Changes:** 
   1. When you're done editing. **Commit you changes** with a commit message in the git client by pushing `Commit x files to master`.
   ![git commit](/img/readme/git_commit.png)
   2. **Push the changes** to the remote repository by clicking `Push origin`.
   ![git push](/img/readme/git_push.png)
10. **DONE!** After a few minutes, the real website will rebuild and update automatically.

### Regular Edit Workflow
Once setup, the workflow for updating the website is very simple.
1. Fetch and pull the repository to sync up.
2. Open VS Code and open the repo folder.
3. Optionally, run the ```hugo serve``` command in the terminal to launch the live preview.
4. Edit away...
5. Commit and push changes.





