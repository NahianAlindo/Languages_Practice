# my repl fpr ruby

BEGIN{
  puts "Initializing Ruby";
}

puts "hello, alindo";
# hi alindo

print <<EOF
  This is the first way
EOF

print <<'EOC' # execute commands
  echo hi
  echo lo
EOC

# stacking \

print <<"foo", <<"bar"
  I said foo
foo
  I said bar
bar

END{
  puts "Terminating ruby";
}