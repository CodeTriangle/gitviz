#!/bin/sh

# script to set up this cursed project

cp hooks/post-commit .git/hooks
cp hooks/post-commit .git/hooks/post-merge
cp hooks/post-commit .git/hooks/post-checkout
