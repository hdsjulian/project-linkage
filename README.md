- [Backend setup](#backend-setup)
  - [Installing python](#installing-python)
    - [Install the prerequisite system libraries](#install-the-prerequisite-system-libraries)
    - [Option1 : System install](#option1---system-install)
    - [Option 2 (recommended): Using asdf version manager](#option-2--recommended---using-asdf-version-manager)
  - [Installing backend dependencies](#installing-backend-dependencies)
- [Frontend setup](#frontend-setup)
  - [Installing nodejs](#installing-nodejs)
    - [Install the prerequisite system libraries](#install-the-prerequisite-system-libraries-1)
    - [Option1 : System install](#option1---system-install-1)
    - [Option 2 (recommended): Using asdf version manager](#option-2--recommended---using-asdf-version-manager-1)
  - [Installing npm dependencies](#installing-npm-dependencies)
- [Setting up the environment](#setting-up-the-environment)
- [Running the backend locally](#running-the-backend-locally)
- [Running the frontend locally](#running-the-frontend-locally)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Backend setup

## Installing python

### Install the prerequisite system libraries

Please refer to the [Pyenv FAQ](https://github.com/pyenv/pyenv/wiki#suggested-build-environment).

Example for Ubuntu/Debian/Mint:

```
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

```

### Option1 : System install

Please check the file `.tool-versions` for the exact version needed for this project.

### Option 2 (recommended): Using asdf version manager

In order to avoid relying on a unique system-based installation, and to be able to switch versions easily, you can use the [asdf](http://asdf-vm.com) method:

1. [Install asdf](http://asdf-vm.com/guide/getting-started.html)
1. In your terminal, `cd` to the root folder of this project containing the file `.tool-versions` and run the command:
   ```
   asdf install
   ```
1. With the command:
   ```
   python --version
   ```
   ensure that the version number matches the one defined in `.tool-versions`
1. With the command:
   ```
   pip --version
   ```
   ensure that pip is installed

## Installing backend dependencies

Use the command:

```
pip install -r requirements.txt
```

If you use `asdf`, make sure that the installed requirements are accessible:

```
asdf reshim
```

# Frontend setup

## Installing nodejs

### Install the prerequisite system libraries

[TODO]

### Option1 : System install

### Option 2 (recommended): Using asdf version manager

1. [Install asdf](http://asdf-vm.com/guide/getting-started.html)
1. In your terminal, `cd` to the root folder of this project containing the file `.tool-versions` and run the command:
   ```
   asdf install
   ```
1. With the command:
   ```
   nodejs --version
   ```
   ensure that the version number matches the one defined in `.tool-versions`
1. Install `yarn`, with the version matching the one under `"engines"` in `package.json`.

   Example:

   ```
   npm install --global yarn@1.22.10
   ```

## Installing npm dependencies

1. Run the command:

```
yarn
```

(shortcut for `yarn install`)

# Setting up the environment

Create your local `.env` file:

```
cp .env.example .env
```

Make sure that all needed envionment variables are present in this file.
For secret environment variables, please ask the project lead developer for a copy of their `.env` file.

This `.env` file is specific to your own local environment. Feel free to change its values to accomodate your specific needs.

# Running the backend locally

For development, use the command:

[TODO]

# Running the frontend locally

1. For development, use the command:

   ```
   yarn dev
   ```

1. Visit your local frontend url.\
   (default: http://localhost:5000)
