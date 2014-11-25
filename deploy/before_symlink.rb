Chef::Log.info("Running deploy/before_migrate.rb...")

Chef::Log.info('Creating tilestache config from template')

if node[:opsworks][:instance][:layers].include? 'tilestache'
  service 'tilestache' do
    action :nothing
  end
  template "#{node[:tilestache][:cfg_path]}/tilestache.conf" do
    local     true
    owner     node[:tilestache][:user]
    group     node[:tilestache][:user]
    mode      0664
    source    "#{release_path}/deploy/templates/tilestache.conf.erb"
    notifies  :restart, 'service[tilestache]', :delayed
  end
else
  template "#{node[:tilestache][:cfg_path]}/tilestache.conf" do
    local     true
    owner     node[:tilestache][:user]
    group     node[:tilestache][:user]
    mode      0664
    source    "#{release_path}/deploy/templates/tilestache.conf.erb"
  end
end
