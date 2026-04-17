const fs = require('fs');
const { execSync } = require('child_process');

/**
 * Creates a verified commit from the current working tree changes using the GitHub API.
 * Returns the commit SHA, or null if there are no changes.
 */
async function createVerifiedCommit({ github, owner, repo, commitMessage }) {
    const headSha = execSync('git rev-parse HEAD').toString().trim();

    const changedFiles = execSync('git diff --name-only HEAD').toString().trim().split('\n').filter(f => f);

    if (changedFiles.length === 0) {
      console.log('No changes to commit');
      return null;
    }

    const treeData = [];
    for (const file of changedFiles) {
      const content = fs.readFileSync(file, 'utf8');
      treeData.push({
        path: file,
        mode: '100644',
        type: 'blob',
        content: content
      });
    }

    const tree = await github.rest.git.createTree({
      owner,
      repo,
      tree: treeData,
      base_tree: headSha
    });

    const commit = await github.rest.git.createCommit({
      owner,
      repo,
      message: commitMessage,
      tree: tree.data.sha,
      parents: [headSha]
    });

    return commit.data.sha;
}

module.exports = { createVerifiedCommit };
