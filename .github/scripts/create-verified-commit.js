const { createVerifiedCommit } = require('./git-utils');

module.exports = async ({ github, context }) => {
    if (!context.commitMessage) {
        throw new Error('commitMessage is required in context');
    }

    const repoInfo = context.repo || (context.payload && context.payload.repository
        ? { owner: context.payload.repository.owner.login, repo: context.payload.repository.name }
        : null);

    if (!repoInfo) {
        console.warn('Warning: Could not create verified commit (unable to determine repository owner and name from context)');
        return;
    }

    const { owner, repo } = repoInfo;

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
