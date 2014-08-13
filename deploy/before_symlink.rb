Chef::Log.info("Running deploy/before_migrate.rb...")

Chef::Log.info('Creating tilestache config from template')
service 'tilestache' do
  action :nothing
end

execute 'restart tilestache' do
  action  :nothing
  command 'sv -w 60 restart tilestache'
end

template "#{node[:tilestache][:cfg_path]}/tilestache.conf" do
  local     true
  owner     node[:tilestache][:user]
  group     node[:tilestache][:user]
  mode      0664
  source    "#{release_path}/deploy/templates/tilestache.conf.erb"
  notifies  :run, 'execute[restart tilestache]', :delayed
end
