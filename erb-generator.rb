#!/usr/bin/env ruby

require 'json'

json = File.read('tilestache.cfg')
data = JSON.parse(json)

data["layers"].each do |key, val|
  val["allowed origin"] = "*"
  val["cache lifespan"] = val["cache lifespan"] || "<%= node[:mapzen_tilestache][:max_age] %>"
  val["maximum cache age"] = val["maximum cache age"] || "<%= node[:mapzen_tilestache][:max_age] %>"
  if val["provider"]["class"] == "TileStache.Goodies.VecTiles:Provider"
    val["provider"]["kwargs"]["dbinfo"]["host"] = "<%= node[:mapzen][:postgresql][:endpoint] %>"
    val["provider"]["kwargs"]["dbinfo"]["port"] = 5432
    val["provider"]["kwargs"]["dbinfo"]["user"] = "gisuser"
    val["provider"]["kwargs"]["dbinfo"]["password"] = "<%= node[:mapzen][:secrets][:postgresql][:password][:gisuser] %>"
    val["provider"]["kwargs"]["dbinfo"]["database"] = "tilestache-gis"
    val["provider"]["kwargs"]["queries"] = val["provider"]["kwargs"]["queries"].collect { |x| if x != nil && x.start_with?("queries/") then "<%= node[:mapzen_tilestache][:query_dir_name] %>/current/"+x else x end }
  end
  data["layers"][key] = val.sort.to_h
end

File.open('deploy/templates/tilestache.conf.erb', 'w') do |file|
  file.write(<<-EOF
{
  "cache": {
    <%- if node[:mapzen_tilestache][:cache][:type] == 'memcache' -%>
    "name": "Memcache",
    "servers": [
      <%= node[:opsworks][:layers][:memcached][:instances]
            .map { |name, config| '"' + name + ':11211' + '"' }
            .join(', ') %>
    ],
    "revision": 0,
    "key prefix": "tilestache-<%= node[:mapzen][:environment] %>"
    <%- elsif node[:mapzen_tilestache][:cache][:type] == 'tileglue' -%>
    "class": "tileglue.make_tilestache_s3_cache",
    "kwargs": {
      "bucket": "<%= node[:mapzen_tilestache][:cache][:tileglue][:s3][:bucket] %>",
      "reduced_redundancy": <%= node[:mapzen_tilestache][:cache][:tileglue][:s3][:reduced_redundancy] %>,
      "path": "<%= node[:mapzen_tilestache][:cache][:tileglue][:s3][:path] %>",
      "redis_host": "<%= node[:mapzen_tilestache][:cache][:tileglue][:redis][:host] %>",
      "redis_cache_set_key": "<%= node[:mapzen_tilestache][:cache][:redis][:cache_set_key] %>"
    }
    <%- else -%>
    "name": "Test",
    "verbose": false
    <%- end -%>
  },
  "layers": {
EOF
  )

  layers_data = []
  data['layers'].each do |k, v|
    layers_data << '"' + k + '": ' + JSON.pretty_generate(v, {:indent => '    '})
  end

  layers_str = layers_data.join(",\n    ")
  file.write('    ' + layers_str + "\n")

  file.write(<<-EOF
  },
  "logging": "info"
}
EOF
  )

end
