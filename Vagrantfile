Vagrant.configure("2") do |config|
  config.ssh.insert_key = false
  config.vm.box = "bento/ubuntu-17.10"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end
end