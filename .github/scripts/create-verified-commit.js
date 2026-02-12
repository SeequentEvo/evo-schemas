const fs = require('fs');
const { execSync } = require('child_process');

module.exports = async ({ github, context }) => {
    const headSha = execSync('git rev-parse HEAD').toString().trim();

    const changedFiles = execSync('git diff --name-only HEAD').toString().trim().split('\n').filter(f => f);

    if (changedFiles.length === 0) {
      console.log('No changes to commit');
      return;
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
      owner: context.repo.owner,
      repo: context.repo.repo,
      tree: treeData,
      base_tree: headSha
    });

    const commit = await github.rest.git.createCommit({
      owner: context.repo.owner,
      repo: context.repo.repo,
      message: 'Update to schema docs',
      tree: tree.data.sha,
      parents: [headSha]
    });

    const branchName = context.ref.split('/').pop();
    await github.rest.git.updateRef({
      owner: context.repo.owner,
      repo: context.repo.repo,
      ref: `heads/${branchName}`,
      sha: commit.data.sha
    });

    console.log(`Created verified commit: ${commit.data.sha}`);
};
