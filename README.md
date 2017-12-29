# Eggdrop script to retrieve pricing information for IRC

## dependencies are tcl and libssl-dev

### Debian based
sudo apt-get install tcl-dev libssl-dev git

### Fedora based
sudo dnf install tcl-devel openssl-devel git

### Centos based
sudo yum install tcl-devel openssl-devel git

### compile eggdrop as non root user
```
cd ~
git clone https://github.com/loeken/cryptocompare-irc-eggdrop
cd cryptocompare-irc-eggdrop
wget ftp://ftp.eggheads.org/pub/eggdrop/GNU/eggdrop1.8-latest.tar.gz
tar xvfz eggdrop1.8-latest.tar.gz
mv eggdrop-1.8.2/ eggdrop_src
cd eggdrop_src
./configure --with-ssl
make config
make DEST=../eggdrop_compiled
make sslcert DEST=../eggdrop_compiled
make install DEST=../eggdrop_compiled
cd ../eggdrop_compiled
openssl genrsa -out eggdrop.key 4096
```


### edit config
change eggdrop_compiled/eggdrop.conf to your needs ( server, botnick, owner etc)

### load script inside config
add source scripts/get_btc.tcl

### start eggdrop for the first time
./eggdrop -m eggdrop.conf