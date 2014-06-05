#!/usr/bin/env ruby

require 'json'

json = File.read('tilestache.cfg')
data = JSON.parse(json)

output = data

output["logging"] = "info"
output["cache"] = {
	"name" => "Memcache", 
	"servers" => ["<%= memcache_vals.join('\",\"') %>"], 
	"revision"=> 0, 
	"key prefix" => "tilestache=<%= node[:mapzen][:environment] %>"
}

output["layers"].each do |key, val|  
    val["allowed origin"] = "*"
    val["cache lifespan"] = "<%= node[:mapzen_tilestache][:max_age] %>"
    val["maximum cache age"] = "<%= node[:mapzen_tilestache][:max_age] %>"
    if val["provider"]["class"] == "TileStache.Goodies.VecTiles:Provider"
    	val["provider"]["kwargs"]["dbinfo"]["host"] = "<%= node[:mapzen][:postgresql][:endpoint] %>"
       	val["provider"]["kwargs"]["dbinfo"]["port"] = 5432
       	val["provider"]["kwargs"]["dbinfo"]["user"] = "gisuser"
       	val["provider"]["kwargs"]["dbinfo"]["password"] = "<%= node[:mapzen][:secrets][:postgresql][:password][:gisuser] %>"
       	val["provider"]["kwargs"]["dbinfo"]["database"] = "gis"
       	val["provider"]["kwargs"]["queries"] = val["provider"]["kwargs"]["queries"].collect { |x| if x != nil then "<%= node[:mapzen_tilestache][:query_dir_name] %>/current/"+x end } 
    end
end

File.open('deploy/templates/tilestache.conf.erb', 'w') do |file|
  file.write("<% memcache_vals = [] -%>
	<% node[:opsworks][:layers][:memcached][:instances].map do |name, config| -%>
  	<% memcache_vals << name + ':11211' -%>
	<% end -%>\n")
  file.write(JSON.pretty_generate(output))
end
