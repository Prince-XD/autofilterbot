if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  https://github.com/prince301102/autofilterbot.git /autofilterbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMaria
fi
cd /EvaMaria
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
