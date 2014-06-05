#!/usr/bin/env rake

require 'json'
require 'rainbow/ext/string'

desc 'Build environment config'
task :build do
  if ENV['CIRCLECI'] == 'true'
    if ENV['CIRCLE_BRANCH'] == 'master'
      puts 'Building tilestache config'.color(:blue)
      sh <<-EOH
        ./erb-generator.rb
        git diff --exit-code
        if [ $? != 0 ]
        then
          echo 'Changes found, committing and pushing'
          git config user.email 'circle@circleci'
          git config user.name 'circle'
          git commit -am 'COMMITTED VIA CIRCLECI: tilestache config update'
          git push origin master
        else
          echo "No changes found, we're done here"
        fi
      EOH
    end
  end
end

task default: 'build'
