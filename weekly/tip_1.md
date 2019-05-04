# Updating your fork to Upstream Repository

Often after you fork a new change may occur in the upstream branch thus giving rise to merge conflicts when you try to submit a pull request. To take care of this before you start editing from your local fork, run the below commands:

#### Add the remote, call it "upstream":

`git remote add upstream https://github.com/whoever/whatever.git`

#### Fetch all the branches of that remote into remote-tracking branches, such as upstream/master:

`git fetch upstream`

#### Make sure that you're on your master branch:

`git checkout master`

#### Rewrite your master branch so that any commits of yours that aren't already in upstream/master are replayed on top of that other branch:

`git rebase upstream/master`