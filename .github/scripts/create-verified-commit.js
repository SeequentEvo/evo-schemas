const { createVerifiedCommit } = require('./git-utils');

module.exports = async ({ github, context }) => {
    if (!context.commitMessage) {
        throw new Error('commitMessage is required in context');
    }

    const { owner, repo } = context.repo;

    const commitSha = await createVerifiedCommit({ github, owner, repo, commitMessage: context.commitMessage });

    if (!commitSha) {
      return;
    }

    let targetBranch;
    const ref = context.ref || '';

    if (ref.startsWith('refs/heads/')) {
      targetBranch = context.ref.split('/').pop();
    } else {
      const repoData = await github.rest.repos.get({ owner, repo });
      targetBranch = repoData.data.default_branch;
    }

    await github.rest.git.updateRef({
      owner,
      repo,
      ref: `heads/${targetBranch}`,
      sha: commitSha
    });

    console.log(`Created verified commit: ${commitSha} on branch ${targetBranch}`);
};
