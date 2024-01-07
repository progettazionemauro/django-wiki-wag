#!/bin/bash

HOOKS_DIR=git-hooks
GIT_HOOKS_DIR=.git/hooks

# Create git-hooks directory if it doesn't exist
[ ! -d "$HOOKS_DIR" ] && mkdir $HOOKS_DIR

# Copy hooks to git-hooks (this is for your local setup)
# NOTE: Only do this if you want to automatically copy hooks. Be careful with this!
for hook in $(ls $GIT_HOOKS_DIR); do
  cp $GIT_HOOKS_DIR/$hook $HOOKS_DIR/
done

# Create symbolic links (this is for setup after cloning)
for hook in $(ls $HOOKS_DIR); do
  ln -s ../../$HOOKS_DIR/$hook $GIT_HOOKS_DIR/$hook
done
