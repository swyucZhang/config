set -e

id=$1

BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Copying dotfiles ..........${NC}"
rsync -avz .bashrc .tmux.conf .zshrc $id:~/

echo -e "${BLUE}Installing oh-my-zsh ..........${NC}"
ssh $id 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'

echo -e "${BLUE}Installing pyenv ..........${NC}"
ssh $id 'curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash'

echo -e "${BLUE}Installing neovim ..........${NC}"
if ssh $id stat nvim.appimage \> /dev/null 2\>\&1
then
    echo "Neovim already exists"
else
    ssh $id 'wget https://github.com/neovim/neovim/releases/download/nightly/nvim.appimage'
    ssh $id 'chmod u+x nvim.appimage'
fi
ssh $id 'python -m pip install --user neovim'
ssh $id 'sh <(curl https://raw.githubusercontent.com/Alexoner/spf13-vim/3.0/bootstrap.sh -L)'
ssh $id 'vim +PlugUpdate +qall'

echo -e "${BLUE}Set zsh as default shell ..........${NC}"
ssh $id 'chsh -s $(which zsh)'

echo -e "${BLUE}Done!${NC}"
