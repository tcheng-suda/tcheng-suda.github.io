#!/bin/bash
# serve.sh - Run Jekyll site in background
cd "$(dirname "$0")"
export PATH="/usr/local/opt/ruby/bin:$PATH"
nohup bundle exec jekyll serve --port 4001 > /tmp/jekyll.log 2>&1 &
echo "Jekyll started in background on http://localhost:4001"
echo "Logs: tail -f /tmp/jekyll.log"
