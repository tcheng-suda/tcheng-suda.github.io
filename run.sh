#!/bin/bash
# run.sh - Run Jekyll site locally
# Usage: ./run.sh

cd "$(dirname "$0")"

# Install dependencies if needed
if [ ! -f Gemfile.lock ]; then
  echo "Installing dependencies..."
  bundle install
fi

# Start Jekyll server
echo "Starting Jekyll server at http://localhost:4000"
bundle exec jekyll serve --livereload
