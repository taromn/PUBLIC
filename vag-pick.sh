
# vagrant global-status --prune | awk '$1 == "id" {print $3, $4, $5, $6, $7}'

# vagrant global-status|awk 'length($1) == 7'

vagrant global-status | awk 'length($1) == 7 && substr($5, 1, 1) == "/"'
