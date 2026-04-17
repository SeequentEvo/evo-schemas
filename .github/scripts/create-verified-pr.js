const { createVerifiedCommit } = require('./git-utils');

module.exports = async ({ github, context }) => {
    if (!context.commitMessage) {
        throw new Error('commitMessage is required in context');
    }
    if (!context.branchName) {
        throw new Error('branchName is required in context');
    }

    const { owner, repo } = context.repo;

    const commitSha = await createVerifiedCommit({ github, owner, repo, commitMessage: context.commitMessage });

    if (!commitSha) {
      return;
    }

    const repoData = await github.rest.repos.get({ owner, repo });
    const defaultBranch = repoData.data.default_branch;

    await github.rest.git.createRef({
      owner,
      repo,
      ref: `refs/heads/${context.branchName}`,
      sha: commitSha
    });

    const pr = await github.rest.pulls.create({
      owner,
      repo,
      title: context.prTitle || context.commitMessage,
      head: context.branchName,
      base: defaultBranch,
      body: context.prBody || ''
    });

    console.log(`Created PR #${pr.data.number}: ${pr.data.html_url}`);
};

