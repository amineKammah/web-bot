wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
sudo apt-get update -y
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8 -y
sudo apt install python3-pip -y
pip3 install selenium randominfo
sudo apt-get -y install pptp-linux

rm chromedriver_linux64.zip google-chrome-stable_current_amd64.deb
chmod +x run.sh
