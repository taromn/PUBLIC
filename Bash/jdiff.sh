diff <(jq --sort-keys . $1) <(jq --sort-keys . $2)



# Reference
# https://blog.pinkumohikan.com/entry/diff-json-smartly-by-jq