FROM ros:jazzy
ARG USERNAME=sudohex
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Delete user if it exists in container
RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi

# Create the user and add sudo support
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN apt-get update && apt-get upgrade -y

# Install python3-pip, python3-venv, zsh and curl (needed for installing Oh My Zsh)
RUN apt-get update && apt-get install -y python3-pip python3-venv zsh curl

USER $USERNAME

# Create a Python virtual environment (with system packages)
RUN python3 -m pip install --upgrade pip virtualenv --break-system-packages && \
    python3 -m venv --system-site-packages /home/$USERNAME/ros2_venv

# Copy the requirements file into the container
COPY --chown=$USERNAME:$USERNAME requirements.txt /home/$USERNAME/requirements.txt

# Install Python packages from requirements.txt using the virtual environment's pip
RUN /home/$USERNAME/ros2_venv/bin/pip install -r /home/$USERNAME/requirements.txt

# Install Oh My Zsh in unattended mode
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Install zsh-autosuggestions and zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${HOME}/.oh-my-zsh/custom/plugins/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${HOME}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting

# Copy custom .zshrc from the build context to override the generated one
COPY --chown=$USERNAME:$USERNAME configs/.zshrc /home/$USERNAME/.zshrc

# Set the default shell to zsh
ENV SHELL /usr/bin/zsh
CMD ["/usr/bin/zsh"]
